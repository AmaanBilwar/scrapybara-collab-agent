from scrapybara import Scrapybara
from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup

class ResearchAgent:
    """Agent that searches the web for information"""
    
    def __init__(self, api_key, shared_memory):
        self.client = Scrapybara(api_key=api_key)
        self.shared_memory = shared_memory
        self.instance = None
        self.browser = None
        self.page = None
        
    def setup(self):
        """Set up the browser instance"""
        print("Research Agent: Setting up browser...")
        self.instance = self.client.start_ubuntu()
        cdp_url = self.instance.browser.start().cdp_url
        
        playwright = sync_playwright().start()
        self.browser = playwright.chromium.connect_over_cdp(cdp_url)
        self.page = self.browser.new_page()
        return self
        
    def search_topic(self, topic, site="https://en.wikipedia.org/wiki/"):
        """Search for information on a topic"""
        print(f"Research Agent: Researching '{topic}'...")
        
        # Adjust URL for Wikipedia search
        if "wikipedia.org" in site:
            search_url = f"{site}{topic.replace(' ', '_')}"
        else:
            search_url = f"{site}search?q={topic.replace(' ', '+')}"
            
        self.page.goto(search_url)
        time.sleep(2)  # Allow page to load
        
        # Get content
        html_content = self.page.content()
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Extract information based on site
        if "wikipedia.org" in site:
            # For Wikipedia, get the first few paragraphs
            paragraphs = soup.select("div.mw-parser-output > p")
            content = "\n\n".join([p.get_text() for p in paragraphs[:3]])
        else:
            # Generic extraction
            paragraphs = soup.select("p")
            content = "\n\n".join([p.get_text() for p in paragraphs[:5]])
            
        # Save research to shared memory
        self.shared_memory.save(f"research_{topic}", {
            "topic": topic,
            "source": search_url,
            "content": content,
            "timestamp": time.time()
        })
        
        # Take screenshot as evidence
        screenshot = self.page.screenshot()
        self.shared_memory.save(f"screenshot_{topic}", screenshot)
        
        print(f"Research Agent: Completed research on '{topic}'")
        return content
        
    def cleanup(self):
        """Clean up resources"""
        if self.instance:
            self.instance.browser.stop()
            print("Research Agent: Browser stopped")