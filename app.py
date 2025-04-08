from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = 6379
r = redis.Redis(host=redis_host, port=redis_port, db=0)

@app.route("/ping")
def ping():
    return jsonify(status="ok"), 200

@app.route('/count')
def count():
    try:
        visits = r.incr('counter')
        return jsonify(
            status="ok",
            visits=visits,
            message=f"This page has been visited {visits} times."
        ), 200
    except redis.ConnectionError:
        return jsonify(
            status="error",
            message="Could not connect to Redis"
        ), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

