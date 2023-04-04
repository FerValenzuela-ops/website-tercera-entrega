FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements /app/requirements
RUN pip install --no-cache-dir -r requirements/production.txt

COPY . /app

ENV DJANGO_SETTINGS_MODULE=lindasonrisa_website.settings.production

EXPOSE 8080

CMD ["gunicorn", "--bind=0.0.0.0:8080", "lindasonrisa_website.wsgi"]
