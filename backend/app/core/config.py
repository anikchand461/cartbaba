import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME = "CartBaba"
    DEBUG = True

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

settings = Settings()
