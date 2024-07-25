from dotenv import load_dotenv
import os

load_dotenv()

SCOUT_TREE_LOGIN = os.getenv("17_SCOUT_365_LOGIN")
SCOUT_TREE_PASSWORD = os.getenv("17_SCOUT_365_PASSWORD")
SCOUT_TREE_URL = os.getenv("17_SCOUT_365_URL")
SCOUT_TREE_BASED_TOKEN = os.getenv("17_SCOUT_365_BASED_TOKEN")

