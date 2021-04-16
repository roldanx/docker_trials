#!/usr/bin/env python3

import redis
from datetime import datetime
from flask import Flask

redis_host = "redis"
redis_port = 6379
count = 0

app = Flask(__name__)

@app.route("/hello")
def say_hello():
    return "Hello from write-app!"

@app.route("/write")
def write_on_redis():
    try:
        # Create connection
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=None, decode_responses=True)

        global count
        count += 1

        # Write
        r.set("time:" + str(count), datetime.now().strftime("%H:%M:%S"))

        return "Timedate successfully stored on redis with key time:"  + str(count) + "\n"
   
    except Exception as e:
        print(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
