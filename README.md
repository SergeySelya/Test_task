executor: Selivonchick Sergey

## Задание 1: Docker image
* Build and launch:
```bash
docker build -t flask-ping .
docker run -p 5000:5000 flask-ping
```
* Сheck
```bash
curl http://localhost:5000/ping
```
