# -*- encoding: utf-8 -*-
'''
@File    :   views.py
@Time    :   2020/04/17 09:11:32
@Author  :   Abelit 
@Version :   1.0
@Contact :   ychenid@live.com
@Copyright :   (C)Copyright 2020, dataforum.org
@Licence :   BSD-3-Clause
@Desc    :   None
'''


from flask import Flask, Blueprint, jsonify, request
# Import module cx_Oracle to connect oracle using python
try:
    import cx_Oracle
except ImportError:
    cx_oracle_exists = False
else:
    cx_oracle_exists = True

ptraffic = Blueprint('ptraffic', __name__)


@ptraffic.route('/ping')
def ping():
    return jsonify({
        "ping": "Pong!",
        "ip": request.remote_addr,
        "router": request.path,
        "module": __name__
    })

class Oracle:
    def __init__(self, username, password, host, port, instance, mode):
        """
        Function: __init__
        Summary: InsertHere
        Examples: InsertHere
        Attributes:
            @param (self):InsertHere
            @param (*args):InsertHere
            username: oracle user,
            password: oracle user's password,
            mod:  "normal, sysdba, sysoper",defaut is normal,
            host: the oracle database locates
            port: the port listen oracle database service, config is 1521
            insrance: the service name of the oracle database instance
        Returns: InsertHere
        """
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.instance = instance
        self.mode = mode

    def __connect(self):
        """
        Function: __connect
        Summary: InsertHere
        Examples: self.__connect()
        Attributes:
            @param (self):Call __connect metod Oracle.__connect()
        Returns: connection
        """
        if not cx_oracle_exists:
            msg = """The cx_Oracle module is required. 'pip install cx_Oracle' \
                should do the trick. If cx_Oracle is installed, make sure ORACLE_HOME \
                & LD_LIBRARY_PATH is set"""

        dsn = cx_Oracle.makedsn(
            host=self.host, port=self.port, service_name=self.instance)

        try:
            if self.mode == 'sysdba' or self.username == 'sys':
                self.connection = cx_Oracle.connect(self.username, self.password, dsn,
                                                    mode=cx_Oracle.SYSDBA)
            else:
                self.connection = cx_Oracle.connect(
                    self.username, self.password, dsn)

        except cx_Oracle.DatabaseError as cx_msg:
            msg = 'Could not connect to database: %s, dsn: %s ' % (cx_msg, dsn)
        return self.connection

    def __disconnect(self):
        try:
            self.cursor.close()
            self.connection.close()
        except cx_Oracle.DatabaseError as cx_msg:
            print(cx_msg)

    def select(self, sql, bindvars=''):
        """
        Given a valid SELECT statement, return the results from the database
        """

        results = None

        try:
            self.__connect()
            self.cursor = self.connection.cursor()
            self.cursor.execute(sql, bindvars)
            results = self.cursor.fetchall()
        except cx_Oracle.DatabaseError as cx_msg:
            print(cx_msg)
        finally:
            self.__disconnect()
        return results

    def execute(self, sql, bindvars='', commit=True):
        """
        Function: execute
        Summary: Execute whatever SQL statements are passed to the method;
            commit if specified. Do not specify fetchall() in here as
            the SQL statement may not be a select.
            bindvars is a dictionary of variables you pass to execute.
        Examples: Oracle().execute(...)
        Attributes:
            @param (self):class method
            @param (sql):The sql that will be excuted
            @param (bindvars) config='': The bind variables of sql
            @param (many) config=False: If set many is True, multiple sql will be excuted at the same time
            @param (commit) config=False: False is not needed commit after excuting sql, but True is needed commit, gernerally DML sql
        Returns: NO value will be returned
        """

        try:
            self.__connect()
            self.cursor = self.connection.cursor()
            self.cursor.execute(sql, bindvars)
            print(
                "The sql executing from database successfully and the sql is " + '"' + sql + '".')
        except cx_Oracle.DatabaseError as cx_msg:
            print(cx_msg)
        finally:
            # Only commit if it-s necessary.
            if commit:
                self.connection.commit()
            else:
                pass
            self.__disconnect()


