#!/usr/bin/python
# -*- coding: <encoding name> -*-


from pymysql.cursors import DictCursor
from logger import logger
import pymysql

class Connection(object):

    def __init__(self, host='192.168.3.100' ,port=3306 ,database='xxxSystem', user='root', password='puluyu123',charset='utf8'):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.charset = charset

    def execute_commit(self, sql=None):

        try:

            conn = pymysql.connect(host=self.host,port=self.port,user=self.user,password=self.password,db=self.database,charset=self.charset,cursorclass=DictCursor)
            logger.info('sql - {}'.format(sql))

            with conn.cursor() as cursor:
                cursor.execute(sql)
            conn.commit()
            cursor.close()
            return True


        except Exception as e:
            logger.error('SQL执行异常--{}'.format(e))
            conn.rollback()
            cursor.close()
            return False

    def execute_query(self,sql=None):
        try:

            conn = pymysql.connect(host=self.host,port=self.port,user=self.user,password=self.password,db=self.database,charset=self.charset,cursorclass=DictCursor)
            logger.info('sql - {}'.format(sql))

            with conn.cursor() as cursor:
                cursor.execute(sql)
                data_list = cursor.fetchall()
            logger.info('sql -- {}'.format(data_list))
            cursor.close()
            return data_list


        except Exception as e:
            logger.error('SQL执行异常--{}'.format(e))
            conn.rollback()
            cursor.close()
            return []

    def query_one_dict(self,sql=None):
        data = self.execute_query(sql)
        if data:
            return data[0]
        else:
            return {}

    def query_list(self,sql=None):
        return self.execute_query(sql)

if __name__ == '__main__':
    db = Connection()

    sql = 'select * from userinfo'

    db.query_list(sql)
    db.query_one_dict(sql)