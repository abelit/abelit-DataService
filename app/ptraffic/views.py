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
        min(xf_starthour)||':'||'00'||'-'||max(xf_starthour)||':'||'00' 时间段,
        nvl(sum(case
        when XF_CAMERAID in 
            ('GHGY5500033140','GHGY5500033141','GHGY5500033142','GHGY5500033143','GHGY5500033144','GHGY5500033147',
            'GHGY5500033155','GHGY5500033156','GHGY5500033157','GHGY5500033158','GHGY5500033159',
            'GHGY5500033169','GHGY5500033170','GHGY5500033171','GHGY5500033172','GHGY5500033173','GHGY5500033174','GHGY5500033168')
            then XF_INCOUNT  
            end),0) "沿湖广场",
        nvl(sum(case
        when XF_CAMERAID in 
            ('GHGY5500033026','GHGY5500033027','GHGY5500033028','GHGY5500033029','GHGY5500033030','GHGY5500033031','GHGY5500033032',
            'GHGY5500033089','GHGY5500033090','GHGY5500033091','GHGY5500033092','GHGY5500033093','GHGY5500033094','GHGY5500033095')
            then XF_INCOUNT 
            end),0) "H&M",
        nvl(sum(case
        when XF_CAMERAID in 
            ('GHGY5500033230','GHGY5500033229','GHGY5500033196','GHGY5500033197')
            then XF_INCOUNT  
            end),0) "人行天桥",
        nvl(sum(case
        when XF_CAMERAID in 
            ('GHGY5500033002','GHGY5500033003','GHGY5500033004','GHGY5500033005','GHGY5500033006','GHGY5500033007','GHGY5500033008','GHGY5500033009','GHGY5500033010',
            'GHGY5500033014','GHGY5500033015','GHGY5500033016','GHGY5500033017','GHGY5500033018')
            then XF_INCOUNT  
            end),0) "停车场",
        nvl(sum(case
        when XF_CAMERAID in
            ('GHGY5500033002','GHGY5500033003','GHGY5500033004','GHGY5500033005','GHGY5500033006','GHGY5500033007','GHGY5500033008','GHGY5500033009','GHGY5500033010',
            'GHGY5500033014','GHGY5500033015','GHGY5500033016','GHGY5500033017','GHGY5500033018',
            'GHGY5500033026','GHGY5500033027','GHGY5500033028','GHGY5500033029','GHGY5500033030','GHGY5500033031','GHGY5500033032',
            'GHGY5500033089','GHGY5500033090','GHGY5500033091','GHGY5500033092','GHGY5500033093','GHGY5500033094','GHGY5500033095',
            'GHGY5500033140','GHGY5500033141','GHGY5500033142','GHGY5500033143','GHGY5500033144','GHGY5500033147',
            'GHGY5500033155','GHGY5500033156','GHGY5500033157','GHGY5500033158','GHGY5500033159',
            'GHGY5500033169','GHGY5500033170','GHGY5500033171','GHGY5500033172','GHGY5500033173','GHGY5500033174','GHGY5500033168',
            'GHGY5500033230','GHGY5500033229','GHGY5500033196','GHGY5500033197')
            then XF_INCOUNT  
            end),0) "共计"
        from 
        xf_tc_countdata
        WHERE
        xf_starthour between 10 and 21 and
        to_date(XF_DATE_TIME,'yyyy-mm-dd') between to_date('{0}','yyyy-mm-dd') and to_Date('{1}','yyyy-mm-dd')
        """
    results = oracle.select(sql_text.format(starttime, endtime))

    data = []

    for row in results:
        print(row[1])
        data.append({
            "pdate": row[0],
            "psquare": row[1],
            "phm": row[2],
            "pgateway": row[3],
            "pparking": row[4],
            "pall": row[5]
        })

    return jsonify(data)