from os import environ as envi

# Database
DB_HOST=envi.get('DB_HOST')

# Postgres
POSTGRES_USER=envi.get('POSTGRES_USER')
POSTGRES_DB_NAME=envi.get('POSTGRES_DB_NAME')
POSTGRES_PASSWORD=envi.get('POSTGRES_PASSWORD')
POSTGRES_PORT=5432

connection_postgres = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOST}:{POSTGRES_PORT}/{POSTGRES_DB_NAME}"
