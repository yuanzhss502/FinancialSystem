#!/usr/bin/python
# -*- coding: <encoding name> -*-

from dbmodel.dbbase import BaseModel
import datetime
from datetime import timedelta
import random

def insert_test_data():

    db = BaseModel()

    insert_test_data = 'insert into gameactive (fdate, fuserid, fgameid) values '

    sql_list =[]

    for j in range(1,10):
        fdate = (datetime.datetime.now().date() + timedelta(days=j)).strftime('%Y-%m-%d')
        temp = random.randrange(1,1000)
        for i in range(1, temp):
            sql = "('{}', {}, {}) ".format(fdate, i+1000, i)
            sql_list.append(sql)

    sql_temp = ','.join(sql_list)
    sql = insert_test_data + sql_temp

    print(db.db_mysql.execute_commit(sql))


if __name__ == '__main__':

    insert_test_data()