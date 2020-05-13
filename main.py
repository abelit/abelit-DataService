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


def create_feedback(_app):
    from app.feedback.views import feedback as feedback_blueprint
    from app.feedback.views import api as feedbackapi
    from app.feedback.views import GiftCardResource,ShopCardResource,ActivityParticipant

     # 添加资源 feedback & 注册自定义blueprint模块
    feedbackapi.add_resource(GiftCardResource, '/gift')
    feedbackapi.add_resource(ShopCardResource, '/shop')
    feedbackapi.add_resource(ActivityParticipant, '/activity')
    _app.register_blueprint(feedback_blueprint, url_prefix="/api/feedback")


def create_traffic(_app):
    # import ptraffic blueprint
    from app.ptraffic.views import ptraffic as ptraffic_blueprint

    # import ptraffic
    _app.register_blueprint(ptraffic_blueprint, url_prefix="/api/ptraffic")


def create_employee(_app):
    from app.employee.views import employee as employee_blueprint
    from app.employee.views import api as employeeapi
    from app.employee.views import EmployeeAttendance,EmployeeAttendanceDevice
    from app.employee.views import scheduler

    employeeapi.add_resource(EmployeeAttendance, '/attend')
    employeeapi.add_resource(EmployeeAttendanceDevice, '/device')
    _app.register_blueprint(employee_blueprint, url_prefix="/api/employee")

    scheduler.init_app(app=_app)
    scheduler.start()


def create_common(_app):
    from app.home.views import home as home_blueprint

    # 注册自定义blueprint模块
    _app.register_blueprint(home_blueprint)

def create_app():
    # 自定义模块
    from db import db
    from config import config

    # 创建flask实例对象
    _app = Flask(__name__)

    # 从config.py中导入配置信息
    _app.config.from_object(config)

    # 导入日志配置信息
    config.init_app(_app)

    # 使用flask-sqlalchemy
    db.init_app(_app)

    # 跨域设置
    cors = CORS(_app, resources={r"/*": {"origins": "*"}})

    # 创建JWT实例对象
    jwt = JWTManager(_app)


    def syncdata():
        print("sync data ...")

    @_app.before_first_request
    def process_first_request():
        print("首次访问：")
        if _app.config['SCHEDULER_ENABLE']:
            from flask_apscheduler import APScheduler
            scheduler = APScheduler()
            # 添加job
            scheduler.add_job(func=syncdata, id=_app.config['SCHEDULER_ID'], trigger='interval', seconds=_app.config['SCHEDULER_INTERVAL'], replace_existing=True)
            scheduler.init_app(app=_app)
            scheduler.start()
        
    # 中间件
    @_app.before_request
    def process_start_request():
        print("正在访问： "+request.path)
        print(request.remote_addr)


    @_app.after_request
    def process_end_request(response):
        print("结束访问： "+request.path)
        # Error "AttributeError: 'NoneType' object has no attribute 'headers'" will bring up if no return response
        return response

    @_app.errorhandler(404)
    def not_found(error):
        return jsonify({"err": 404, "msg": "page not found"}), 404

    create_common(_app)

    create_feedback(_app) if 'feedback' in _app.config['APPS'] else None
    create_traffic(_app) if 'traffic' in _app.config['APPS'] else None
    create_employee(_app) if 'employee' in _app.config['APPS'] else None

    return _app
    

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5060)