@ptraffic.route("/")
def get_passenger_traffic():
    starttime = request.args.get('start')
    endtime = request.args.get('end')

    if starttime is None:
        starttime = 0
    if endtime is None:
        endtime = 24
    oracle = Oracle(username='gdata', password='gdata',
                    mode="", host="10.50.0.212", port=1521, instance='gdata')
    sql_text = """select pdate,pentry,pin,pout,sysdate as gettime from (SELECT
        a.XF_DATE_TIME pdate,
        b.xf_passageway pentry,
            sum(a.xf_incount) pin,
            sum(a.xf_outcount) pout
        from 
        XF_new_TC_COUNTDATA a,
            XF_TC_PASS b 
        WHERE
        a.XF_CAMERAID=b.XF_CAMERAID and
        a.XF_CAMERAID NOT IN ('GHGY5500033011','GHGY5500033012','GHGY5500033013','GHGY5500033019','GHGY5500033020','GHGY5500033022','GHGY5500033023','GHGY5500033024','GHGY5500033025',
        'GHGY5500033033','GHGY5500033034','GHGY5500033035','GHGY5500033036','GHGY5500033040','GHGY5500033041','GHGY5500033042','GHGY5500033043','GHGY5500033046',
        'GHGY5500033047','GHGY5500033048','GHGY5500033049','GHGY5500033050','GHGY5500033051','GHGY5500033052','GHGY5500033053','GHGY5500033055','GHGY5500033056',
        'GHGY5500033057','GHGY5500033058','GHGY5500033059','GHGY5500033060','GHGY5500033061','GHGY5500033062','GHGY5500033073','GHGY5500033074','GHGY5500033076',
        'GHGY5500033077','GHGY5500033078','GHGY5500033082','GHGY5500033083','GHGY5500033084','GHGY5500033096','GHGY5500033097','GHGY5500033098','GHGY5500033099',
        'GHGY5500033100','GHGY5500033101','GHGY5500033104','GHGY5500033105','GHGY5500033106','GHGY5500033107','GHGY5500033108','GHGY5500033109','GHGY5500033110',
        'GHGY5500033111','GHGY5500033114','GHGY5500033117','GHGY5500033118','GHGY5500033119','GHGY5500033128','GHGY5500033133','GHGY5500033134','GHGY5500033135',
        'GHGY5500033138','GHGY5500033139','GHGY5500033145','GHGY5500033148','GHGY5500033149','GHGY5500033150','GHGY5500033151','GHGY5500033152','GHGY5500033153',
        'GHGY5500033162','GHGY5500033163','GHGY5500033175','GHGY5500033176','GHGY5500033177','GHGY5500033178','GHGY5500033181','GHGY5500033183','GHGY5500033184',
        'GHGY5500033185','GHGY5500033186','GHGY5500033187','GHGY5500033188','GHGY5500033189','GHGY5500033192','GHGY5500033193','GHGY5500033198','GHGY5500033199',
        'GHGY5500033200','GHGY5500033204','GHGY5500033205','GHGY5500033210','GHGY5500033211','GHGY5500033212','GHGY5500033213','GHGY5500033214','GHGY5500033215',
        'GHGY5500033216','GHGY5500033217','GHGY5500033218','GHGY5500033219','GHGY5500033220','GHGY5500033221','GHGY5500033228') AND
         to_date(a.XF_DATE_TIME,'yyyy-mm-dd') = to_date(to_char(sysdate,'yyyy-mm-dd'),'yyyy-mm-dd') and XF_STARTHOUR between {0} and {1}
        GROUP BY
        a.XF_DATE_TIME,b.xf_passageway
        order by a.XF_DATE_TIME)"""
    results = oracle.select(sql_text.format(starttime, endtime))

    data = []

    for row in results:
        print(row[1])
        data.append({
            "pdate": row[0],
            "pentry": row[1],
            "pin": row[2],
            "pout": row[3],
            "gettime": row[4]
        })

    return jsonify(data)


