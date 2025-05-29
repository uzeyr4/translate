# translate_api.py
from fastapi import FastAPI, Query
import requests
from apikey import Api_key 

app = FastAPI()

API_KEY = Api_key

@app.get("/")
def home():
    return "hello"

@app.get("/translate")
def translate_text(q: str = Query(...), target: str = "en", source: str = "tr"):
    url = f"https://translation.googleapis.com/language/translate/v2"
    params = {
        "q": q,
        "target": target,
        "source": source,
        "key": API_KEY
    }
    response = requests.post(url, params=params)
    return response.json()
