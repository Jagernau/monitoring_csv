from database import postgres_models as pgmodels

from database.bd_conectors import PostgresDatabase as pgdb

import datetime

from sqlalchemy import func, Date, cast, and_

from datetime import date

import sys
sys.path.append('../')
from monitoring_csv import my_logger

def get_last_pg_id_database():
    session = pgdb().session
    data = session.query(pgmodels.Tdata.id).order_by(pgmodels.Tdata.id.desc()).first()
    session.close()
    return data


def add_objects(marge_data: list):
    
    current_date = datetime.datetime.now()
    current_month = current_date.month
    current_day = current_date.day
    current_year = current_date.year

    today = f"{current_month}.{current_day}.{current_year} 1:40"
    session = pgdb().session
    
    # Проверяем существование записей за сегодняшнюю дату
    existing = session.query(pgmodels.Tdata).filter(
        pgmodels.Tdata.dimport == today,
        pgmodels.Tdata.idsystem == marge_data[0][2]
    ).first()
    
    if existing:
        my_logger.logger.info(f"Данные за {today} уже загружены, образец {existing}, пропускаем добавление")
        session.close()
        return
    
    full_dimport = today  # Используем текущую дату и время
    
    for i in marge_data:
        objects_data = pgmodels.Tdata(
            login=i[0],
            idlogin=i[1],
            idsystem=i[2],
            object=i[3],
            idobject=i[4],
            isactive=i[5],
            dimport=full_dimport
        )
        session.add(objects_data)

    # print(today, marge_data[0][2])
    session.commit()
    session.close()
    my_logger.logger.info(f"Успешно добавлено {len(marge_data)} записей за {today}, образец {existing}")


# def add_objects(marge_data: list):
#     current_date = datetime.datetime.now()
#     current_month = current_date.month
#     current_day = current_date.day
#     current_year = current_date.year
#     #last_id = int(get_last_pg_id_database()[0])
#     session = pgdb().session
#     for i in marge_data:
#         #last_id += 1
#             
#         objects_data = pgmodels.Tdata(
#                 #id = last_id,
#                 login = i[0],
#                 idlogin = i[1],
#                 idsystem = i[2],
#                 object = i[3],
#                 idobject = i[4],
#                 isactive = i[5],
#                 dimport = f"{current_month}.{current_day}.{current_year} 1:40"
#                 )
#         session.add(objects_data)
#     session.commit()
#     session.close()

