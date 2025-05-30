# translate_api.py
from fastapi import FastAPI, Query
import requests

from pydantic import BaseModel

app = FastAPI()

API_KEY = Api_key

@app.get("/")
def home():
    return "hello"

class TranslateRequest(BaseModel):
    text: str
    target: str = "en"
    source: str = "tr"

@app.post("/translate")
def translate_text(request_data: TranslateRequest):
    url = "https://translation.googleapis.com/language/translate/v2"
    params = {
        "q": request_data.text,
        "target": request_data.target,
        "source": request_data.source,
        "key": API_KEY
    }
    response = requests.post(url, params=params)
    result = response.json()

    # Hata kontrolü
    if "data" in result:
        return {"translated": result['data']['translations'][0]['translatedText']}
    else:
        return {"error": result.get("error", "Bilinmeyen hata")}
