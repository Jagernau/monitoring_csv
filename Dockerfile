FROM python:3.10
COPY . /monitoring_db_autosave
WORKDIR /monitoring_db_autosave
# Database

# Postgres
ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_DB_NAME=${POSTGRES_DB_NAME}
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "create_tables.py"]
