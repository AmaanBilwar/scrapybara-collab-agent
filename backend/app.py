import os
from pydantic import BaseModel
from dotenv import load_dotenv
from typing import List
from scrapybara import Scrapybara
from scrapybara.tools import BashTool, ComputerTool, EditTool
from scrapybara.openai import OpenAI
from playwright.sync_api import sync_playwright
from scrapybara.prompts import UBUNTU_SYSTEM_PROMPT


load_dotenv()
SCRAPYBARA_API_KEY = os.getenv("SCRAPYBARA_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# change this check later to have an LLM 

if not OPENAI_API_KEY: 
    pass

client = Scrapybara(api_key=SCRAPYBARA_API_KEY)


instance = client.start_ubuntu(
    timeout_hours=1,
)


class HNSchema(BaseModel):
    class Post(BaseModel):
        title: str
        url: str 
        points: int
    
    posts: List[Post]

stream_url = instance.get_stream_url().stream_url
print(f"Stream URL: {stream_url}")

cdp_url = instance.browser.start().cdp_url
playwright = sync_playwright().start()
browser = playwright.chromium.connect_over_cdp(cdp_url)

prompt = f'''
navigate to playtictactoe.com and play a game of tic tac toe with the computer.
make sure to win the game.
'''

response = client.act(
    model=OpenAI(
    ),
    tools=[
        BashTool(instance),
        ComputerTool(instance),
        EditTool(instance),
    ],
    system=UBUNTU_SYSTEM_PROMPT,
    prompt=f"{prompt}",
    on_step=lambda step: print(step.text),
    schema=HNSchema
)

posts = response.output.posts
print(posts)

instance.stop()