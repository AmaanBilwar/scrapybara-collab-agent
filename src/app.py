import os
from dotenv import load_dotenv
from scrapybara import Scrapybara
from scrapybara.tools import BashTool, ComputerTool, EditTool
from scrapybara.openai import OpenAI
from scrapybara.anthropic import Anthropic
from playwright.sync_api import sync_playwright
from scrapybara.prompts import UBUNTU_SYSTEM_PROMPT


load_dotenv()
SCRAPYBARA_API_KEY = os.getenv("SCRAPYBARA_API_KEY")
if not SCRAPYBARA_API_KEY:
    raise ValueError("SCRAPYBARA_API_KEY not set in environment variables.")

# Initialize Scrapybara client
client = Scrapybara(api_key=SCRAPYBARA_API_KEY)


instance = client.start_ubuntu(
    timeout_hours=1,
)

cdp_url = instance.browser.start().cdp_url
playwright = sync_playwright().start()
browser = playwright.chromium.connect_over_cdp(cdp_url)

prompt = '''

'''

response = client.act(
    model=Anthropic(),
    tools=[
        BashTool(instance),
        ComputerTool(instance),
        EditTool(instance),
    ],
    system=UBUNTU_SYSTEM_PROMPT,
    prompt=f"{prompt}",
    on_step=lambda step: print(step.text),
)

print(response.result)

instance.stop()