# 📦 Задание 1: Docker image
🔧 Сборка и запуск
'''
docker build -t flask-ping .
docker run -p 5000:5000 flask-ping
'''

🔍 Проверка
'''
curl http://localhost:5000/ping
'''
