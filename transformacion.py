import pandas as pd
# esta es la api de opendota API_URI = "https://api.opendota.com/api/matches/8317181521"
def transformar_datos(raw_json):
    # Claves a eliminar para poder insertar bien en la tabla
    claves_considerar = [
        'match_id', 'start_time', 'duration', 'radiant_win', 'radiant_score',
        'dire_score', 'radiant_name', 'dire_name', 'radiant_team_id', 'dire_team_id', 'leagueid',
        'game_mode', 'lobby_type', 'human_players', 'cluster'
    ]
    
    partida = {clave: raw_json.get(clave) for clave in claves_considerar}

    df = pd.DataFrame([partida])
    return df

if __name__ == "__main__":
    from extraccion import extraer_datos
    raw = extraer_datos()
    df = transformar_datos(raw)
    print("Datos transformados con éxito.")