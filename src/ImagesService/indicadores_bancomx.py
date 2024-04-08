import requests

def get_indicadores_bamx() -> bytes:
    url = 'http://172.17.0.4:8000/services/get_image/indicadores_bancomx'
    response = requests.put(url, json={
        "context": {}
    })
    
    return response.content