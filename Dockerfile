FROM python:3.9-slim-buster

WORKDIR /app

COPY . /app

# ✅ Instalás Flask directamente
RUN pip install Flask
RUN pip install Flask flask_pymongo

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]
