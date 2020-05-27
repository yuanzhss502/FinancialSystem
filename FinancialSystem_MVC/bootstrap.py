#!/usr/bin/python
# -*- coding: <encoding name> -*-

from flask import Flask, g, request, session
from viewhandler.page_blueprint import page
from viewhandler.user_blueprint import user
from viewhandler.data_blueprint import data


app = Flask(__name__)

app.config.from_pyfile('config.py')

BLUEPRINT = [page, user, data]

def bootstrap_app(app):
    for view in BLUEPRINT:
        app.register_blueprint(view)

    @app.context_processor
    def common():
        return {
            'isLogin': True if session.get('fwork_id', None) else False
        }

    @app.before_request
    def before():

        args = {k: v for k, v in dict(request.args).items()}  #get
        args_form = {k: v for k, v in dict(request.form).items()} #port

        args.update(args_form)
        g.args = args


bootstrap_app(app)


if __name__ == '__main__':

    app.run(host=app.config['WEB_HOST'],port=app.config['WEB_PORT'])