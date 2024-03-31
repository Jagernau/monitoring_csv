from typing import Final

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import sys
sys.path.append('../')
from monitoring_db_autosave import config


class PostgresDatabase: 
    BASE: Final = declarative_base()

    def __init__(self):
        self.__engine = create_engine(str(config.connection_postgres))
        session = sessionmaker(autocommit=False, autoflush=False, bind=self.__engine)
        self.__session = session()

    @property 
    def session(self): 
        return self.__session

    @property
    def engine(self): 
        return self.__engine
