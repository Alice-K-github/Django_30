# Указываем базовый образ
FROM python:3.12.9

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл с зависимостями и устанавливаем их
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта в контейнер
COPY . .


RUN mkdir -p /app/media/

# Открываем порт 8000 для взаимодействия с приложением
EXPOSE 8000

# Определяем команду для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
