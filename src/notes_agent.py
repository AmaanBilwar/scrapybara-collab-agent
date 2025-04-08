import time
import os

class NotesAgent:
    """Agent that takes notes from research and saves them to a file"""
    
    def __init__(self, shared_memory, notes_file_path):
        self.shared_memory = shared_memory
        self.notes_file_path = notes_file_path
        
    def process_research(self, topic):
        """Process research data and write notes"""
        print(f"Notes Agent: Processing research on '{topic}'...")
        
        research_key = f"research_{topic}"
        
        # Wait for research to be available if needed
        retry_count = 0
        while not self.shared_memory.exists(research_key) and retry_count < 10:
            print(f"Notes Agent: Waiting for research on '{topic}'...")
            time.sleep(1)
            retry_count += 1
            
        if not self.shared_memory.exists(research_key):
            print(f"Notes Agent: No research found for '{topic}'")
            return False
            
        # Get research data
        research = self.shared_memory.load(research_key)
        
        # Format notes
        notes = f"""
# RESEARCH NOTES: {topic.upper()}
Date: {time.strftime('%Y-%m-%d %H:%M:%S')}
Source: {research['source']}

## CONTENT
{research['content']}

-----------------------------------------------
"""
        
        # Write notes to file
        with open(self.notes_file_path, "a", encoding="utf-8") as file:
            file.write(notes)
            
        print(f"Notes Agent: Added notes for '{topic}' to {self.notes_file_path}")
        return True
            
    def summarize_all_research(self):
        """Create a summary of all research"""
        print("Notes Agent: Creating research summary...")
        
        all_data = self.shared_memory.get_all()
        research_topics = [key.replace("research_", "") for key in all_data.keys() if key.startswith("research_")]
        
        summary = f"""
# RESEARCH SUMMARY
Date: {time.strftime('%Y-%m-%d %H:%M:%S')}

Topics Researched:
{', '.join(research_topics)}

## KEY FINDINGS
"""
        
        # Add a brief summary of each topic
        for topic in research_topics:
            research = self.shared_memory.load(f"research_{topic}")
            summary_text = research['content'][:200] + "..." if len(research['content']) > 200 else research['content']
            summary += f"\n### {topic}\n{summary_text}\n\n"
            
        # Write summary to file
        with open(self.notes_file_path, "a", encoding="utf-8") as file:
            file.write(summary)
            
        print(f"Notes Agent: Added research summary to {self.notes_file_path}")
        return True