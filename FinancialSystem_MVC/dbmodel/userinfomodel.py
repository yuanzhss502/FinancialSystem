#!/usr/bin/python
# -*- coding: <encoding name> -*-

from dbmodel.dbbase import BaseModel
from logger import logger
import json

class UserinfoModel(BaseModel):

    def check_userauth(self, fwork_id=None, fpassword=None):
        if not fwork_id or not fpassword:
            logger.warning('账号密码为空')
            return False

        sql = "select fname, fwork_id, fdept_id, flevel_id from userinfo where fwork_id={fwork_id} and fpassword={fpassword};".format(fwork_id=fwork_id, fpassword=fpassword)
        data = self.db_mysql.query_one_dict(sql)
        return True if data else False

    def get_userinfo(self, fworkid):

        if not fworkid:
            logger.warning('工号为空')
        # 字符串
        # hash
        redis_key = self.produce_redis_keys('userinfo', fworkid)
        data = self.redis_db.hgetall(redis_key)
        if not data:
            print("从redis中取数据")
            sql = "select fname, fwork_id, fdept_id, flevel_id from userinfo where fwork_id={fworkid}".format(fworkid=fworkid)
            data = self.db_mysql.query_one_dict(sql)
            if data:
                self.redis_db.hmset(redis_key, data)
                self.redis_db.expire(redis_key, self.redis_time)


        return data

if __name__ == "__main__":
    db = UserinfoModel()
    print(db.get_userinfo(fworkid=1000))