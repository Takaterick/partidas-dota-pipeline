import pandas as pd
# esta es la api de opendota API_URI = "https://api.opendota.com/api/matches/8317181521"
def transformar_datos(raw_json):
    partida = raw_json
    partida.pop('players', None) # Eliminar los datos de jugadores porque es demasiado grande para que quede solo partidas ps
    df = pd.DataFrame([partida])
    return df

if __name__ == "__main__":
    from extraccion import extraer_datos
    raw = extraer_datos()
    df = transformar_datos(raw)
    print("Datos transformados con éxito.")