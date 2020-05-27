#!/usr/bin/python
# -*- coding: <encoding name> -*-

import sys
sys.path.append('/home/yuanzhss/scs_jobs/scs_job')
from sqoop.sqoopexe import ShellExec


class ExportGameactive(ShellExec):

    def create_table(self):
        sql = """create table if not EXISTS gameuserage
        (fdate varchar(64), fgametime int, fage int)
        default  charset utf8

        """

        return self.mysql_db.execute_commit(sql)

    def do_jobs(self):
        sqoop_export = self.export_cmd.format(tablename='gameuserage', fdate=self.today)

        return self.execute(cmd=sqoop_export)


if __name__ == '__main__':
    try:
        date = sys.argv[1]
    except Exception as e:
        date=None

    obj = ExportGameactive(date)
    obj()

