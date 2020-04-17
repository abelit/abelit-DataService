# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2020/03/21 08:30:15
@Author  :   Abelit
@Version :   1.0
@Contact :   ychenid@live.com
@Copyright :   (C)Copyright 2020, dataforum.org
Licence :   BSD-3-Clause
@Desc    :   None
'''


from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_restful import Api, Resource


# 自定义模块
from db import db
from config import config

#from utils.middleware import Middleware
from app.home.views import home as home_blueprint

from app.feedback.views import feedback as feedback_blueprint
from app.feedback.views import api as feedbackapi
from app.feedback.views import GiftCardResource,ShopCardResource

from app.employee.views import employee as employee_blueprint
from app.employee.views import api as employeeapi
from app.employee.views import EmployeeAttendance,EmployeeAttendanceDevice

# import ptraffic blueprint
from app.ptraffic.views import ptraffic as ptraffic_blueprint

# 创建flask实例对象
app = Flask(__name__)

# 从config.py中导入配置信息
app.config.from_object(config)

# 导入日志配置信息
config.init_app(app)

# 使用flask-sqlalchemy
db.init_app(app)

# 跨域设置
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# 创建JWT实例对象
jwt = JWTManager(app)

# 注册中间件
# app.wsgi_app = Middleware(app.wsgi_app, request.path)

# 中间件
@app.before_request
def process_start_request():
    # print("正在访问： "+request.path)
    # app.wsgi_app = Middleware(app.wsgi_app, request.path)
    print(request.remote_addr)


@app.after_request
def process_end_request(response):
    print("结束访问： "+request.path)
    # Error "AttributeError: 'NoneType' object has no attribute 'headers'" will bring up if no return response
    return response


@app.errorhandler(404)
def not_found(error):
    return jsonify({"err": 404, "msg": "page not found"}), 404


# 注册自定义blueprint模块
app.register_blueprint(home_blueprint)

# 添加资源 feedback & 注册自定义blueprint模块
feedbackapi.add_resource(GiftCardResource, '/gift')
feedbackapi.add_resource(ShopCardResource, '/shop')
app.register_blueprint(feedback_blueprint, url_prefix="/api/feedback")

# import employee
employeeapi.add_resource(EmployeeAttendance, '/attend')
employeeapi.add_resource(EmployeeAttendanceDevice, '/device')
app.register_blueprint(employee_blueprint, url_prefix="/api/employee")

# import ptraffic
app.register_blueprint(ptraffic_blueprint, url_prefix="/api/ptraffic")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5060)
