# pull official base image
FROM python:3.7-stretch

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /usr/src/app/Pipfile
RUN pipenv install --skip-lock --system --dev

# install net-tools
RUN apt-get update && apt-get install -y netcat

# copy entrypoint.sh
COPY ./scripts/entrypoint.sh /usr/src/app/scripts/entrypoint.sh

# copy project
COPY ./backend /usr/src/app/backend
COPY ./manage.py /usr/src/app/

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/scripts/entrypoint.sh"]
