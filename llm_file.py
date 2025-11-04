import os
from dotenv import load_dotenv
from google import genai
from google.genai.errors import APIError

load_dotenv()

try:
    client = genai.Client   ()
except Exception as e:
    print("Erro ao inicializar o cliente Gemini. Verifique a chave GEMINI_API_KEY no seu .env.")
    print(f"Detalhes: {e}")
    exit()