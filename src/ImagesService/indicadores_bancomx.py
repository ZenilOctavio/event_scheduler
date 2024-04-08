import requests

def get_services():
    url = 'http://web_image:8000/services/'
    response = requests.get(url)
    return response.json()

def get_indicadores_bamx() -> bytes:
    url = 'http://web_image:8000/services/get_image/indicadores_bancomx'
    response = requests.put(url, json={
        "context": {}
    })
    
    return response.content