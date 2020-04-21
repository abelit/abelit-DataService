from flask import Flask, Blueprint, jsonify, request
from flask_restful import Api, Resource,request
from sqlalchemy.sql import and_
import time

from models import EmployeeAttendanceModel,EmployeeAttendanceDeviceModel
from db import db

from app.employee.dbconnect import MSSQLServer

employee = Blueprint('employee', __name__)

api = Api(employee)


@employee.route('/ping')
def ping():
    results = mssql.select(sql)
    print(results[0][1])
    return jsonify({
        "ping": "Pong!",
        "ip": request.remote_addr,
        "router": request.path,
        "module": __name__
    })

class EmployeeAttendance(Resource):
    def get(self):
        msg, code = 'ok', 200
        starttime = request.args.get('start')
        endtime = request.args.get('end')
        userid = request.args.get('userid')

        print(starttime)

        # print(starttime + '-------' + endtime)
        condition = (1==1)
        if starttime is not None and endtime is not None:
            condition = and_(condition,EmployeeAttendanceModel.checktime.between(starttime,endtime))
            
        if userid is not None:
            condition = and_(condition,EmployeeAttendanceModel.userid==userid)
            
        emp = EmployeeAttendanceModel.query.filter(condition).all()

        result = []

        for e in emp:
            result.append({
                "id": e.id,
                "userid": e.userid,
                "username": e.username,
                "temperature": e.temperature,
                "checktime": e.checktime,
                "snid": e.snid,
                "snname": e.snname,
                "unname": e.unname
            })

        return jsonify(result)

    def post(self):
        req_data = request.json

        msg, code = None, None
        rmsg, rcode = None, None

        userid = req_data.get('ID')
        username = req_data.get('Name')
        checktime = req_data.get('Time')
        temperature = req_data.get('TP')
        snid = req_data.get('snid')
        snname = req_data.get('snname')
        unname = req_data.get('unname')
        # 0 upload successfully, 1 upload failed, 2 repeated data
        status = 0

        results = []

        # 根据设备snid从后台获取snname,unname
        dvc = EmployeeAttendanceDeviceModel.query.filter_by(snid=snid).first()

        if dvc is not None:
            snname = dvc.snname
            unname = dvc.unname
        else:
            return jsonify({
                "msg": "Failed to get attendance device!",
                "code": 5501
            })

        uchecktime = time.strftime("%Y-%m-%d %H:%M",time.strptime(checktime,"%Y/%m/%d %H:%M:%S.%f"))
        try:
            mssql = MSSQLServer(host="192.168.1.87",port=1433, username='hlcsykqehr', password='hlcsykqehr123.',database='zy_hlc',charset="utf8")
            sql = "select userid,checktime,jlzt,sn_id,sn_name,un_name  FROM checkinout_zy where userid='{0}' and format(checktime,'yyyy-MM-dd HH:mm')='{1}'".format(userid,uchecktime)
            results = mssql.select(sql)
            print(results)
        except Exception:
            rmsg, rcode = '', 5504
        
        if len(results)>0:
            status = 2
        else:
            try:
                mssql = MSSQLServer(host="192.168.1.87",port=1433, username='hlcsykqehr', password='hlcsykqehr123.',database='zy_hlc',charset="utf8")
                addsql = "insert into checkinout_zy(userid,checktime,sn_id,sn_name,un_name) values('{0}','{1}','{2}','{3}','{4}')".format(userid, checktime,snid,snname,unname)
                mssql.execute(addsql)
                rmsg, rcode = 'ok', 200
                status = 0
            except Exception:
                rmsg, rcode = 'Failed to add attendance data to remote', 5503
                status = 1

        emp_attend = EmployeeAttendanceModel(userid=userid, username=username, checktime=checktime, temperature=temperature,snid=snid,snname=snname,unname=unname,status=status)
        try:
            db.session.add(emp_attend)
            db.session.commit()
            msg, code = 'ok', 200
        except Exception:
            msg, code = 'Failed to add attendance data to local!', 5502
            db.session.rollback()

        return jsonify({"msg": msg,"code": code,"rmsg": rmsg,"rcode": rcode})


class EmployeeAttendanceDevice(Resource):
    def get(self):
        msg, code = 'ok', 200

        empdvc = EmployeeAttendanceDeviceModel.query.all()

        result = []

        for ed in empdvc:
            result.append({
                "id": ed.id,
                "snid": ed.snid,
                "snname": ed.snname,
                "unname": ed.unname,
                "ip": ed.ip,
                "created_timestamp": ed.created_timestamp
            })

        return jsonify(result)

    def post(self):
        req_data = request.json

        msg, code = 'ok', 200

        snid = req_data.get('snid')
        snname = req_data.get('snname')
        unname = req_data.get('unname')
        ip = req_data.get('ip')

        empdvc_attend = EmployeeAttendanceDeviceModel(snid=snid,snname=snname,unname=unname,ip=ip)

        try:
            db.session.add(empdvc_attend)
            db.session.commit()
            msg, code = 'ok', 200
        except Exception:
            msg, code = 'failed', 500
            db.session.rollback()

        return jsonify({"msg": msg,"code": code})
