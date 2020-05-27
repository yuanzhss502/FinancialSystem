#!/usr/bin/python
# -*- coding: <encoding name> -*-

import redis

def Connection(host='127.0.0.1',port=6379):

    pool = redis.ConnectionPool(host=host, port=port)
    redis_tmp = redis.Redis(connection_pool=pool)
    return redis_tmp