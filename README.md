# Partidas de Dota Data Pipeline

Pipeline para extraer datos de partidas de dota 2 de una API pública, transformarlos y cargarlos en PostgreSQL.
Este proyecto implementa un pipeline de datos en Python que:

- Extrae datos de partidas de Dota 2 de una API pública.
- Transforma y guarda los datos en CSV.
- Carga los datos a una base de datos PostgreSQL.
- Permite consultar datos con SQL.

## Requisitos

- Python 3
- PostgreSQL (crear la base de datos obvis xd)
- Paquetes: `requests`, `pandas`, `sqlalchemy`, `psycopg2`

## Estructura

- `extraccion.py`: obtiene datos desde la API.
- `transformacion.py`: transforma el JSON en DataFrame.
- `carga.py`: guarda a CSV y carga en base de datos.
- `pipeline.py`: ejecuta todo el flujo ETL.
- `config.py`: parámetros del pipeline.

## Uso (aun por implementar xd)

```bash
python pipeline.py