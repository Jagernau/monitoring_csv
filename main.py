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

def job():

    wialon = WialonData()
    wialon.dict_to_csv()
    
    time.sleep(60)

    fort = FortData()
    fort.list_to_csv()

    time.sleep(60)

    glanass = GlanassData()
    glanass.list_to_csv()

    time.sleep(60)

    scaut = ScautData()
    scaut.list_to_csv()

    time.sleep(60)

    era = EraData()
    era.list_to_csv()

    time.sleep(60)

    wlocal = WlocalData()
    wlocal.dict_to_csv()

    time.sleep(60)

    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

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

# Задаем время выполнения скрипта
schedule.every().day.at("01:26").do(job)
# Бесконечный цикл для выполнения заданий
while True:
    schedule.run_pending()
    time.sleep(1)
