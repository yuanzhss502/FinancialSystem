#!/usr/bin/python
# -*- coding: <encoding name> -*-

import sys
sys.path.append('/home/yuanzhss/scs_jobs/scs_job')
from dbbase.HiveBase import HiveBase


class GameInfo(HiveBase):

    def create_table(self):
        hql = """

            create table if not EXISTS stat.gameinfo (fgameid int, fgamename string)
            row format delimited fields terminated by ','
            location '/user/hadoop/stat/gameinfo'

        """
        return self.execute(hql)

    def do_jobs(self):
        hql = """

            load data inpath '/user/hadoop/stat/gameinfo' into table stat.gameinfo

        """
        return self.execute(hql)


if __name__ == "__main__":
    obj = GameInfo()
    obj()