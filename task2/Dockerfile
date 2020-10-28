# Idare Task
# Version: 1.0

FROM python:3

WORKDIR /usr/src/idare_assignment/task2

COPY Pipfile Pipfile.lock ./

RUN pip install -U pipenv

RUN pipenv install --system

COPY . .