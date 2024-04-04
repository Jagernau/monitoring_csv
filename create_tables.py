# from postgres_models import *
# from bd_conectors import  PostgresDatabase as pgdb
#
# postgres_db = pgdb()
#
# postgres_db.BASE.metadata.create_all(postgres_db.engine)
#

import config

print(f"---{config.DB_HOST}---")
print(f"---{config.POSTGRES_USER}---")
print(f"---{config.POSTGRES_DB_NAME}---")
print(f"---{config.POSTGRES_PASSWORD}---")

