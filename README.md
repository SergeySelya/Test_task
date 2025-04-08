executor: Selivonchick Sergey

## Task 1: Docker image
* Build and launch:
```bash
docker build -t flask-ping .
docker run -p 5000:5000 flask-ping
```
* Сheck
```bash
curl http://localhost:5000/ping
```

## Task 2: Docker compose
* Build and launch:
```bash
docker-compose up -d --build
```
* Сheck
```bash
http://localhost:5000/ping
http://localhost:5000/count
```

# Output example
http://localhost:5000/ping
<img width="195" alt="image" src="https://github.com/user-attachments/assets/543abb0f-b193-4cdc-8945-2b357ec1d1b5" />

http://localhost:5000/count
<img width="632" alt="image" src="https://github.com/user-attachments/assets/4d99f40c-d969-492f-9f27-ac92c1ebacae" />


