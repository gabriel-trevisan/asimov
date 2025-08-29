from transformers import pipeline
import os 
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

modelo = pipeline('text-generation', model='google/gemma-7b-it', token=token)

print(modelo)