from flask import Flask, Blueprint, jsonify, request
from flask_restful import Api, Resource,request

from models import GiftCardModel, ShopCardModel, ActivityParticipantModel
from db import db
import time

feedback = Blueprint('feedback', __name__)

api = Api(feedback)


@feedback.route('/ping')
def ping():
    return jsonify({
        "ping": "Pong!",
        "ip": request.remote_addr,
        "router": request.path,
        "module": __name__
    })


# curl http://localhost:5000/todo1 -d "data=Remember the milk" -X PUT
# curl http://localhost:5000/todo1

class GiftCardResource(Resource):
    def get(self):
        gift = GiftCardModel.query.all()

        result = []
        
        for g in gift:
            result.append({
                "title_confirmdate": g.title_confirmdate,
                "base_brdname": g.base_brdname,
                "base_shopno": g.base_shopno,
                "base_company": g.base_company,
                "base_expiredate": g.base_expiredate,

                "mem_check": g.mem_check,
                "mem_silverdiscount": g.mem_silverdiscount,
                "mem_diamonddiscount": g.mem_diamonddiscount,
                "mem_gloddiscount": g.mem_gloddiscount,
                "mem_other": g.mem_other,

                "sign_signature": g.sign_signature,
                "sign_contact": g.sign_contact,
                "sign_call": g.sign_call,
                "sign_email": g.sign_email,
                "sign_replydate": g.sign_replydate,
            })

        return  jsonify(result)

    def post(self):
        req = request.json

        code = 200
        msg = "ok"

        # print(req.get('username'))
        # pass
        title_confirmdate = req.get('title_confirmdate')

        base_brdname = req.get('base_brdname')
        base_shopno = req.get('base_shopno')
        base_company = req.get('base_company')
        base_expiredate = req.get('base_expiredate')

        mem_check = req.get('mem_check')
        mem_silverdiscount = req.get('mem_silverdiscount')
        mem_diamonddiscount = req.get('mem_diamonddiscount')
        mem_gloddiscount = req.get('mem_gloddiscount')
        mem_other = req.get('mem_other')

        sign_signature = req.get('sign_signature')
        sign_contact = req.get('sign_contact')
        sign_call = req.get('sign_call')
        sign_email = req.get('sign_email')
        sign_replydate = req.get('sign_replydate')
        

        gift = GiftCardModel(title_confirmdate=title_confirmdate,base_brdname=base_brdname,base_shopno=base_shopno,
        base_company=base_company,base_expiredate=base_expiredate,mem_check=mem_check,mem_silverdiscount=mem_silverdiscount,mem_diamonddiscount=mem_diamonddiscount,
        mem_gloddiscount=mem_gloddiscount,mem_other=mem_other,sign_signature=sign_signature,sign_contact=sign_contact,sign_call=sign_call,sign_email=sign_email,
        sign_replydate=sign_replydate)

        try:
            db.session.add(gift)
            db.session.commit()
            msg = "ok"
            code = 200
        except Exception:
            msg = "failed"
            code = 500
            db.session.rollback()

        return jsonify({"msg": msg,"code": code})


    def put(self, id):
        return {}

class ShopCardResource(Resource):
    def get(self):
        shop = ShopCardModel.query.all()

        result = []
        
        for s in shop:
            result.append({
                "title_confirmdate": s.title_confirmdate,
                "title_vipperson": s.title_vipperson,
                "title_vipemail": s.title_vipemail,
                "title_viptel": s.title_viptel,

                "base_brdname": s.base_brdname,
                "base_shopno": s.base_shopno,
                "base_company": s.base_company,

                "spcard_check": s.spcard_check,
                "spcard_shopmall": s.spcard_shopmall,
                # "spcard_dolphin": s.spcard_dolphin,
                # "spcard_gyint": s.spcard_gyint,

                "remark_policy": s.remark_policy,
                "remark_contact": s.remark_contact,

                "sign_signature": s.sign_signature,
                "sign_contact": s.sign_contact,
                "sign_call": s.sign_call,
                "sign_email": s.sign_email,
                "sign_replydate": s.sign_replydate,
            })

        return  jsonify(result)


    def post(self):
        req = request.json

        code = 200
        msg = "ok"

        # print(req.get('username'))
        # pass
        title_confirmdate = req.get('title_confirmdate')
        title_vipperson = req.get('title_vipperson')
        title_vipemail = req.get('title_vipemail')
        title_viptel = req.get('title_viptel')

        base_brdname = req.get('base_brdname')
        base_shopno = req.get('base_shopno')
        base_company = req.get('base_company')

        spcard_check = req.get('spcard_check')
        spcard_shopmall = req.get('spcard_shopmall')
        # spcard_dolphin = req.get('spcard_dolphin')
        # spcard_gyint = req.get('spcard_gyint')

        remark_policy = req.get('remark_policy')
        remark_contact = req.get('remark_contact')

        sign_signature = req.get('sign_signature')
        sign_contact = req.get('sign_contact')
        sign_call = req.get('sign_call')
        sign_email = req.get('sign_email')
        sign_replydate = req.get('sign_replydate')
        
        print(type(str(spcard_shopmall)))

        shop = ShopCardModel(title_confirmdate=title_confirmdate,title_vipperson=title_vipperson,title_vipemail=title_vipemail,title_viptel=title_viptel,
        base_brdname=base_brdname,base_shopno=base_shopno,base_company=base_company,spcard_check=spcard_check,spcard_shopmall=str(spcard_shopmall),
        remark_policy=remark_policy,remark_contact=remark_contact,sign_signature=sign_signature,
        sign_contact=sign_contact,sign_call=sign_call,sign_email=sign_email,sign_replydate=sign_replydate)

        try:
            db.session.add(shop)
            db.session.commit()
            msg = "ok"
            code = 200
        except Exception as e:
            print(e)
            msg = "failed"
            code = 500
            db.session.rollback()

        return jsonify({"msg": msg,"code": code})

    def put(self, id):
        return {}


