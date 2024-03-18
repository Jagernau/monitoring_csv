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
        curl -fsSL https://get.docker.com -o get-docker.sh
        sudo sh get-docker.sh

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
        sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
        sudo chmod +x /usr/local/bin/docker-compose

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
git clone https://github.com/Jagernau/monitoring_csv -b auto_create monitoring_db_autosave && wait

cd monitoring_db_autosave

# Создание файла .env
touch .env

# Проверка подключения Glonasssoft
read -p "Подключить Glonasssoft? (y/n): " glonass_choice
if [ "$glonass_choice" = "y" ] || [ "$glonass_choice" = "Y" ]; then
    read -p "Введите Логин для Glonasssoft: " glonass_login
    read -p "Введите Пароль для Glonasssoft: " glonass_password
fi
