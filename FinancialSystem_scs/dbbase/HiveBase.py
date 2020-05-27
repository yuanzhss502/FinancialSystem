#!/usr/bin/python
# -*- coding: <encoding name> -*-

from pyhive import hive
from logger import logger
import config
from datetime import datetime

class HiveBase(object):

    def __init__(self, date=None):
        self.host = config.HIVE_HOST
        self.port = config.HIVE_PORT
        if date:
            self.date = date
        else:
            self.today = datetime.now().date().strftime('%Y-%m-%d')

    def execute(self, hql=None):

        try:
            logger.info("hql-- {}".format(hql))


            conn = hive.connect(host=self.host, port=self.port)
            cursor = conn.cursor()
            cursor.execute(hql)
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            logger.error("hive 执行异常")
            cursor.close()
            conn.close()
            return False


    def create_table(self):
        raise '子类必须实现创建表的方法'


    def do_jobs(self):
        raise '子类必须实现统计表的方法'

    def __call__(self, *args, **kwargs):

        logger.info("开始建表")
        res = self.create_table()
        if res:
            logger.info("建表成功")
        else:
            logger.warning("建表失败")

        logger.info("开始统计，耐心等候")
        res = self.do_jobs()
        if res:
            logger.info("统计成功")
        else:
            logger.warning("统计失败")