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

mkdir data_base_postgres

cd data_base_postgres

# Создание файла .env
touch .env

env_lines=(

    "POSTGRES_USER="
    "POSTGRES_DB_NAME="
    "POSTGRES_PASSWORD="
    "POSTGRES_PORT="
)
# Запись строк в файл .env
for line in "${env_lines[@]}"; do
    echo "$line" >> .env
done

echo "Файл .env создан успешно!"
nvim .env

cat > docker-compose.yaml << EOF
version: '3.8'
networks:
  postgres_db:
    driver: bridge

services:
  db:
    image: postgres
    environment:
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB_NAME} 
      ENCODING: 'UTF8'
      LC_COLLATE: 'C.UTF-8'
      LC_CTYPE: 'C.UTF-8'
    ports:
      - "${POSTGRES_PORT}:5432"
    command: postgres -c 'max_connections=300'
    volumes:
      - db_data:/var/lib/postgresql/data

    healthcheck:
      test: ["CMD", "pg_isready", "-U", "postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

    restart: always
    networks:
      - postgres_db

volumes:
  db_data
EOF
echo "Файл docker-compose.yaml создан успешно!"
sudo docker-compose --env-file .env up -d
echo "Сервер базы данных PostgreSQL успешно запущен!"
# вывести имя контейнера postgres
sudo docker ps