@ptraffic.route("/all")
def get_all_passenger_traffic():
    oracle = Oracle(username='gdata', password='gdata',
                    mode="", host="10.50.0.212", port=1521, instance='gdata')
    sql_text = """select pdate,pentry,pin,pout,sysdate as gettime from (SELECT
        a.XF_DATE_TIME pdate,
        b.xf_passageway pentry,
            sum(a.xf_incount) pin,
            sum(a.xf_outcount) pout
        from 
        XF_new_TC_COUNTDATA a,
            XF_TC_PASS b 
        WHERE
        a.XF_CAMERAID=b.XF_CAMERAID and
        a.XF_CAMERAID NOT IN ('GHGY5500033011','GHGY5500033012','GHGY5500033013','GHGY5500033019','GHGY5500033020','GHGY5500033022','GHGY5500033023','GHGY5500033024','GHGY5500033025',
        'GHGY5500033033','GHGY5500033034','GHGY5500033035','GHGY5500033036','GHGY5500033040','GHGY5500033041','GHGY5500033042','GHGY5500033043','GHGY5500033046',
        'GHGY5500033047','GHGY5500033048','GHGY5500033049','GHGY5500033050','GHGY5500033051','GHGY5500033052','GHGY5500033053','GHGY5500033055','GHGY5500033056',
        'GHGY5500033057','GHGY5500033058','GHGY5500033059','GHGY5500033060','GHGY5500033061','GHGY5500033062','GHGY5500033073','GHGY5500033074','GHGY5500033076',
        'GHGY5500033077','GHGY5500033078','GHGY5500033082','GHGY5500033083','GHGY5500033084','GHGY5500033096','GHGY5500033097','GHGY5500033098','GHGY5500033099',
        'GHGY5500033100','GHGY5500033101','GHGY5500033104','GHGY5500033105','GHGY5500033106','GHGY5500033107','GHGY5500033108','GHGY5500033109','GHGY5500033110',
        'GHGY5500033111','GHGY5500033114','GHGY5500033117','GHGY5500033118','GHGY5500033119','GHGY5500033128','GHGY5500033133','GHGY5500033134','GHGY5500033135',
        'GHGY5500033138','GHGY5500033139','GHGY5500033145','GHGY5500033148','GHGY5500033149','GHGY5500033150','GHGY5500033151','GHGY5500033152','GHGY5500033153',
        'GHGY5500033162','GHGY5500033163','GHGY5500033175','GHGY5500033176','GHGY5500033177','GHGY5500033178','GHGY5500033181','GHGY5500033183','GHGY5500033184',
        'GHGY5500033185','GHGY5500033186','GHGY5500033187','GHGY5500033188','GHGY5500033189','GHGY5500033192','GHGY5500033193','GHGY5500033198','GHGY5500033199',
        'GHGY5500033200','GHGY5500033204','GHGY5500033205','GHGY5500033210','GHGY5500033211','GHGY5500033212','GHGY5500033213','GHGY5500033214','GHGY5500033215',
        'GHGY5500033216','GHGY5500033217','GHGY5500033218','GHGY5500033219','GHGY5500033220','GHGY5500033221','GHGY5500033228') AND
         to_date(a.XF_DATE_TIME,'yyyy-mm-dd') = to_date(to_char(sysdate,'yyyy-mm-dd'),'yyyy-mm-dd')
        GROUP BY
        a.XF_DATE_TIME,b.xf_passageway
        order by a.XF_DATE_TIME)"""
    results = oracle.select(sql_text)

    data = []

    for row in results:
        print(row[1])
        data.append({
            "pdate": row[0],
            "pentry": row[1],
            "pin": row[2],
            "pout": row[3],
            "gettime": row[4]
        })

    return jsonify(data)



