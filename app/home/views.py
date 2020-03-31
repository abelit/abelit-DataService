# -*- encoding: utf-8 -*-
'''
@File    :   views.py
@Time    :   2020/03/21 08:32:03
@Author  :   Abelit
@Version :   1.0
@Contact :   ychenid@live.com
@Copyright :   (C)Copyright 2020, dataforum.org
Licence :   BSD-3-Clause
@Desc    :   None
'''


from flask import render_template, Blueprint, request, jsonify, current_app

home = Blueprint("home", __name__)

# 入口文件，通过入口文件跳转到vue前端
@home.route('/')
def index():
    # flash('You were successfully logged in')
    return render_template('index.html')


@home.route('/api/ping')
def ping():
    return jsonify({
        "ping": "Pong!",
        "ip": request.remote_addr,
        "router": request.path,
        "module": __name__
    })


@home.route('/api')
def get_api():
    rules = []
    for rule in current_app.url_map.iter_rules():
        rules.append({
            "rule": rule.rule,
            "endpoint": rule.endpoint,
            "methods": str(rule.methods)
        })

    return jsonify({
        "msg": "apis",
        "rules": rules
    })
