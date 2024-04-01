#!/bin/bash

# Зеленая подсветка текста
GREEN='\033[0;32m'
# Красная подсветка текста
RED='\033[0;31m'
# Белая подсветка текста
NC='\033[0m'


# Зеленая подсветка текста
echo "${GREEN}Запуск установки...${NC}"
#
# Проверка наличия Docker
if command -v docker &> /dev/null
then
    echo "${GREEN}Docker уже установлен.${NC}"
    docker --version
else
    read -p "Docker не установлен. Хотите установить Docker? (y/n): " choice
    if [ "$choice" == "y" ] || [ "$choice" == "Y" ]; then
        # Установка Docker
        sudo apt update
        sudo apt install -y apt-transport-https ca-certificates curl software-properties-common

        # Добавление ключа GPG официального репозитория Docker
        curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

        # Добавление репозитория Docker в список источников пакетов APT
        sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

        # Установка Docker
        sudo apt update
        sudo apt install -y docker-ce

        # Добавление текущего пользователя в группу docker для запуска Docker без sudo
        sudo usermod -aG docker $USER

        # Перезапуск сервиса Docker
        sudo systemctl restart docker

        # Проверка успешной установки Docker и вывод версии
        if command -v docker &> /dev/null
        then
            echo "Docker успешно установлен."
            docker --version
        else
            echo "${RED}Установка Docker не удалась.${NC}"
        fi
    else
        echo "${RED}Установка Docker отменена.${NC}"
        # Выход из скрипта
        exit 1
    fi
fi

# Check if Docker Compose is installed
if command -v docker-compose &> /dev/null
then
    echo "${GREEN}Docker Compose уже установлен.${NC}"
    docker-compose --version
else
    read -p "Docker Compose не установлен. Хотите установить Docker Compose? (y/n): " choice
    if [ "$choice" == "y" ] || [ "$choice" == "Y" ]; then
        # Install Docker Compose
        # Установка Docker Compose
        sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

        # Делаем установленный файл исполняемым
        sudo chmod +x /usr/local/bin/docker-compose

        # Создаем символическую ссылку на исполняемый файл
        sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

        # Check successful Docker Compose installation and display version
        if command -v docker-compose &> /dev/null
        then
            echo "Docker Compose успешно установлен."
            docker-compose --version
        else
            echo "Установка Docker Compose не удалась."
        fi
    else
        echo "Тогда не получится запустить программу"
        exit 1
    fi
fi

echo "${GREEN}Первичная установка завершена${NC}"

mkdir simple_data_collector

cd simple_data_collector

# Создание файла .env
touch .env

env_lines=(

    "WIALON_HOST=hst-api.wialon.com" # по умолчанию
    "WIALON_TOKEN="
    "FORT_HOST="
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
    "DB_HOST=" # хостинг базы данных
    "POSTGRES_USER="
    "POSTGRES_DB_NAME="
    "POSTGRES_PASSWORD="
    "POSTGRES_PORT="
    "TIME_ACTIVE=" # типа 10:00
)
# Запись строк в файл .env
for line in "${env_lines[@]}"; do
    echo "$line" >> .env
done

echo "Файл .env создан успешно!"
nvim .env

