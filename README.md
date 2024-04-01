# Программа для получения данных из систем мониторинга
# Версия 1.3

Программа получает данные об объектах из систем мониторинга, таких как:
1. Gsoft
2. Fort
3. Scout
4. Whosting
5. Wlocal
6. Era
## Формирует csv фаил с колонками:
1. Имя учётки
2. Id учётки
3. Id системы мониторинга
4. Имя объекта
5. Id объекта
6. Активность(применима только к Wlocal, Whosting)

Такой файл перед заливкой в БД нужно обработать с помощью Excel, а именно проставление pk, даты и времени выгрузки.

## Как получить токен от яндекс диска
Найти в интернете по запросу: yandex disk python.
Это не сложно. Нужно создать приложение яндекс. И получить токен.
## Как получить токены от Wialon-ов
https://Адрес виалона хостинга либо локала/login.html?client_id=wialon&access_type=-1&activation_time=0&duration=0
* access_type=-1 - уровень доступа, -1 доступ ко всему
* activation_time=0 - время активации, 0 прямо сейчас
* duration=0 - время действия, 0 бесконечный
после ввода в форму, и регистрации, в строке с url будет выведен токен.

## Как запустить Базу данных на postgres в контейнере docker-compose
### Это контейнер подходящий БД подходящий под программу собирания данных
Если понадобится создать базу данных Postgres и в ней создать таблицы с нужными названиями
1. Запустить скрипт `curl -s https://raw.githubusercontent.com/Jagernau/monitoring_csv/simple_data_collector/data_base_postgres_install.sh`




## Как установить программу по сбору данных.
### Установка только собирателя данных, и только с отправкой на Яндекс Диск сгенерированного csv, без записи в БД
Чисто собиратель данных, будет собирать данные с систем мониторинга, этот скрипт применять если уже СУЩЕСТВУЮЕТ БД с нужными таблицами на postgres и отcылать данные за день на yandex Диск.
1. Запустить скрипт `curl -s https://raw.githubusercontent.com/Jagernau/monitoring_csv/simple_data_collector/simple_data_collector_install.sh | sh`
* Пройдёт проверка установлен ли docker.
* Пройдёт проверка установлен ли docker-compose.
* Если нет, то установится.
* Нужно будет прописать пароли в открывшемся автоматическом окне .env

    "WIALON_HOST=hst-api.wialon.com" # по умолчанию
    "WIALON_TOKEN="
    "FORT_HOST=" # с http
    "FORT_LOGIN="
    "FORT_PASSWORD="
    "GLONASS_HOST=https://hosting.glonasssoft.ru" # по умолчанию
    "GLONASS_LOGIN="
    "GLONASS_PASSWORD="
    "SCAUT_HOST=" #c http и портом
    "SCAUT_LOGIN="
    "SCAUT_PASSWORD="
    "ERA_HOST=monitoring.aoglonass.ru" # по умолчанию
    "ERA_LOGIN="
    "ERA_PASSWORD="
    "WIALON_LOCAL_HOST=" # свой или наш, написание без http и порта
    "WIALON_LOCAL_TOKEN="
    "DISK_TOKEN="
    "DB_HOST=" # хостинг базы данных для локального подключения localhost или внутренний ip
    "POSTGRES_USER=" # имя пользователя
    "POSTGRES_DB_NAME=" # название базы данных
    "POSTGRES_PASSWORD=" # пароль базы данных
    "POSTGRES_PORT=" # порт базы данных
    "TIME_ACTIVE=" # типа 10:00

* Скачается контейнер собирателя данных с отправкой на Яндекс Диск csv
* Запускается скрипт, который получает данные и записывает в Яндекс Диск csv, название директории в Яндекс диске 'simple_data_collector'


