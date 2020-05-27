#!/usr/bin/python
# -*- coding: <encoding name> -*-

from control.basecontrol import BaseControl
from commom.response import Response
from dbmodel.datamodel import DataModel
from _collections import defaultdict
from dbmodel.userinfomodel import UserinfoModel
from dbmodel.authtablemodel import AuthTableModel



class DataControl(BaseControl):

    def __init__(self, *args, **kwargs):
        super(DataControl, self).__init__(*args, **kwargs)

        self.datamodel = DataModel()
        self.userinfomodel = UserinfoModel()
        self.authtablemodel = AuthTableModel()


    def auth_required(self, dimsname=None):
        '''
        根据用户等级及请求表格要求权限来检验用户是否具有权限
        '''

         # 获取用户工号及等级
        fworkid = self.session.get('fwork_id', None)
        userinfo = self.userinfomodel.get_userinfo(fworkid=fworkid)
        flevel_id = userinfo.get(b'flevel_id', 0)
         # 获取表格所需要权限
        levelinfo = self.authtablemodel.get_dims_level_info(dimsname=dimsname)
        dims_flevel_id = levelinfo.get(b'flevel_id', 10000)


         # 比较
        if flevel_id < dims_flevel_id:
            return False
        return True


    def format_data(self, dims=None):
        '''
        格式化数据
        输入数据
        dims={
            'data':['activatecount': 144,'fdate':'2017-3-3']
            'name': 'activate'
        }
        输出数据
        #     'title': 'sahjgds',
        #     'xAxis': ['dshja', 'dsadsd', 'dsaww', 'dswwwq', 'dsaw', 'gdse'],
        #     'series': [{'name': 'dads',
        #                 'type': 'bar',
        #                 'data': [5, 20, 30, 21, 45]}]
        '''
        data = dims.get('data',[])
        name = dims.get('name','')
        type = dims.get('type', 'bar')

        dict_data = defaultdict(list)

        for item in data:        #{'2020-2-25':[144,29,43]}
            key = item.get('fdate','')
            dict_data[key].append(item.get(name))

        axis_x = []
        axis_y = []
        temp = sorted(dict_data.items(), key=lambda x : x[0], reverse=False)
        for key, obj in temp:
            axis_x.append(key)
            sum_data = sum([num for num in obj if isinstance(num, (float, int))])
            axis_y.append(sum_data)

        dims = {

            'title': '所有游戏活跃度',
            'xAxis': axis_x,
            'series': [{
                'name': name,
                'type': type,
                'data': axis_y,

            }]

        }
        return dims


    def user_get_data(self):

        dims = self.args.get('dims')
        if not dims:
            return Response.responseJson(Response.INPUT_EMPTY, '输入指标为空')

        isAuth = self.auth_required(dimsname=dims)
        if not isAuth:
            return Response.responseJson(Response.NO_AUTH)

        params = {

            'sdata': self.args.get('sdata', ''),
            'edata': self.args.get('edata', '')

        }



        data = self.datamodel.get_data(dims=dims, args=params)

        dims = {

            'name': dims,
            'type': 'bar',
            'data': data

        }

        res_data = self.format_data(dims=dims)
        print(res_data)
        # option = {
        #     'title': 'sahjgds',
        #     'xAxis': ['dshja', 'dsadsd', 'dsaww', 'dswwwq', 'dsaw', 'gdse'],
        #     'series': [{'name': 'dads',
        #                 'type': 'bar',
        #                 'data': [5, 20, 30, 21, 45]}]
        # }
        return Response.responseJson(Response.SUCCESS, data=res_data, msg="获取数据成功")


