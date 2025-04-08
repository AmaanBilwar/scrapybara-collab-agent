import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Scrapybara configuration
SCRAPYBARA_API_KEY = os.getenv("SCRAPYBARA_API_KEY")
if not SCRAPYBARA_API_KEY:
    raise ValueError("SCRAPYBARA_API_KEY environment variable not set.")

# Research agent configuration
RESEARCH_TOPICS = ["Collaborative AI", "Multi-agent systems", "Agent communication"]
RESEARCH_SITES = ["https://en.wikipedia.org/wiki/", "https://scholar.google.com/"]

# Note taking agent configuration
NOTES_FILE_PATH = "research_notes.txt"