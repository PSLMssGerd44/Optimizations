FROM python:3.10.12-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

RUN python -m pip install --upgrade pip

RUN pip install  pipenv==2023.6.12

COPY Pipfile* . 

RUN pipenv install --deploy --system 

COPY . .
