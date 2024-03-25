from dotenv import dotenv_values

config = dotenv_values(".env")

# Глонасс
GLONASS_HOST=config.get('GLONASS_HOST')
GLONASS_LOGIN=config.get('GLONASS_LOGIN')
GLONASS_PASSWORD=config.get('GLONASS_PASSWORD')

# Форт
FORT_HOST=config.get('FORT_HOST')
FORT_LOGIN=config.get('FORT_LOGIN')
FORT_PASSWORD=config.get('FORT_PASSWORD')

# Wialon
WIALON_HOST=config.get('WIALON_HOST')
WIALON_TOKEN=config.get('WIALON_TOKEN')

# Wialon local
WIALON_LOCAL_HOST=config.get('WIALON_LOCAL_HOST')
WIALON_LOCAL_TOKEN=config.get('WIALON_LOCAL_TOKEN')

# Scout
SCAUT_HOST=config.get('SCAUT_HOST') # с портом
SCAUT_LOGIN=config.get('SCAUT_LOGIN')
SCAUT_PASSWORD=config.get('SCAUT_PASSWORD')

# Era
ERA_HOST=config.get('ERA_HOST')
ERA_LOGIN=config.get('ERA_LOGIN')
ERA_PASSWORD=config.get('ERA_PASSWORD')

# Database
DB_HOST=config.get('DB_HOST')

# Postgres
POSTGRES_USER=config.get('POSTGRES_USER')
POSTGRES_DB_NAME=config.get('POSTGRES_DB_NAME')
POSTGRES_PASSWORD=config.get('POSTGRES_PASSWORD')
POSTGRES_PORT=config.get('POSTGRES_PORT')

# MySQL
MYSQL_USER=config.get('MYSQL_USER')
MYSQL_DB_NAME=config.get('MYSQL_DB_NAME')
MYSQL_PASSWORD=config.get('MYSQL_PASSWORD')
MYSQL_PORT=config.get('MYSQL_PORT')

DISK_TOKEN = config.get('DISK_TOKEN')

connection_postgres = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOST}:{POSTGRES_PORT}/{POSTGRES_DB_NAME}"

connection_mysql = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{DB_HOST}:{MYSQL_PORT}/{MYSQL_DB_NAME}"
time_active = config['TIME_ACTIVE']
