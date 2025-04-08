# Scrapybara Collaborative Agents Framework
A multi-agent collaborative system built to fulfill the Scrapybara bounty requirements. This framework demonstrates how two different AI agents can work together on the same machine toward a common goal.

## Project Overview
This project creates a collaborative system with two specialized agents:

 - Research Agent: Browses the web using Scrapybara's cloud browsers to gather information on specified topics
 - Notes Agent: Processes the research, formats it, and saves it to a text file


The agents communicate through a shared memory system, allowing them to coordinate their activities effectively.

## Requirements
- Python 3.8+
- Scrapybara API key
## Installation
Clone the repository:
```bash
git clone https://github.com/yourusername/scrapybara-collab-agent.git
cd scrapybara-collab-agent
```
Install required packages:
```python
pip install -r requirements.txt
```
Create a .env file in the root directory with your Scrapybara API key:
```env
SCRAPYBARA_API_KEY=your_api_key_here
```
Install Playwright dependencies:
`playwright install`
## Project Structure
```
scrapybara-collab-agent/
├── src/
│   ├── main.py           # Main coordinator script
│   ├── research_agent.py # Web research agent using Scrapybara
│   ├── notes_agent.py    # Note-taking agent
│   ├── shared_memory.py  # Communication system between agents
│   └── config.py         # Configuration settings
├── research_notes.txt    # Output file with research notes
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

## How It Works
1. Shared Memory

The SharedMemory class provides a simple key-value store that allows agents to share data:

- `save(key, value)`: Stores data in memory
- `load(key)`: Retrieves data from memory
- `exists(key)`: Checks if a key exists
- `get_all()`: Retrieves all stored data

2. Research Agent

The ResearchAgent class uses Scrapybara to:

- Launch a cloud-based Ubuntu instance and browser
- Search Wikipedia for specified topics
- Extract relevant content from web pages
- Take screenshots as evidence
- Store research data in shared memory

3. Notes Agent

The NotesAgent class processes research data to:

- Retrieve research from shared memory
- Format the content into structured notes
- Write notes to a text file
- Create a summary of all research topics

4. Workflow

1. The main script initializes the shared memory and agents
2. For each topic in the configuration:
    - The Research Agent searches for information
    - The Notes Agent processes the data and writes notes
3. After all topics are researched, a summary is generated
4. Resources are properly cleaned up
## Configuration
Edit `config.py` to customize:
- Research topics: List of topics to research
- Target websites: List of websites to search (e.g., Wikipedia)
- Output file path: Path to save the research notes (default: research_notes.txt)
## Running the Project
Execute the main script:
`python src/main.py`
The script will:

1. Initialize both agents
2. Research each topic sequentially
3. Generate notes for each topic
4. Create a summary
5. Save all output to the specified text file_
## Demo

Link to video demonstration (add video link later)

## Bounty Fulfillment
This project fulfills the Scrapybara "Collaborative Agents" bounty requirements by:

 - [x]  Using Scrapybara technology for web research
 - [x]  Implementing multiple agents (Research + Notes) working toward a common goal
 - [x]  Creating a general framework for agent collaboration
 - [x]  Demonstrating one agent conducting research while another writes notes to a text file

## License
This project is open source and available under the MIT License.

## Acknowledgments
Scrapybara for providing the cloud browser technology
Playwright for browser automation capabilities
BeautifulSoup for HTML parsing