# Указываем базовый образ
FROM python:3.9

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл с зависимостями и устанавливаем их
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта в контейнер
COPY . .

ENV DATABASE_URL='postgres://postgres:AlisaKa145@localhost:5432/postgres2'
ENV SECRET_KEY='django-insecure-v@d4$20cv#^x32^-cktx-j%xhtn4rxu+hz_*&m1yu^$w5pjtu+'
ENV CELERY_BROKER_URL='redis://redis:6379/2'

RUN mkdir -p /app/media/

# Открываем порт 8000 для взаимодействия с приложением
EXPOSE 8000

# Определяем команду для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
