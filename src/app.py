from typing import Optional, Dict, List, Any, Type
from scrapybara import Scrapybara
from scrapybara.openai import OpenAI, UBUNTU_SYSTEM_PROMPT
from scrapybara.tools import ComputerTool, BashTool, EditTool
from scrapybara.types import Model
from scrapybara.client import UbuntuInstance
from dotenv import load_dotenv
import os
import time
import logging
import argparse
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("game-agent")

class GameConfig:
    """Configuration for a specific game"""
    def __init__(
        self, 
        name: str, 
        install_command: str, 
        start_command: str, 
        task_prompt: str,
        initial_prompt: str,
        screenshot_interval: int = 5
    ):
        self.name = name
        self.install_command = install_command
        self.start_command = start_command
        self.task_prompt = task_prompt
        self.initial_prompt = initial_prompt
        self.screenshot_interval = screenshot_interval

# Predefined game configurations
GAME_CONFIGS = {
    "dungeon_crawl": GameConfig(
        name="Dungeon Crawl Stone Soup",
        install_command="sudo apt-get install -y crawl-tiles",
        start_command="(DISPLAY=:1 /usr/games/crawl-tiles &)",
        task_prompt="""<TASK>
You are an expert gamer playing Dungeon Crawl Stone Soup (DCSS), a roguelike RPG.
Your goal is to explore the dungeon, fight monsters, and survive.

- The game is turn-based, so take your time to think
- You can see your health, mana, and status in the interface
- Use keyboard commands for movement (yuhjklbn) and actions
- '?' shows help, 'i' for inventory, 'g' to pick up items
- Read the messages at the bottom of the screen carefully

DO NOT STOP AND ASK THE USER FOR ANYTHING. JUST KEEP PLAYING THE GAME.
</TASK>""",
        initial_prompt="""I've started Dungeon Crawl Stone Soup for you. 
Create a cool character with a unique name and start exploring the dungeon!""",
        screenshot_interval=5
    ),
    "tetris": GameConfig(
        name="Tetris",
        install_command="sudo apt-get install -y vitetris",
        start_command="(DISPLAY=:1 vitetris &)",
        task_prompt="""<TASK>
You are an expert Tetris player. Your goal is to clear as many lines as possible.

- Use arrow keys to move and rotate pieces
- Left/Right arrows: Move piece horizontally
- Up arrow: Rotate piece
- Down arrow: Soft drop
- Space: Hard drop
- 'P' to pause

DO NOT STOP AND ASK THE USER FOR ANYTHING. JUST KEEP PLAYING THE GAME.
</TASK>""",
        initial_prompt="""I've started Tetris for you. Start playing and try to clear as many lines as possible!""",
        screenshot_interval=3
    ),
    "2048": GameConfig(
        name="2048",
        install_command="sudo apt-get install -y 2048",
        start_command="(DISPLAY=:1 2048 &)",
        task_prompt="""<TASK>
You are an expert 2048 player. Your goal is to combine tiles to reach the 2048 tile.

- Use arrow keys to move tiles
- Up: Move all tiles up
- Down: Move all tiles down
- Left: Move all tiles left
- Right: Move all tiles right
- 'q' to quit

DO NOT STOP AND ASK THE USER FOR ANYTHING. JUST KEEP PLAYING THE GAME.
</TASK>""",
        initial_prompt="""I've started 2048 for you. Start playing and try to reach the 2048 tile!""",
        screenshot_interval=2
    )
}

