FROM python:3.8.1-slim-buster

WORKDIR /usr/src/app

# Variables para que python no cree archivos pyc y para que no envie mensajes a consola
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instalar los paquetes para construir el cliente de postgressql psycopg2-binary con pip
RUN apt update
RUN apt-get install -y gcc-8 libpq-dev
RUN ln -s /usr/bin/gcc-8 /usr/bin/gcc

# Instalar mas dependencias
RUN apt-get install -y netcat

# Actualizando pip e instalando los paquetes necesarios
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app

# Ejecuta entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
