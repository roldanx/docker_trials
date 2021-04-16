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
    return "Hello from read-app!"

@app.route("/read")
def read_on_redis():
    try:
        # Create connection
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=None, decode_responses=True)

        # Read
        key_arr = []
        # value_arr = []
        for key in r.scan_iter("time:*"):
            key_arr.append(key)
        #     value_arr.append(r.get(key))
        # print(key_arr)
        # print(value_arr)

        # Return stringified keys  
        if (len(key_arr) > 0): 
            sep = " "
            result = sep.join(key_arr) + "\n"
        else:
            result = "No writes have been made yet :("

        return result
   
    except Exception as e:
        print(e)
        result = "Redis is not available :(\n"
        return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
