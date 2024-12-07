FROM python:3.11.4-slim-bullseye

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY . /app/

RUN apt-get update

COPY ./requirements.txt .
RUN pip install -r requirements.txt



# Command to run the app
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "PostingItems.wsgi:application"]