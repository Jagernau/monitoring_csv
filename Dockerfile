FROM python:3.10
COPY . /monitoring_db_autosave
WORKDIR /monitoring_db_autosave
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
