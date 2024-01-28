from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# set the API key
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")