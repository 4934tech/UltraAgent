import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOVEE_API_KEY = os.getenv("GOVEE_API_KEY")
