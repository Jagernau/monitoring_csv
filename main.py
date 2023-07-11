import csv
import datetime
import schedule
import time


def job():
    import mwln
    import mfrt
    import mgls
    import mspic
    import mera
    import mwlnl

    wialon = mwln.WialonData()
    wialon.dict_to_csv()
    
    time.sleep(60)

    fort = mfrt.FortData()
    fort.list_to_csv()

    time.sleep(60)

    glanass = mgls.GlanassData()
    glanass.list_to_csv()

    time.sleep(60)

    scaut = mspic.ScautData()
    scaut.list_to_csv()

    time.sleep(60)

    era = mera.EraData()
    era.list_to_csv()

    time.sleep(60)

    wlocal = mwlnl.WlocalData()
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
            all_gets_writer.writerows(second_get_reader)

        # Открываем третий файл и добавляем его содержимое в новый файл
        with open('glonqssoft.csv', mode='r', encoding='utf-8') as third_get_file:
            third_get_reader = csv.reader(third_get_file)
            all_gets_writer.writerows(third_get_reader)

        with open('scaut.csv', mode='r', encoding='utf-8') as third_get_file:
            third_get_reader = csv.reader(third_get_file)
            all_gets_writer.writerows(third_get_reader)

        with open('era.csv', mode='r', encoding='utf-8') as third_get_file:
            third_get_reader = csv.reader(third_get_file)
            all_gets_writer.writerows(third_get_reader)

        with open('wlocal.csv', mode='r', encoding='utf-8') as third_get_file:
            third_get_reader = csv.reader(third_get_file)
            all_gets_writer.writerows(third_get_reader)

# Задаем время выполнения скрипта
schedule.every().day.at("02:40").do(job)
# Бесконечный цикл для выполнения заданий
while True:
    schedule.run_pending()
    time.sleep(1)
