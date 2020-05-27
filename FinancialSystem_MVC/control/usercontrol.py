#!/usr/bin/python
# -*- coding: <encoding name> -*-

from commom.response import Response
from dbmodel.userinfomodel import UserinfoModel
from control.basecontrol import BaseControl


class UserControl(BaseControl):

    def __init__(self, *args, **kwargs):
        super(UserControl, self).__init__(*args, **kwargs)

        self.userinfomodel =UserinfoModel()

    def user_login(self):

        fwork_id = self.args.get('fwork_id', None)
        fpassword = self.args.get('fpassword', None)

        if not fwork_id:
            return Response.responseJson(Response.INPUT_EMPTY, msg="账号为空")

        if not fpassword:
            return Response.responseJson(Response.INPUT_EMPTY, msg="密码为空")

        res = self.userinfomodel.check_userauth(fwork_id=fwork_id, fpassword=fpassword)

        if res:
            self.session['fwork_id'] = fwork_id
            return Response.responseJson(Response.SUCCESS, msg="登录成功")
        else:
            return Response.responseJson(Response.ERROR, msg="账号或者密码错误")


    def user_logout(self):
        self.session.pop('fwork_id', None)
        return Response.responseJson(Response.SUCCESS, msg="注销成功")