"""
gift card: 
    新增数据：
    api: /api/feedback/gift
    method: POST

    查询数据
    api: /api/feedback/gift
    method: GET

shop card: 
    新增数据：
    api: /api/feedback/shop
    method: POST

    查询数据
    api: /api/feedback/shop
    method: GET
"""

class GiftCardResource(Resource):
    def get(self):
        gift = GiftCardModel.query.all()

        result = []
        
        for g in gift:
            result.append({
                "title_confirmdate": g.title_confirmdate,
                "base_brdname": g.base_brdname,
                "base_shopno": g.base_shopno,
                "base_company": g.base_company,
                "base_expiredate": g.base_expiredate,

                "mem_check": g.mem_check,
                "mem_silverdiscount": g.mem_silverdiscount,
                "mem_diamonddiscount": g.mem_diamonddiscount,
                "mem_gloddiscount": g.mem_gloddiscount,
                "mem_other": g.mem_other,

                "sign_signature": g.sign_signature,
                "sign_contact": g.sign_contact,
                "sign_call": g.sign_call,
                "sign_email": g.sign_email,
                "sign_replydate": g.sign_replydate,
            })

        return  jsonify(result)

    def post(self):
        req = request.json

        code = 200
        msg = "ok"

        # print(req.get('username'))
        # pass
        title_confirmdate = req.get('title_confirmdate')

        base_brdname = req.get('base_brdname')
        base_shopno = req.get('base_shopno')
        base_company = req.get('base_company')
        base_expiredate = req.get('base_expiredate')

        mem_check = req.get('mem_check')
        mem_silverdiscount = req.get('mem_silverdiscount')
        mem_diamonddiscount = req.get('mem_diamonddiscount')
        mem_gloddiscount = req.get('mem_gloddiscount')
        mem_other = req.get('mem_other')

        sign_signature = req.get('sign_signature')
        sign_contact = req.get('sign_contact')
        sign_call = req.get('sign_call')
        sign_email = req.get('sign_email')
        sign_replydate = req.get('sign_replydate')
        

        gift = GiftCardModel(title_confirmdate=title_confirmdate,base_brdname=base_brdname,base_shopno=base_shopno,
        base_company=base_company,base_expiredate=base_expiredate,mem_check=mem_check,mem_silverdiscount=mem_silverdiscount,mem_diamonddiscount=mem_diamonddiscount,
        mem_gloddiscount=mem_gloddiscount,mem_other=mem_other,sign_signature=sign_signature,sign_contact=sign_contact,sign_call=sign_call,sign_email=sign_email,
        sign_replydate=sign_replydate)

        try:
            db.session.add(gift)
            db.session.commit()
            msg = "ok"
            code = 200
        except Exception:
            msg = "failed"
            code = 500
            db.session.rollback()

        return jsonify({"msg": msg,"code": code})


    def put(self, id):
        return {}
        
class ActivityParticipant(Resource):
    def get(self):
        activity = ActivityParticipantModel.query.all()

        result = []
        
        for a in activity:
            result.append({
                "name": a.name,
                "phone": a.phone,
                "signdate": a.signdate,
                "label": a.label,
                "servertime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            })

        return  jsonify(result)

    def post(self):
        req = request.json

        code = 200
        msg = "ok"

        name = req.get('name')
        phone = req.get('phone')
        signdate = req.get('signdate')
        label = req.get('label')

        act = ActivityParticipantModel(name=name, phone=phone, signdate=signdate, label=label)

        try:
            db.session.add(act)
            db.session.commit()
            msg = "ok"
            code = 200
        except Exception:
            msg = "failed"
            code = 500
            db.session.rollback()

        data = {"msg": msg,"code": code,"servertime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}
        # return jsonify(data),code

        return data,code


    def put(self):
        req = request.json
        msg, code = "ok", 200
        
        try:
            for p in req['phone_arr']:
                act = ActivityParticipantModel.query.filter_by(phone=p).first()
                act.label = 1
                db.session.add(act)
                db.session.commit()
            msg = "ok"
            code = 200
        except Exception:
            msg = "failed"
            code = 500
            db.session.rollback()
            
        data = {"msg": msg,"code": code, "servertime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) }
        return data,code

    """
    API: 
        URL: http://127.0.0.1:5060/api/feedback/activity
            POST:
                {
                    "name": "Abelit",
                    "phone": "15285649896",
                    "label": 1
                }
            GET:
    """