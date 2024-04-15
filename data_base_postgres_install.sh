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

curl -LJO https://raw.githubusercontent.com/jagernau/monitoring_csv/simple_data_collector/pgschema_bd.sql
# Создание файла .env
cat > .env << EOF
POSTGRES_USER=
POSTGRES_DB_NAME=
POSTGRES_PASSWORD=
POSTGRES_PORT=
EOF

#!/bin/bash

# Проверка установки Neovim и вывод версии
if command -v nvim &> /dev/null
then
    echo "Neovim установлен. Версия:"
    nvim --version | head -n 1
else
    echo "Neovim не установлен. Установка..."
    
    # Установка Neovim на Ubuntu и Debian
    if command -v apt &> /dev/null
    then
        sudo apt update
        sudo apt install neovim
    fi

    # Установка Neovim на Manjaro и Arch Linux
    if command -v pacman &> /dev/null
    then
        sudo pacman -Syu neovim
    fi

    # Установка Neovim на Fedora
    if command -v dnf &> /dev/null
    then
        sudo dnf install -y neovim
    fi

    # Установка Neovim через Flatpak
    flatpak install flathub io.neovim.nvim

    # Установка Neovim через Snap
    sudo snap install nvim --classic

    echo "Neovim успешно установлен."
fi

nvim .env

cat > docker-compose.yaml << 'EOF'
version: '3.9'
networks:
  suntel_network:
    driver: bridge

services:
  db:
    image: postgres:latest
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
      test: ["CMD", "pg_isready", "-U", "${POSTGRES_USER}", "-d", "${POSTGRES_DB_NAME}", "-h", "localhost"]
      interval: 5s
      timeout: 5s
      retries: 5
    restart: always
    networks:
      - suntel_network

  # pgadmin:
  #   image: dpage/pgadmin4:latest
  #   restart: always
  #   environment:
  #     PGADMIN_DEFAULT_EMAIL: ${POSTGRES_USER}@mail.com
  #     PGADMIN_DEFAULT_PASSWORD: ${POSTGRES_PASSWORD}
  #   ports:
  #     - "5010:80"

  web:
    image: jagernau/rest_suntel:latest
    environment:
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB_NAME: ${POSTGRES_DB_NAME}
      POSTGRES_PORT: 5432
      POSTGRES_HOST: db
    depends_on:
      db:
        condition: service_healthy
    command: >
      sh -c "python manage.py runserver 0.0.0.0:8000"
    networks:
      - suntel_network
    ports:
      - 8000:8000

volumes:
  db_data:
EOF

echo "Файл docker-compose.yaml создан успешно!"
sudo docker-compose --env-file .env up -d
echo "${GREEN}Сервер базы данных PostgreSQL успешно запущен!${NC}"


sudo docker cp pgschema_bd.sql db:/home/pgschema_bd.sql
sleep 5
sudo docker exec -i data_base_postgres_db_1 psql -U max -d max -f /home/pgschema_bd.sql

sudo docker-compose --env-file .env exec web python manage.py migrate

source .env
docker-compose exec -T web python manage.py createsuperuser --noinput --email "${POSTGRES_USER}@mail.ru" --username "${POSTGRES_USER}_${POSTGRES_USER}" --password "${POSTGRES_USER}_${POSTGRES_PORT}"