@ptraffic.route("/time")
def get_time_passenger_traffic():
    starttime = request.args.get('start')
    endtime = request.args.get('end')

    if starttime is None:
        starttime = 0
    if endtime is None:
        endtime = 24
    oracle = Oracle(username='gdata', password='gdata',
                    mode="", host="10.50.0.212", port=1521, instance='gdata')
    sql_text = """SELECT
     to_date(xf_tc_countdata.XF_DATE_TIME,'yyyy-mm-dd') pdate,
        min(xf_tc_countdata.xf_starthour)||':'||'00'||'-'||max(xf_tc_countdata.xf_starthour)||':'||'00' ptime,
        nvl(sum(case
        when xf_tc_pass.xf_pass_no in 
            (7,8,9)
            then XF_INCOUNT  
            end),0) "沿湖广场",
        nvl(sum(case
        when xf_tc_pass.xf_pass_no in 
            (4,5)
            then XF_INCOUNT 
            end),0) "HM",
        nvl(sum(case
        when xf_tc_pass.xf_pass_no in 
            (11)
            then XF_INCOUNT  
            end),0) "人行天桥(乐转旁)",
        nvl(sum(case
        when xf_tc_pass.xf_pass_no in 
            (12)
            then XF_INCOUNT  
            end),0) "人行天桥(必胜客旁)",
        nvl(sum(case
        when xf_tc_pass.xf_pass_no in 
            (2)
            then XF_INCOUNT  
            end),0) "肯德基",
        nvl(sum(case
        when xf_tc_pass.xf_pass_no in 
            (3)
            then XF_INCOUNT  
            end),0) "黔宝金店旁",
                    nvl(sum(case
        when xf_tc_pass.xf_pass_no in 
            (10)
            then XF_INCOUNT  
            end),0) "食尚汇门厅旁",
                    nvl(sum(case
        when xf_tc_pass.xf_pass_no in 
            (6)
            then XF_INCOUNT  
            end),0) "CKJeans旁",
        nvl(sum(case
        when xf_tc_pass.xf_pass_no in 
            (1)
            then XF_INCOUNT  
            end),0) "停车场",
        nvl(sum(case
        when xf_tc_pass.xf_pass_no in
            (1,2,4,5,7,8,9,10,11,12)
            then XF_INCOUNT  
            end),0) "共计"
        from
        xf_tc_countdata,xf_tc_pass
        WHERE
        xf_tc_countdata.xf_cameraid=xf_tc_pass.xf_cameraid and
        xf_tc_countdata.xf_starthour between 10 and 21 and
        to_date(xf_tc_countdata.XF_DATE_TIME,'yyyy-mm-dd') between to_date('{0}','yyyy-mm-dd') and to_Date('{1}','yyyy-mm-dd')
        group by  to_date(xf_tc_countdata.XF_DATE_TIME,'yyyy-mm-dd') order by 1
        """
    results = oracle.select(sql_text.format(starttime, endtime))

    data = []

    for row in results:
        print(row[1])
        data.append({
            "pdate": row[0],
            "ptime": row[1],
            "psquare": row[2],
            "phm": row[3],
            "pgateway": row[4],
            "pgatewaypiz": row[5],
            "pkfc": row[6],
            "pqbj": row[7],
            "prest": row[8],
            "pck": row[9],
            "pparking": row[10],
            "pall": row[11]
        })

    return jsonify(data)



@ptraffic.route("/date")
def get_date_passenger_traffic():
    starttime = request.args.get('start')
    endtime = request.args.get('end')

    if starttime is None:
        starttime = 0
    if endtime is None:
        endtime = 24
    oracle = Oracle(username='gdata', password='gdata',
                    mode="", host="10.50.0.212", port=1521, instance='gdata')
    sql_text = """SELECT
     to_date(xf_tc_countdata.XF_DATE_TIME,'yyyy-mm-dd') pdate,
        min(xf_tc_countdata.xf_starthour)||':'||'00'||'-'||max(xf_tc_countdata.xf_starthour)||':'||'00' ptime,
        nvl(sum(case
        when xf_tc_pass.xf_pass_no in 
            (7,8,9)
            then XF_INCOUNT  
            end),0) "沿湖广场",
        nvl(sum(case
        when xf_tc_pass.xf_pass_no in 
            (4,5)
            then XF_INCOUNT 
            end),0) "HM",
        nvl(sum(case
        when xf_tc_pass.xf_pass_no in 
            (11)
            then XF_INCOUNT  
            end),0) "人行天桥(乐转旁)",
        nvl(sum(case
        when xf_tc_pass.xf_pass_no in 
            (12)
            then XF_INCOUNT  
            end),0) "人行天桥(必胜客旁)",
        nvl(sum(case
        when xf_tc_pass.xf_pass_no in 
            (2)
            then XF_INCOUNT  
            end),0) "肯德基",
        nvl(sum(case
        when xf_tc_pass.xf_pass_no in 
            (3)
            then XF_INCOUNT  
            end),0) "黔宝金店旁",
                    nvl(sum(case
        when xf_tc_pass.xf_pass_no in 
            (10)
            then XF_INCOUNT  
            end),0) "食尚汇门厅旁",
                    nvl(sum(case
        when xf_tc_pass.xf_pass_no in 
            (6)
            then XF_INCOUNT  
            end),0) "CKJeans旁",
        nvl(sum(case
        when xf_tc_pass.xf_pass_no in 
            (1)
            then XF_INCOUNT  
            end),0) "停车场",
        nvl(sum(case
        when xf_tc_pass.xf_pass_no in
            (1,2,4,5,7,8,9,10,11,12)
            then XF_INCOUNT  
            end),0) "共计"
        from
        xf_tc_countdata,xf_tc_pass
        WHERE
        xf_tc_countdata.xf_cameraid=xf_tc_pass.xf_cameraid and
        xf_tc_countdata.xf_starthour between 10 and 21 and
        to_date(xf_tc_countdata.XF_DATE_TIME,'yyyy-mm-dd') between to_date('{0}','yyyy-mm-dd') and to_Date('{1}','yyyy-mm-dd')
        group by  to_date(xf_tc_countdata.XF_DATE_TIME,'yyyy-mm-dd') order by 1
        """
    results = oracle.select(sql_text.format(starttime, endtime))

    data = []

    for row in results:
        print(row[1])
        data.append({
            "pdate": row[0],
            "ptime": row[1],
            "psquare": row[2],
            "phm": row[3],
            "pgateway": row[4],
            "pgatewaypiz": row[5],
            "pkfc": row[6],
            "pqbj": row[7],
            "prest": row[8],
            "pck": row[9],
            "pparking": row[10],
            "pall": row[11]
        })

    return jsonify(data)

