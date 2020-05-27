#!/usr/bin/python
# -*- coding: <encoding name> -*-

from dbmodel.dbbase import BaseModel
from logger import logger
from dbmodel.sql_tpl import SQL_TPL
from datetime import datetime

class DataModel(BaseModel):

    def get_data(self, dims=None, args={}):

        sql = SQL_TPL.get(dims, None)
        if not sql:
            logger.warning('没有找到sql')
            return []

        # 先从缓存获取数据

        # 参数转换
        sql = sql % args

        params = {

            'sql': sql,

        }

        datenow = datetime.now().strftime('%Y-%m-%d')
        res = self.db_mongodb.buniss.find_one(params)
        if not res:
            logger.info("从mysql中获取数据")
            data = self.db_mysql.query_list(sql=sql)
            for item in data:
                fcount = int(item.get('activecount', 0))
                item['activecount'] = fcount

            params = {

                'sql': sql,
                'data': data,
                'flushdate': datenow,
                'flushcount': 1

            }
            self.db_mongodb.buniss.insert_one(params)
        else:
            logger.info("从mongo中获取数据")
            self.db_mongodb.buniss.update(params, {"$set": {'flushdate': datenow}, "$inc": {'flushcount': 1}}, False, True)
            data = res.get('data', [])

        return data



if __name__ == '__main__':
    db = DataModel()

    params = {
        'sdata': '2020-03-06',
        'edata': '2020-03-08'
    }
    db.get_data(dims='chart1', args=params)





