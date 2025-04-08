# Используем Python 3.9 как базовый образ
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы приложения
COPY app.py .
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт 5000
EXPOSE 5000

# Запуск приложения
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]