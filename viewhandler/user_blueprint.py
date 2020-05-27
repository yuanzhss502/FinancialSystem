#!/usr/bin/python
# -*- coding: <encoding name> -*-

from flask import Blueprint, jsonify, g, session
from control.usercontrol import UserControl
from commom.auth import auth

user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/login', methods = ['GET','POST'])
def login():

    control =UserControl(args=g.args, session=session)

    response = control.user_login()

    return jsonify(response)

@user.route('/logout', methods = ['POST'])
def logout():

    control = UserControl(args=g.args, session=session)
    response = control.user_logout()
    return jsonify(response)


@user.route('/test')
@auth.login_require
def test():

    return  jsonify({'code': 0, 'msg': '已经登录'})