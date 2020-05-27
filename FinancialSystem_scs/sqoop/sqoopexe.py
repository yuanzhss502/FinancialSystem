#!/usr/bin/python
# -*- coding: <encoding name> -*-

import paramiko
from logger import logger
from sqoop.db_mysql import Connection
import config
from datetime import datetime


class ShellExec(object):

    host = '192.168.3.100'
    port = 22
    user = 'yuanzhss'
    password = 'puluyu123'

    mysql_db = Connection(host=config.MYSQL_HOST, port=config.MYSQL_PORT, user=config.MYSQL_USERNAME, password=config.MYSQL_PASSWORD, database=config.MYSQL_DATABASE)

    def __init__(self, date):
        self._connect()

        if date:
            self.today = date
        else:
            self.today = datetime.now().date().strftime('%Y-%m-%d')

        self.export_cmd = """
            /usr/local/sqoop/bin/sqoop export  \
            --connect "jdbc:mysql://192.168.3.100:3306/analysis?useUnicode=true&characterEncoding=utf-8"   \
            --username root --password puluyu123  \
            --table {tablename} -m 1  \
            --export-dir /user/hadoop/analysis/{tablename}/dt={fdate}/  \
            --fields-terminated-by ',' 
        
        """

    def _connect(self):
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
            self.ssh.connect(hostname=self.host, port=self.port, username=self.user, password=self.password)
        except Exception as e:
            logger.error('connection fail -- {}'.format(e))

    def execute(self, cmd=None):
        logger.info('info -- {}'.format(cmd))

        stdin, stdout, stderr = self.ssh.exec_command(cmd)

        return stdout.read(), stderr.read()

    def create_table(self):
        raise '子类必须实现'

    def do_jobs(self):
        raise '子类必须实现'

    def __call__(self, *args, **kwargs):


        logger.info("开始建表")
        res = self.create_table()
        if res:
            logger.info("建表成功")
        else:
            logger.warning("建表失败")

        logger.info("开始导出，耐心等候")
        res = self.do_jobs()
        if res:
            logger.info("统计成功")
        else:
            logger.warning("统计失败")

if __name__ == '__main__':

    obj = ShellExec()

    stdout, stderr = obj.execute('ls')

    print(stdout)
    print(stderr)