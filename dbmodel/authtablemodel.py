#!/usr/bin/python
# -*- coding: <encoding name> -*-

from dbmodel.dbbase import BaseModel
from logger import logger

class AuthTableModel(BaseModel):

    def get_dims_level_info(self, dimsname=None):

        if not dimsname:
            logger.warning('输入dimsname为空')
        redis_key = self.produce_redis_keys('authtable', dimsname)
        data = self.redis_db.hgetall(redis_key)

        if not data:
            sql = "select ftablename, flevel_id from authtable where ftablename='{dimsname}'".format(dimsname=dimsname)
            data = self.db_mysql.query_one_dict(sql)
            if data:
                self.redis_db.hmset(redis_key, data)
                self.redis_db.expire(redis_key, self.redis_time)

        return data

if __name__ == "__main__":
    db = AuthTableModel()
    db.get_dims_level_info('activecount')


