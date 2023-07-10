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
    with open(f'{current_time}_all_gets.csv', mode='w', newline='') as all_gets_file:
        all_gets_writer = csv.writer(all_gets_file)

        # Открываем первый файл и добавляем его содержимое в новый файл
        with open('wialon.csv', mode='r') as first_get_file:
            first_get_reader = csv.reader(first_get_file)
            all_gets_writer.writerows(first_get_reader)

        # Открываем второй файл и добавляем его содержимое в новый файл
        with open('fort.csv', mode='r') as second_get_file:
            second_get_reader = csv.reader(second_get_file)
            all_gets_writer.writerows(second_get_reader)

        # Открываем третий файл и добавляем его содержимое в новый файл
        with open('glonqssoft.csv', mode='r') as third_get_file:
            third_get_reader = csv.reader(third_get_file)
            all_gets_writer.writerows(third_get_reader)

        with open('scaut.csv', mode='r') as third_get_file:
            third_get_reader = csv.reader(third_get_file)
            all_gets_writer.writerows(third_get_reader)

        with open('era.csv', mode='r') as third_get_file:
            third_get_reader = csv.reader(third_get_file)
            all_gets_writer.writerows(third_get_reader)

        with open('wlocal.csv', mode='r') as third_get_file:
            third_get_reader = csv.reader(third_get_file)
            all_gets_writer.writerows(third_get_reader)

# Задаем время выполнения скрипта
schedule.every().day.at("02:40").do(job)
# Бесконечный цикл для выполнения заданий
while True:
    schedule.run_pending()
    time.sleep(1)
