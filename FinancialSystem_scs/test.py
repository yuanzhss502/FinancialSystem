#!/usr/bin/python
# -*- coding: <encoding name> -*-
import random
from datetime import datetime, timedelta

def test():
    area_list = [u'重庆', u'广州', u'北京', u'上海', u'海口']
    fd = open('/stat/userinfo/userinfo.txt', 'wt')
    for i in range(1000):
        userid =str(100 + i)
        age = str(random.randrange(10,40))
        area = str(random.choice(area_list))
        user_money = str(i)
        str_temp = userid + ',' + age + ',' + area + ',' + user_money + '\n'
        fd.write(str_temp)

    fd.close()

def gameinfo():

    game_list = [u'斗地主', u'梦幻', u'石器时代', u'魔力', u'英雄联盟']
    fd = open('/stat/gameinfo/gameinfo.txt', 'wt')
    for i in range(4):
        gameid = str(i)
        gamename = str(game_list[i])
        str_temp = gameid + ',' + gamename + '\n'
        fd.write(str_temp)

    fd.close()

def gametime():

    gameid_list = [0, 1, 2, 3]
    gametime_list = [10, 15, 20, 50, 80, 90]

    for j in range(10):
        date = (datetime.now() + timedelta(days=j)).strftime('%Y-%m-%d')
        fd = open('/Users/yuanzhss/PycharmProjects/scs_job/gametime {}.txt'.format(date), 'wt')
        for i in range(1000):
            fdate = str(date)
            userid = str(100 + i)
            gameid = str(random.choice(gameid_list))
            gametime = str(random.choice(gametime_list))
            str_temp = fdate + ',' + userid + ',' + gameid + ',' + gametime + '\n'
            fd.write(str_temp)
        fd.close()

def userfee():

    gameid_list = [0, 1, 2, 3]
    userfee_list = [10, 15, 50, 100, 200, 1000]

    for j in range(10):
        date = (datetime.now() + timedelta(days=j)).strftime('%Y-%m-%d')
        fd = open('/Users/yuanzhss/PycharmProjects/scs_job/userfee {}.txt'.format(date), 'wt')
        for i in range(1000):
            fdate = str(date)
            userid = str(100 + i)
            gameid = str(random.choice(gameid_list))
            userfee = str(random.choice(userfee_list))
            str_temp = fdate + ',' + userid + ',' + gameid + ',' + userfee + '\n'
            fd.write(str_temp)

        fd.close()


if __name__ == "__main__":
    gametime()
    userfee()


