#!/bin/bash


if command -v docker &> /dev/null
then
    echo "Docker уже установлен."
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
            echo "Установка Docker не удалась."
        fi
    else
        echo "Установка Docker отменена."
    fi
fi
