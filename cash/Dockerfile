FROM python:3.9.7

ENV PYTHONBUFFERED=1

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt
COPY . .
RUN python3 manage.py makemigrations main
RUN python3 manage.py migrate

EXPOSE 8000

CMD ["gunicorn"  , "-b", "0.0.0.0:8000", "cash.wsgi:application"]

