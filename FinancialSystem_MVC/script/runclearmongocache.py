#!/usr/bin/python
# -*- coding: <encoding name> -*-

from dbmodel.dbbase import BaseModel
from datetime import datetime, timedelta
from pymongo import ASCENDING, DESCENDING


class ClearMongoDBCache(BaseModel):

    def __init__(self):
        self.maxcount = 995

    def insert_test(self):
        for i in range(10):
            date = (datetime.now() + timedelta(days=i)).strftime('%Y-%m-%d')
            for j in range(100):
                params = {

                    'sql': "select * from fdate={} and i={}".format(date, str(j)),
                    'flushdate': date,
                    'flushcount': j,
                    'data': {'a': 1}

                }
                self.db_mongodb.buniss.insert_one(params)

    def run_script(self):

        count = self.db_mongodb.buniss.count()
        overcount = count - self.maxcount

        if overcount > 0:
            res_data = self.db_mongodb.buniss.find().sort([('flushdate', ASCENDING), ('flushcount', ASCENDING)]).limit(overcount)
            res_sql_list = [item.get('sql', '') for item in res_data]
            print(res_sql_list)
            self.db_mongodb.buniss.remove({"sql": {"$in": res_sql_list}})

if __name__ == "__main__":
    test = ClearMongoDBCache()
    test.run_script()

