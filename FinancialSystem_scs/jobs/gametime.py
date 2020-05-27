#!/usr/bin/python
# -*- coding: <encoding name> -*-

import sys
sys.path.append('/home/yuanzhss/scs_jobs/scs_job')
from dbbase.HiveBase import HiveBase


class GameTime(HiveBase):

    def create_table(self):
        hql = """

            create table if not EXISTS stat.gametime (fdate string, fuserid int, fgameid int, fgametime int)
            partitioned by (dt string)
            row format delimited fields terminated by ','
            location '/user/hadoop/stat/gametime'

        """
        return self.execute(hql)

    def do_jobs(self):
        hql = """

            alter table stat.gametime add if not EXISTS partition (dt='{fdate}')
            location '/user/hadoop/stat/gametime/{fdate}'

        """.format(fdate=self.today)
        return self.execute(hql)


if __name__ == "__main__":
    try:
        date = sys.argv[1]
    except Exception as e:
        date=None

    obj = GameTime(date)
    obj()