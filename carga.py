from sqlalchemy import create_engine
from config import DB_URI, CSV_PATH

def cargar_datos_csv(df):
    df.to_csv(CSV_PATH, index=False)

def cargar_datos_db(df):
    engine = create_engine(DB_URI)
    df.to_sql('partidas', con=engine, if_exists='replace', index=False)

if __name__ == "__main__":
    import pandas as pd
    from transformacion import transformar_datos
    from extraccion import extraer_datos

    try:
        raw_data = extraer_datos()
        df = transformar_datos(raw_data)
        cargar_datos_csv(df)
        cargar_datos_db(df)
        print("Datos cargados con éxito.")
    except Exception as e:
        print(f"Error al cargar los datos: {e}")