# -*- encoding: utf-8 -*-
'''
@File    :   views.py
@Time    :   2020/03/21 08:31:39
@Author  :   Abelit
@Version :   1.0
@Contact :   ychenid@live.com
@Copyright :   (C)Copyright 2020, dataforum.org
Licence :   BSD-3-Clause
@Desc    :   None
'''


from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import time


from db import db
from models import Group, Position, User, Role, Menu, Session

admin = Blueprint("admin", __name__)


@admin.route('/ping')
def ping():
    return jsonify({
        "ping": "Pong!",
        "ip": request.remote_addr,
        "router": request.path,
        "module": __name__
    })
