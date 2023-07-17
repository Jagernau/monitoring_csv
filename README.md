# Программа для получения данных из систем мониторинга
# Версия 0.1

Программа получает данные об объектах из систем мониторинга, таких как:
1. Gsoft
2. Fort
3. Scout
4. Whosting
5. Wlocal
6. Era
Формирует csv фаилс колонками:
1. Имя учётки
2. Id учётки
3. Id системы мониторинга
4. Имя объекта
5. Id объекта
6. Активность(применима только к Wlocal, Whosting)

Такой файл обрабатывается с помощью Excel, а именно проставление pk, даты и времени выгрузки.

## Как установить.
скачать репо:`git clone https://github.com/Jagernau/monitoring_csv`
войти в папку с репо: `cd monitoring_csv.py`
создать окружение: `python -m virtualenv env`
войти в окружение: `source env/bin/activate`
установить пакеты: `pip install -r requirements.txt`
создать файл .env с паролями:
```
11_CID=
11_TOKEN=
12_LOGIN=
12_PASSWORD=
13_LOGIN=
13_PASSWORD=
14_URL=
14_LOGIN=
14_PASSWORD=
15_PORT=
15_LOGIN=
15_PASSWORD=
16_CID=
16_TOKEN=
```
Запустить: `python main.py`

Можно запускать выгрузку из каждой системы по отдельности.
Файлами с названием системы мониторинга.
