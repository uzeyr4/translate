import requests


url = "http://127.0.0.1:8000/translate"


params = {
    "q": "Merhaba dünya",        # Çevrilecek metin
    "target": "en",              # Hedef dil
    "source": "tr"               # Kaynak dil
}

response = requests.get(url, params=params)

print(response.json())
