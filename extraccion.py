import requests
from config import API_URI

def extraer_datos():
    response = requests.get(API_URI)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error al obtener datos: {response.status_code}")
    
if __name__ == "__main__":
    try:
        datos = extraer_datos()
        print("Datos extraídos con éxito.")
    except Exception as e:
        print(f"Error: {e}")