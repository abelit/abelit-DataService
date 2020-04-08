from flask import Flask, Blueprint, jsonify, request
from flask_restful import Api, Resource,request

from models import EmployeeAttendanceModel
from db import db

employee = Blueprint('employee', __name__)

api = Api(employee)


@employee.route('/ping')
def ping():
    return jsonify({
        "ping": "Pong!",
        "ip": request.remote_addr,
        "router": request.path,
        "module": __name__
    })

class EmployeeAttendance(Resource):
    def get(self):
        msg, code = 'ok', 200
        return jsonify({
            "msg": msg,
            "code": code
        })

    def post(self):
        req_data = request.json

        msg, code = 'ok', 200

        userid = req_data.get('ID')
        username = req_data.get('Name')
        checktime = req_data.get('Time')
        temperature = req_data.get('TP')

        emp_attend = EmployeeAttendanceModel(userid=userid, username=username, checktime=checktime, temperature=temperature)

        try:
            db.session.add(emp_attend)
            db.session.commit()
            msg, code = 'ok', 200
        except Exception:
            msg, code = 'failed', 500
            db.session.rollback()

        return jsonify({"msg": msg,"code": code})
