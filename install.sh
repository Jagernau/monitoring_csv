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
git clone https://github.com/Jagernau/monitoring_csv -b auto_create monitoring_db_autosave

cd monitoring_db_autosave

# Создание файла .env
touch .env

# Функция для проверки логина и пароля Glonasssoft
check_glonass_credentials() {
    local login=$1
    local password=$2
    local auth_id=$(curl -s -X POST -H "Content-Type: application/json" -d "{\"login\": \"$login\", \"password\": \"$password\"}" https://hosting.glonasssoft.ru/api/v3/auth/login | jq -r '.AuthId')

    if [ -n "$auth_id" ]; then
        echo "Логин и Пароль для Glonasssoft верны."
        # Запись Логина и Пароля в файл .env
        echo "GLONASS_LOGIN=$login" >> .env
        echo "GLONASS_PASSWORD=$password" >> .env
    else
        echo "Логин или Пароль для Glonasssoft неверны."
        read -p "Введите Логин для Glonasssoft: " new_login
        read -p "Введите Пароль для Glonasssoft: " new_password
        check_glonass_credentials $new_login $new_password
    fi
}

# Проверка подключения Glonasssoft
read -p "Подключить Glonasssoft? (y/n): " glonass_choice
if [ "$glonass_choice" == "y" ] || [ "$glonass_choice" == "Y" ]; then
    read -p "Введите Логин для Glonasssoft: " glonass_login
    read -p "Введите Пароль для Glonasssoft: " glonass_password

    check_glonass_credentials $glonass_login $glonass_password
fi
