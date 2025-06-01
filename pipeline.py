from extraccion import extraer_datos
from transformacion import transformar_datos
from carga import cargar_datos_csv, cargar_datos_db

def pipeline():
    print("Iniciando el pipeline de ETL...")

    print("1. Extrayendo datos...")
    raw_data = extraer_datos()

    print("2. Transformando datos...")
    df = transformar_datos(raw_data)

    print("3. Cargando datos a CSV...")
    cargar_datos_csv(df)

    print("4. Cargando datos a la base de datos...")
    cargar_datos_db(df)

    print("Pipeline de ETL completado con exito.")

if __name__ == "__main__":
    try:
        pipeline()
    except Exception as e:
        print(f"Error en el pipeline: {e}")