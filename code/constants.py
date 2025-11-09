import dotenv
import os

dotenv.load_dotenv("../env_workshop")

OPENAI_BASE_URL = os.environ.get("OPENAI_BASE_URL")
PHOENIX_PROJECT_NAME = os.environ.get("PHOENIX_PROJECT_NAME")
TAVILY_BASE_URL = os.environ.get("TAVILY_BASE_URL")