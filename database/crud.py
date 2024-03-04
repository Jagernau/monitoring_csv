from collections.abc import ItemsView

from sqlalchemy.util import EMPTY_DICT

import postgres_models as pgmodels
import mysql_models as mysqlmodels

from bd_conectors import PostgresDatabase as pgdb
from bd_conectors import MysqlDatabase as mysqldb

import datetime

def get_last_pg_id_database():
    session = pgdb().session
    data = session.query(pgmodels.Tdata.id).order_by(pgmodels.Tdata.id.desc()).first()
    session.close()
    return data

print(get_last_pg_id_database())

def add_objects(marge_data: list):
    current_date = datetime.datetime.now()
    current_month = current_date.month
    current_day = current_date.day
    current_year = current_date.year
    last_id = int(get_last_pg_id_database()[0])
    session = pgdb().session
    for i in marge_data:
        objects_data = pgmodels.Tdata(
                login = i[0],
                idlogin = i[1],
                idsystem = i[2],
                object = i[3],
                idobject = i[4],
                isactive = i[5],
                id = last_id + 1,
                dimport = f"{current_day}.{current_month}.{current_year} 1:40"
                )
        session.add(objects_data)
    session.commit()
    session.close()
