#!/usr/bin/env python3

# step 1: import the redis-py client package
import redis

# step 2: define our connection information for Redis
# Replaces with your configuration information
redis_host = ""
redis_port = 0
redis_password = ""


def hello_redis():
    """Example Hello Redis Program"""
   
    # step 3: create the Redis Connection object
    try:
   
        # The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
        # using the default encoding utf-8.  This is client specific.
        # r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
        r = redis.Redis(host=redis_host, ssl=True, port=redis_port, password=redis_password)
   
        print("setting redis key")
        # step 4: Set the hello message in Redis
        r.set("msg:hello", "Hello Redis!!!")
        r.set("foo",100)
        r.incr("foo")

        newfoo = r.get("foo")
        print(newfoo)
        # step 5: Retrieve the hello message from Redis
        msg = r.get("msg:hello")
        print(msg)        
   
    except Exception as e:
        print(e)


if __name__ == '__main__':
    hello_redis()