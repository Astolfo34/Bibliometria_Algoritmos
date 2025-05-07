import requests


#   Funcion para la indexacion de metadatos al usar la base de datos
#   de scopus: para extracion de datos como autor, titulo, resumen, etc.

def fetch_scopus_data(query):
    API_KEY = "TU_CLAVE_SCOPUS"
    url = "https://api.elsevier.com/content/search/scopus"

    params = {
        "query": query,
        "apiKey": API_KEY,
        "httpAccept": "application/json"
    }

    response = requests.get(url, params=params)
    return response.json()["search-results"]["entry"]

# Uso: results = fetch_scopus_data("computational thinking")