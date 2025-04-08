from research_agent import ResearchAgent
from notes_agent import NotesAgent
from shared_memory import SharedMemory
from config import *
import time
import os

def main():
    print("Starting Collaborative Agents Framework...")
    
    # Initialize shared memory
    memory = SharedMemory()
    
    # Initialize agents
    research_agent = ResearchAgent(SCRAPYBARA_API_KEY, memory)
    notes_agent = NotesAgent(memory, NOTES_FILE_PATH)
    
    try:
        # Set up research agent
        research_agent.setup()
        
        # Run the research and notes tasks
        for topic in RESEARCH_TOPICS:
            # Research agent researches the topic
            research_agent.search_topic(topic)
            
            # Notes agent processes the research
            notes_agent.process_research(topic)
            
            # Small delay between topics
            time.sleep(2)
        
        # Generate summary of all research
        notes_agent.summarize_all_research()
        
        print(f"\nCollaborative task completed! Research notes saved to {NOTES_FILE_PATH}")
        
    except Exception as e:
        print(f"Error in collaborative agents framework: {e}")
    finally:
        # Cleanup
        research_agent.cleanup()
        
if __name__ == "__main__":
    main()