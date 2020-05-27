#!/usr/bin/python
# -*- coding: <encoding name> -*-

from flask import session, jsonify
from commom.response import Response

class Auth():


    def login_require(self,func):

        def wrap(*args,**kwargs):

            isLogin = True if session.get('fwork_id', None) else False

            if not isLogin:
                return jsonify(Response.responseJson(Response.NOT_LOGIN))
            return func(*args, **kwargs)

        return wrap

auth = Auth()
