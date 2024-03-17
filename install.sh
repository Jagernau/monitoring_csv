#!/bin/bash

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color


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
    fi
fi
