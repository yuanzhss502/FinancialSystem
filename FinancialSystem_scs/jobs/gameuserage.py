#!/usr/bin/python
# -*- coding: <encoding name> -*-

import sys

sys.path.append('/home/yuanzhss/scs_jobs/scs_job')
from dbbase.HiveBase import HiveBase


class GameUserAge(HiveBase):

    def create_table(self):
        hql = """

            create table if not EXISTS analysis.gameuserage (fdate string, fgametime int, fage int)
            partitioned by (dt string)
            row format delimited fields terminated by ','
            location '/user/hadoop/analysis/gameuserage'

        """
        return self.execute(hql)

    def do_jobs(self):
        hql = """

            insert overwrite table analysis.gameuserage
            partition (dt='{fdate}')
            select gt.fdate as fdate, sum(gt.fgametime) as fgametime, ui.fage as fage from stat.gametime as gt
            left join stat.userinfo as ui
            on gt.fuserid=ui.fuserid
            where gt.fdate='{fdate}'
            group by ui.fage, gt.fdate
             """.format(fdate=self.today)

        return self.execute(hql)


if __name__ == "__main__":
    try:
        date = sys.argv[1]
    except Exception as e:
        date = None

    obj = GameUserAge(date)
    obj()

