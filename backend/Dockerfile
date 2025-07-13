FROM python:3.9.23-slim-bookworm

WORKDIR /code

COPY backend/app/requirements.txt .

RUN pip install -r requirements.txt

COPY ./backend/app .

CMD ["python", "main.py"]