@ptraffic.route("/compare")
def get_compare_passenger_traffic():
    """
    API: http://58.42.231.98:5060/api/ptraffic/compare
    参数（可选）: sart（开始日期）, end (结束日期)
    说明：
    "pdate": "日期",
    "psquare": 沿湖广场,
    "psquare_last": 沿湖广场去年同期,
    "phm": HM,
    "phm_last": HM去年同期,
    "pgateway_lz": 人行天桥(乐转旁),
    "pgateway_lz_last": 人行天桥(乐转旁)去年同期,
    "pgateway_b": 人行天桥(必胜客旁),
    "pgateway_b_last": 人行天桥(必胜客旁)去年同期,
    "pkfc": 肯德基,
    "pkfc_last": 肯德基去年同期,
    "pqbj": 黔宝金店旁,
    "pqbj_last": 黔宝金店旁去年同期,
    "prest": 食尚汇门厅旁,
    "prest_last": 食尚汇门厅旁去年同期,
    "pck": CKJeans旁,
    "pck_last": CKJeans旁去年同期,
    "ppark": 停车场,
    "ppark_last": 停车场去年同期,
    "pall": 总计,
    "pall_last": 总计（上一年）

    示例: http://58.42.231.98:5060/api/ptraffic/compare?start=2020-07-01&end=2020-07-02

    """
    import time
    starttime = request.args.get('start')
    endtime = request.args.get('end')

    if starttime is None:
        starttime = time.strftime("%Y-%m-%d", time.localtime())
    if endtime is None:
        endtime = time.strftime("%Y-%m-%d", time.localtime())
    oracle = Oracle(username='gdata', password='gdata',
                    mode="", host="10.50.0.212", port=1521, instance='gdata')
    sql_text = """select to_char(a.pdate, 'yyyy-mm-dd') pdate,a.yh psquare,nvl(b.yh,0) psquare_last,a.hm phm,nvl(b.hm,0) phm_last,a.lz pgateway_lz,nvl(b.lz,0) pgateway_lz_last,
            a.bsk pgateway_b,nvl(b.bsk,0) pgateway_b_last,a.kfc pkfc,nvl(b.kfc,0) pkfc_last,a.QBJD pqbj,nvl(b.qbjd,0) pqbj_last,
            a.ssh prest,nvl(b.ssh,0) prest_last,a.ck pck,nvl(b.ck,0) pck_last,a.tcc ppark,nvl(b.tcc,0) ppark_last,a.al pall,nvl(b.al,0) pall_last
            from 
        (SELECT
            to_date(xf_tc_countdata.XF_DATE_TIME,'yyyy-mm-dd') pdate,
                --min(xf_tc_countdata.xf_starthour)||':'||'00'||'-'||max(xf_tc_countdata.xf_starthour+1)||':'||'00' ptime,
                nvl(sum(case
                when xf_tc_pass.xf_pass_no in 
                    (7,8,9)
                    then XF_INCOUNT  
                    end),0) YH,
                nvl(sum(case
                when xf_tc_pass.xf_pass_no in 
                    (4,5)
                    then XF_INCOUNT 
                    end),0) HM,
                nvl(sum(case
                when xf_tc_pass.xf_pass_no in 
                    (11)
                    then XF_INCOUNT  
                    end),0) LZ,
                nvl(sum(case
                when xf_tc_pass.xf_pass_no in 
                    (12)
                    then XF_INCOUNT  
                    end),0) BSK,
                nvl(sum(case
                when xf_tc_pass.xf_pass_no in 
                    (2)
                    then XF_INCOUNT  
                    end),0) KFC,
                nvl(sum(case
                when xf_tc_pass.xf_pass_no in 
                    (3)
                    then XF_INCOUNT  
                    end),0) QBJD,
                            nvl(sum(case
                when xf_tc_pass.xf_pass_no in 
                    (10)
                    then XF_INCOUNT  
                    end),0) SSH,
                            nvl(sum(case
                when xf_tc_pass.xf_pass_no in 
                    (6)
                    then XF_INCOUNT  
                    end),0) CK,
                nvl(sum(case
                when xf_tc_pass.xf_pass_no in 
                    (1)
                    then XF_INCOUNT  
                    end),0) TCC,
                nvl(sum(case
                when xf_tc_pass.xf_pass_no in
                    (1,2,3,4,5,6,7,8,9,10,11,12)
                    then XF_INCOUNT  
                    end),0) AL
                from
                xf_tc_countdata,xf_tc_pass
                WHERE
                xf_tc_countdata.xf_cameraid=xf_tc_pass.xf_cameraid and
                --xf_tc_countdata.xf_starthour between 10 and 21 and
                xf_tc_countdata.XF_DATE_TIME between '{0}' and '{1}'
                group by  to_date(xf_tc_countdata.XF_DATE_TIME,'yyyy-mm-dd')) a,
        (SELECT
            to_date(substr(xf_tc_countdata.XF_DATE_TIME,1,4)+1||'-'||substr(xf_tc_countdata.XF_DATE_TIME,6,2)||'-'||substr(xf_tc_countdata.XF_DATE_TIME,9,2),'yyyy-mm-dd') s_pdate,
            -- substr(xf_tc_countdata,1,4)-1||'-'||substr(xf_tc_countdata,6,2)||'-'||substr(xf_tc_countdata,9,2),'yyyy-mm-dd'
                --min(xf_tc_countdata.xf_starthour)||':'||'00'||'-'||max(xf_tc_countdata.xf_starthour+1)||':'||'00' ptime,
                nvl(sum(case
                when xf_tc_pass.xf_pass_no in 
                    (7,8,9)
                    then XF_INCOUNT  
                    end),0) YH,
                nvl(sum(case
                when xf_tc_pass.xf_pass_no in 
                    (4,5)
                    then XF_INCOUNT 
                    end),0) HM,
                nvl(sum(case
                when xf_tc_pass.xf_pass_no in 
                    (11)
                    then XF_INCOUNT  
                    end),0) LZ,
                nvl(sum(case
                when xf_tc_pass.xf_pass_no in 
                    (12)
                    then XF_INCOUNT  
                    end),0) BSK,
                nvl(sum(case
                when xf_tc_pass.xf_pass_no in 
                    (2)
                    then XF_INCOUNT  
                    end),0) KFC,
                nvl(sum(case
                when xf_tc_pass.xf_pass_no in 
                    (3)
                    then XF_INCOUNT  
                    end),0) QBJD,
                            nvl(sum(case
                when xf_tc_pass.xf_pass_no in 
                    (10)
                    then XF_INCOUNT  
                    end),0) SSH,
                            nvl(sum(case
                when xf_tc_pass.xf_pass_no in 
                    (6)
                    then XF_INCOUNT  
                    end),0) CK,
                nvl(sum(case
                when xf_tc_pass.xf_pass_no in 
                    (1)
                    then XF_INCOUNT  
                    end),0) TCC,
                nvl(sum(case
                when xf_tc_pass.xf_pass_no in
                    (1,2,3,4,5,6,7,8,9,10,11,12)
                    then XF_INCOUNT  
                    end),0) AL
                from
                xf_tc_countdata,xf_tc_pass
                WHERE
                xf_tc_countdata.xf_cameraid=xf_tc_pass.xf_cameraid and
                --xf_tc_countdata.xf_starthour between 10 and 21 and
                xf_tc_countdata.XF_DATE_TIME between 
                substr('{0}',1,4)-1||'-'||substr('{0}',6,2)||'-'||substr('{0}',9,2) and 
                substr('{1}',1,4)-1||'-'||substr('{1}',6,2)||'-'||substr('{1}',9,2)
                group by  xf_tc_countdata.XF_DATE_TIME) b
        where a.pdate=b.s_pdate(+)
        order by a.pdate
        """
    results = oracle.select(sql_text.format(starttime, endtime))

    data = []

    for row in results:
        print(row[1])
        data.append({
            "pdate": row[0],
            "psquare": row[1],
            "psquare_last": row[2],
            "phm": row[3],
            "phm_last": row[4],
            "pgateway_lz": row[5],
            "pgateway_lz_last": row[6],
            "pgateway_b": row[7],
            "pgateway_b_last": row[8],
            "pkfc": row[9],
            "pkfc_last": row[10],
            "pqbj": row[11],
            "pqbj_last": row[12],
            "prest": row[13],
            "prest_last": row[14],
            "pck": row[15],
            "pck_last": row[16],
            "ppark": row[17],
            "ppark_last": row[18],
            "pall": row[19],
            "pall_last": row[20]
        })

    return jsonify(data)

