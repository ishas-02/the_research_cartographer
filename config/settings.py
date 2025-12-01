import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()  # loads .env file

def init_gemini():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("❌ GOOGLE_API_KEY missing. Add it in .env")
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("gemini-2.0-flash")

model = init_gemini()
