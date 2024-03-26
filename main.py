import csv
import datetime
import schedule
import time

from mwln import WialonData
from mfrt import FortData
from mgls import GlonassData
from mspic import ScautData
from mera import EraData
from mwlnl import WlocalData
from send_to_yandex import send_csv_to_yandex
from my_logger import logger
import config

monitoring_systems = {
#    "wialon": WialonData,
    "fort": FortData,
    "glonqssoft": GlonassData,
#    "scaut": ScautData,
#   "era": EraData,
#    "wlocal": WlocalData,
}

def systems_query():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    accepted_data = []
    for i in monitoring_systems:
        try:
            monitoring_system = monitoring_systems[i]()
            data = monitoring_system.get_data()
        except Exception as e:
            logger.error(f"Ошибка при получении данных {i}: {e}")
        else:
            logger.info(f"Данные {i} получены.")
            try:
                monitoring_system.data_to_csv(data)
            except Exception as e:
                logger.error(f"Ошибка при записи данных в файл {i}: {e}")
            else:
                logger.info(f"Данные {i} записаны в файл.")
                accepted_data.append(i)
            try:
                monitoring_system.add_to_db(data)
            except Exception as e:
                logger.error(f"Ошибка при добавлении данных {i} в базу: {e}")
            else:
                logger.info(f"Данные {i} добавлены в базу.")


    with open(f'{current_time}_all_gets_autosave.csv', mode='w', newline='', encoding='utf-8') as f:
        all_gets_writer = csv.writer(f)

        # Iterate over the file list and process each file
        for filename in accepted_data:
            try:
                with open(f'{filename}.csv', mode='r', encoding='utf-8') as file:
                    reader = csv.reader(file)
                    next(reader)  # Skip the header row
                    all_gets_writer.writerows(reader)
                    logger.info(f"Файл {filename} обработан.")
            except FileNotFoundError:
                logger.error(f"Файл {filename} не существует.")
            except Exception as e:
                logger.error(f"Ошибка при обработке {filename}: {e}.")

