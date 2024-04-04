from postgres_models import *
from bd_conectors import  PostgresDatabase as pgdb

postgres_db = pgdb()

postgres_db.BASE.metadata.create_all(postgres_db.engine)

postgres_db.session.commit()
