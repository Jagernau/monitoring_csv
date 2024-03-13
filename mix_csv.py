import csv
import datetime


current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Открываем новый файл для записи
with open(f'{current_time}_all_gets_autosave.csv', mode='w', newline='', encoding='utf-8') as all_gets_file:
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