@ptraffic.route("/traffics")
def get_traffics():
    import datetime
    starttime = request.args.get('start')
    endtime = request.args.get('end')

    if starttime is None:
        # 当月第一天
        starttime = datetime.datetime.strftime(datetime.datetime(datetime.datetime.now().year,datetime.datetime.now().month,1),'%Y-%m-%d')
    if endtime is None:
        endtime = datetime.datetime.strftime(datetime.datetime.now()-datetime.timedelta(days=1),'%Y-%m-%d')
    oracle = Oracle(username='gdata', password='gdata',
                    mode="", host="10.50.0.212", port=1521, instance='gdata')

    sql_text = """
        select sum(XF_INCOUNT) as nums from xf_tc_countdata where xf_cameraid in ( select xf_cameraid from xf_tc_pass) and XF_DATE_TIME between '{0}' and '{1}'
    """    
    alltraffics = oracle.select(sql_text.format(starttime, endtime))
    daytraffics = oracle.select(sql_text.format(endtime, endtime))
    data = {}

    data["alltraffics"] =  alltraffics[0][0]
    data["daytraffics"] =  daytraffics[0][0]

    return jsonify(data)

@ptraffic.route("/sales")
def get_sales():
    import datetime
    starttime = request.args.get('start')
    endtime = request.args.get('end')

    if starttime is None:
        # 当月第一天
        starttime = datetime.datetime.strftime(datetime.datetime(datetime.datetime.now().year,datetime.datetime.now().month,1),'%Y-%m-%d')
    if endtime is None:
        endtime = datetime.datetime.strftime(datetime.datetime.now()-datetime.timedelta(days=1),'%Y-%m-%d')

    oracle = Oracle(username='gl_mis', password='garland123321mis',
                    mode="", host="10.10.10.20", port=1521, instance='garland.org')

    sale_sql = """
    select sum(gw_salesamount) as total, sum(case when  type=1 and gw_state in (1,2) then gw_salesamount else 0 end) as pos,sum(case when  not (type=1 and gw_state in (1,2)) then gw_salesamount else 0 end) nonpos  from gw_transsalestotal where gw_txdate between '{0}' and '{1}'
    """

    pos_sql = """
    select m_type as postype, count(1) as posnum from tmp_posinstall group by m_type
    """

    posusage_sql = """
    select count(distinct cashier_code) as posusage  from gw_transsalestotal where gw_txdate between '{0}' and '{1}' and type=1 and gw_state in (1,2)
    """

    inputsale_sql = """
    SELECT
    A.TENANTCODE,
	A.TENANTNAME,
	A.STORECODE,
	A.STORENAME
    FROM
        gl_biapi.MIS_STOREINFO A JOIN
    gl_biapi.V_SETTLE_R20 B ON A.MALL_ID = B.MALL_ID AND A.CONTRACTCODE = B.CONTRACTCODE
    WHERE B.ACCOUNT_PAYABLE BETWEEN REPLACE(substr('{0}',0,7),'-','') AND REPLACE(substr('{1}',0,7),'-','') and a.storecode not in (select shops_code from gl_merchant.GW_SALE_DATA where sale_date='{1}')
    """

    data = {}

    sales = oracle.select(sale_sql.format(starttime,endtime))
    pos = oracle.select(pos_sql.format(starttime,endtime))
    posusage = oracle.select(posusage_sql.format(starttime,endtime))
    inputsale = oracle.select(inputsale_sql.format(starttime,endtime))

    tmpres = []
    for row in inputsale:
        tmpres.append({
            "mcode": row[0],
            "mname": row[1],
            "scode": row[2],
            "sname": row[3]
        })

    data["totalsale"] = sales[0][0]
    data["possale"] = sales[0][1]
    data["posw280p"] = pos[0][1]
    data["posa8"] = pos[1][1]
    data["posusage"] = posusage[0][0]
    data["inputsale"] = tmpres


    return jsonify(data)


