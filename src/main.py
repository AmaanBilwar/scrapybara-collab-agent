from agents.research_agent import ResearchAgent
from shared.shared_memory import SharedMemory
from config import *
import time
import os

def main():
    print("Starting Collaborative Agents Framework...")
    
    # Initialize shared memory
    memory = SharedMemory()
    
    # Initialize agents
    research_agent = ResearchAgent(SCRAPYBARA_API_KEY, memory)
    
    try:
        # Set up research agent
        research_agent.setup()
        
        # Run the research and notes tasks
        for topic in RESEARCH_TOPICS:
            # Research agent researches the topic
            research_agent.search_topic(topic)
            
            # Notes agent processes the research
            
            # Small delay between topics
            time.sleep(2)
        
        # Generate summary of all research
        
        print(f"\nCollaborative task completed! Research notes saved to {NOTES_FILE_PATH}")
        
    except Exception as e:
        print(f"Error in collaborative agents framework: {e}")
    finally:
        # Cleanup
        research_agent.cleanup()
        
if __name__ == "__main__":
    main()