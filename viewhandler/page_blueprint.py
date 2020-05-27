#!/usr/bin/python
# -*- coding: <encoding name> -*-

from flask import Blueprint, jsonify, g, render_template

page = Blueprint('page',__name__,url_prefix='/page')

@page.route('/index')
def index():
    print(g.args)
    return jsonify({'dsad': 1111})

@page.route('/main/')
def main():
    return render_template('main.html')