# @ptraffic.route("/date")
# def get_date_passenger_traffic():
#     starttime = request.args.get('start')
#     endtime = request.args.get('end')

#     if starttime is None:
#         starttime = 0
#     if endtime is None:
#         endtime = 24
#     oracle = Oracle(username='gdata', password='gdata',
#                     mode="", host="10.50.0.212", port=1521, instance='gdata')
#     sql_text = """SELECT
#      to_date(XF_DATE_TIME,'yyyy-mm-dd') pdate,
#         min(xf_starthour)||':'||'00'||'-'||max(xf_starthour)||':'||'00' ptime,
#         nvl(sum(case
#         when XF_CAMERAID in 
#             ('GHGY5500033140','GHGY5500033141','GHGY5500033142','GHGY5500033143','GHGY5500033144','GHGY5500033147',
#             'GHGY5500033155','GHGY5500033156','GHGY5500033157','GHGY5500033158','GHGY5500033159',
#             'GHGY5500033169','GHGY5500033170','GHGY5500033171','GHGY5500033172','GHGY5500033173','GHGY5500033174','GHGY5500033168')
#             then XF_INCOUNT  
#             end),0) "沿湖广场",
#         nvl(sum(case
#         when XF_CAMERAID in 
#             ('GHGY5500033026','GHGY5500033027','GHGY5500033028','GHGY5500033029','GHGY5500033030','GHGY5500033031','GHGY5500033032',
#             'GHGY5500033089','GHGY5500033090','GHGY5500033091','GHGY5500033092','GHGY5500033093','GHGY5500033094','GHGY5500033095')
#             then XF_INCOUNT 
#             end),0) "HM",
#         nvl(sum(case
#         when XF_CAMERAID in 
#             ('GHGY5500033203')
#             then XF_INCOUNT  
#             end),0) "人行天桥",
#         nvl(sum(case
#         when XF_CAMERAID in 
#             ('GHGY5500033002','GHGY5500033003','GHGY5500033004','GHGY5500033005','GHGY5500033006','GHGY5500033007','GHGY5500033008','GHGY5500033009','GHGY5500033010',
#             'GHGY5500033014','GHGY5500033015','GHGY5500033016','GHGY5500033017','GHGY5500033018')
#             then XF_INCOUNT  
#             end),0) "停车场",
#         nvl(sum(case
#         when XF_CAMERAID in
#             ('GHGY5500033203','GHGY5500033002','GHGY5500033003','GHGY5500033004','GHGY5500033005','GHGY5500033006','GHGY5500033007','GHGY5500033008'
# ,'GHGY5500033009','GHGY5500033010','GHGY5500033014','GHGY5500033015','GHGY5500033016','GHGY5500033017','GHGY5500033018','GHGY5500033026'
# ,'GHGY5500033027','GHGY5500033028','GHGY5500033029','GHGY5500033030','GHGY5500033031','GHGY5500033032','GHGY5500033089','GHGY5500033090'
# ,'GHGY5500033091','GHGY5500033092','GHGY5500033093','GHGY5500033094','GHGY5500033095','GHGY5500033140','GHGY5500033141','GHGY5500033142'
# ,'GHGY5500033143','GHGY5500033144','GHGY5500033147','GHGY5500033155','GHGY5500033156','GHGY5500033157','GHGY5500033158','GHGY5500033159'
# ,'GHGY5500033169','GHGY5500033170','GHGY5500033171','GHGY5500033172','GHGY5500033173','GHGY5500033174','GHGY5500033168')
#             then XF_INCOUNT  
#             end),0) "共计"
#         from 
#         xf_tc_countdata
#         WHERE
#         xf_starthour between 10 and 21 and
#         to_date(XF_DATE_TIME,'yyyy-mm-dd') between to_date('{0}','yyyy-mm-dd') and to_Date('{1}','yyyy-mm-dd')
#         group by  to_date(XF_DATE_TIME,'yyyy-mm-dd')
#         """
#     results = oracle.select(sql_text.format(starttime, endtime))

#     data = []

#     for row in results:
#         print(row[1])
#         data.append({
#             "pdate": row[0],
#             "ptime": row[1],
#             "psquare": row[2],
#             "phm": row[3],
#             "pgateway": row[4],
#             "pparking": row[5],
#             "pall": row[6]
#         })

#     return jsonify(data)
