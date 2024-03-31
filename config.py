from os import environ as envi

# Глонасс
GLONASS_HOST=envi.get('GLONASS_HOST')
GLONASS_LOGIN=envi.get('GLONASS_LOGIN')
GLONASS_PASSWORD=envi.get('GLONASS_PASSWORD')

# Форт
FORT_HOST=envi.get('FORT_HOST')
FORT_LOGIN=envi.get('FORT_LOGIN')
FORT_PASSWORD=envi.get('FORT_PASSWORD')

# Wialon
WIALON_HOST=envi.get('WIALON_HOST')
WIALON_TOKEN=envi.get('WIALON_TOKEN')

# Wialon local
WIALON_LOCAL_HOST=envi.get('WIALON_LOCAL_HOST')
WIALON_LOCAL_TOKEN=envi.get('WIALON_LOCAL_TOKEN')

# Scout
SCAUT_HOST=envi.get('SCAUT_HOST')
SCAUT_LOGIN=envi.get('SCAUT_LOGIN')
SCAUT_PASSWORD=envi.get('SCAUT_PASSWORD')

# Era
ERA_HOST=envi.get('ERA_HOST')
ERA_LOGIN=envi.get('ERA_LOGIN')
ERA_PASSWORD=envi.get('ERA_PASSWORD')

# Database
DB_HOST=envi.get('DB_HOST')

# Postgres
POSTGRES_USER=envi.get('POSTGRES_USER')
POSTGRES_DB_NAME=envi.get('POSTGRES_DB_NAME')
POSTGRES_PASSWORD=envi.get('POSTGRES_PASSWORD')
POSTGRES_PORT=envi.get('POSTGRES_PORT')

# Yandex Disk
DISK_TOKEN=envi.get.get('DISK_TOKEN')

# Time active
TIME_ACTIVE=envi.get.get('TIME_ACTIVE')

connection_postgres = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOST}:{POSTGRES_PORT}/{POSTGRES_DB_NAME}"