class GameAgent:
    """Base class for game-playing agents"""
    def __init__(
        self, 
        model: Model, 
        game_config: GameConfig,
        scrapybara_api_key: Optional[str] = None,
        timeout_hours: int = 1
    ):
        load_dotenv()
        self.model = model
        self.game_config = game_config
        self.client = Scrapybara(api_key=scrapybara_api_key or os.getenv("SCRAPYBARA_API_KEY"))
        self.instance = None
        self.timeout_hours = timeout_hours
        self.last_screenshot_time = 0
        self.screenshot_count = 0

    def initialize(self):
        """Initialize the Ubuntu instance and install the game"""
        logger.info(f"Starting Ubuntu instance for {self.game_config.name}")
        self.instance = self.client.start_ubuntu(timeout_hours=self.timeout_hours)
        logger.info(f"Instance URL: {self.instance.get_stream_url().stream_url}")

        # Install the game
        logger.info(f"Installing {self.game_config.name}")
        self.instance.bash(command=self.game_config.install_command)
        
        # Start the game
        logger.info(f"Starting {self.game_config.name}")
        self.instance.bash(command=self.game_config.start_command)
        
        # Wait for the game to load
        time.sleep(5)

    def handle_step(self, step):
        """Handle each step of the agent's execution"""
        if step.text:
            logger.info(f"Agent: {step.text}")
        
        # Log tool calls
        if step.tool_calls:
            for call in step.tool_calls:
                logger.info(f"Tool: {call.tool_name} → {', '.join(f'{k}={v}' for k,v in call.args.items())}")
        
        # Take screenshots periodically
        current_time = time.time()
        if current_time - self.last_screenshot_time > self.game_config.screenshot_interval:
            self.take_screenshot()
            self.last_screenshot_time = current_time

    def take_screenshot(self):
        """Take a screenshot of the game"""
        try:
            screenshot = self.instance.screenshot()
            self.screenshot_count += 1
            logger.info(f"Screenshot #{self.screenshot_count} taken")
            
            # Save screenshot to file
            screenshot_path = f"screenshots/{self.game_config.name.lower().replace(' ', '_')}_{self.screenshot_count}.png"
            os.makedirs("screenshots", exist_ok=True)
            
            # Fix: Use the correct attribute for the screenshot data
            # The screenshot object might have different attributes depending on the Scrapybara version
            if hasattr(screenshot, 'base64_image'):
                image_data = screenshot.base64_image
            elif hasattr(screenshot, 'image'):
                image_data = screenshot.image
            else:
                # Try to access the raw response data
                image_data = screenshot.raw_response.get('image', None)
                if not image_data:
                    logger.warning("Could not find image data in screenshot response")
                    return
            
            with open(screenshot_path, "wb") as f:
                f.write(image_data)
            
            logger.info(f"Screenshot saved to {screenshot_path}")
        except Exception as e:
            logger.error(f"Failed to take screenshot: {e}")

    def play_game(self):
        """Start the game-playing agent"""
        logger.info(f"Starting gameplay for {self.game_config.name}")

        self.client.act(
            model=self.model,
            tools=[
                ComputerTool(self.instance),
                BashTool(self.instance),
                EditTool(self.instance)
            ],
            system=f"{UBUNTU_SYSTEM_PROMPT}\n\n{self.game_config.task_prompt}",
            prompt=self.game_config.initial_prompt,
            on_step=self.handle_step
        )

    def cleanup(self):
        """Clean up resources"""
        if self.instance:
            logger.info("Stopping instance")
            self.instance.stop()

class GameAgentFactory:
    """Factory for creating game agents"""
    @staticmethod
    def create_agent(game_name: str, model: Model, scrapybara_api_key: Optional[str] = None, timeout_hours: int = 1) -> GameAgent:
        """Create a game agent for the specified game"""
        if game_name not in GAME_CONFIGS:
            raise ValueError(f"Unknown game: {game_name}. Available games: {', '.join(GAME_CONFIGS.keys())}")
        
        return GameAgent(
            model=model,
            game_config=GAME_CONFIGS[game_name],
            scrapybara_api_key=scrapybara_api_key,
            timeout_hours=timeout_hours
        )

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description="Game-playing agent using Scrapybara")
    parser.add_argument("--game", type=str, default="dungeon_crawl", 
                        help=f"Game to play. Available games: {', '.join(GAME_CONFIGS.keys())}")
    parser.add_argument("--api-key", type=str, help="Scrapybara API key")
    parser.add_argument("--timeout", type=int, default=1, help="Instance timeout in hours")
    parser.add_argument("--openai-key", type=str, help="OpenAI API key")
    
    args = parser.parse_args()
    
    # Create model with OpenAI
    model = OpenAI(
        api_key=args.openai_key or os.getenv("OPENAI_API_KEY")
    )
    
    # Create agent
    agent = GameAgentFactory.create_agent(
        game_name=args.game,
        model=model,
        scrapybara_api_key=args.api_key,
        timeout_hours=args.timeout
    )
    
    try:
        agent.initialize()
        agent.play_game()
    except Exception as e:
        logger.error(f"Error: {e}")
    finally:
        agent.cleanup()

if __name__ == "__main__":
    main()
