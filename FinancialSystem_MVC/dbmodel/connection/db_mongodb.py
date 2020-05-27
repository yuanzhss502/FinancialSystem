#!/usr/bin/python
# -*- coding: <encoding name> -*-

from pymongo import MongoClient

def Connection(host='127.0.0.1',port=27017, database=None):

    conn = MongoClient(host=host,port=port)
    mongo = eval('conn.' + database)
    return mongo

if __name__ == "__main__":
    db = Connection(host='192.168.3.100', database='xxx')
    print(db.test.insert_one({'a': 1}))
    print(db.test.find_one)