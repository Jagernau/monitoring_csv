import csv
import datetime
import schedule
import time

from mwln import WialonData
from mfrt import FortData
from mgls import GlanassData
from mspic import ScautData
from mera import EraData
from mwlnl import WlocalData
from send_to_yandex import send_csv_to_yandex
from my_logger import logger


def job():
    try:
        wialon = WialonData()
        wialon.dict_to_csv()
        logger.info("Wialon успешно обновлен")
    except Exception as e:
        logger.error(f"В обновлении Wialon возникла ошибка: {e}")

    time.sleep(30)

    try:
        fort = FortData()
        fort.list_to_csv()
        logger.info("ФОРТ успешно обновлен")
    except Exception as e:
        logger.error(f"В обновлении ФОРТ возникла ошибка: {e}")

    time.sleep(30)

    try:
        glanass = GlanassData()
        glanass.list_to_csv()
        logger.info("Глонасссофт успешно обновлен")
    except Exception as e:
        logger.error(f"В обновлении Глонасссофтов возникла ошибка: {e}")

    time.sleep(30)

    try:
        scaut = ScautData()
        scaut.list_to_csv()
        logger.info("СКАУТ успешно обновлен")
    except Exception as e:
        logger.error(f"В обновлении СКАУТ возникла ошибка: {e}")

    time.sleep(30)

    try:
        era = EraData()
        era.list_to_csv()
        logger.info("Era успешно обновлен")
    except Exception as e:
        logger.error(f"В обновлении Era возникла ошибка: {e}")

    time.sleep(30)

    try:
        wlocal = WlocalData()
        wlocal.dict_to_csv()
        logger.info("Wlocal успешно обновлен")
    except Exception as e:
        logger.error(f"В обновлении Wlocal возникла ошибка: {e}")

    time.sleep(30)

    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    try:
    # Открываем новый файл для записи
        with open(f'{current_time}_all_gets.csv', mode='w', newline='', encoding='utf-8') as all_gets_file:
            all_gets_writer = csv.writer(all_gets_file)

            # Открываем первый файл и добавляем его содержимое в новый файл
            with open('wialon.csv', mode='r', encoding='utf-8') as first_get_file:
                first_get_reader = csv.reader(first_get_file)
                all_gets_writer.writerows(first_get_reader)

            # Открываем второй файл и добавляем его содержимое в новый файл
            with open('fort.csv', mode='r', encoding='utf-8') as second_get_file:
                second_get_reader = csv.reader(second_get_file)
                next(second_get_reader)
                all_gets_writer.writerows(second_get_reader)

            # Открываем третий файл и добавляем его содержимое в новый файл
            with open('glonqssoft.csv', mode='r', encoding='utf-8') as third_get_file:
                third_get_reader = csv.reader(third_get_file)
                next(third_get_reader)
                all_gets_writer.writerows(third_get_reader)

            with open('scaut.csv', mode='r', encoding='utf-8') as for_get_file:
                for_get_reader = csv.reader(for_get_file)
                next(for_get_reader)
                all_gets_writer.writerows(for_get_reader)

            with open('era.csv', mode='r', encoding='utf-8') as five_get_file:
                five_get_reader = csv.reader(five_get_file)
                next(five_get_reader)
                all_gets_writer.writerows(five_get_reader)

            with open('wlocal.csv', mode='r', encoding='utf-8') as six_get_file:
                six_get_reader = csv.reader(six_get_file)
                next(six_get_reader)
                all_gets_writer.writerows(six_get_reader)

        logger.info("Все данные успешно обновлены и записаны в csv")
    except Exception as e:
        logger.error(f"В обновлении данных возникла и запись в csv возникла ошибка: {e}")

    time.sleep(30)

    try:
        send_csv_to_yandex(f"{current_time}_all_gets.csv")
        logger.info("Все данные успешно отправлены на Яндекс.Диск")
    except Exception as e:
        logger.error(f"В отправке данных возникла ошибка: {e}")


# Задаем время выполнения скрипта
schedule.every().day.at("00:20").do(job)
# Бесконечный цикл для выполнения заданий
while True:
    schedule.run_pending()
    time.sleep(1)

