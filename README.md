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
11_CID="" # оставим пустым
11_TOKEN= <токен> Whosting
12_LOGIN= <логин> Fort
12_PASSWORD= <пароль> Fort
13_LOGIN= <логин> Gsoft
13_PASSWORD= <пароль> Gsoft
14_URL= <адрес> Скаут
14_LOGIN= <логин> Скаут
14_PASSWORD= <пароль> Скаут
15_PORT= <порт> Era
15_LOGIN= <логин> Era
15_PASSWORD= <пароль> Era
16_CID="" # оставим пустым
16_TOKEN= <токен> Wlocal

DISK_TOKEN= <токен> YandexDisk

17_SCOUT_365_LOGIN= <логин> Scout_365
17_SCOUT_365_PASSWORD= <пароль> Scout_365
17_SCOUT_365_URL= <адрес> Scout_365
17_SCOUT_365_BASED_TOKEN= <базовый токен, искать в документах> Scout_365
```
Запустить: `python main.py`

Можно запускать выгрузку из каждой системы по отдельности.
Файлами с названием системы мониторинга.
