import pymssql

from collections.abc import Iterable
print(isinstance('abc', Iterable))

class MSSQLServer:
    def __init__(self, username, password, host, port, database, charset="utf8"):
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
            charset: the database characterset
        Returns: InsertHere
        """
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.charset = charset

    def __connect(self):
        """
        Function: __connect
        Summary: InsertHere
        Examples: self.__connect()
        Attributes:
            @param (self):Call __connect metod Oracle.__connect()
        Returns: connection
        """

        try:
            self.connection = pymssql.connect(host=self.host,port=self.port, user=self.username, password=self.password,database=self.database,charset=self.charset)
            print("ok")
        except Exception as cx_msg:
            msg = 'Could not connect to database: %s' % (cx_msg)
            raise Exception(msg)
        return self.connection

    def __disconnect(self):
        try:
            self.cursor.close()
            self.connection.close()
        except Exception as cx_msg:
            print(cx_msg)
            raise Exception(cx_msg)

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
            print("data ok")
        except Exception as cx_msg:
            print(cx_msg)
            raise Exception(cx_msg)
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
            print("The sql executing from database successfully and the sql is " + '"' + sql + '".')
        except Exception as cx_msg:
            print(cx_msg)
            raise Exception(cx_msg)
        finally:
            # Only commit if it-s necessary.
            if commit:
                self.connection.commit()
                print("commit ....")
            else:
                pass
            self.__disconnect()

if __name__ == "__main__":
    mssql = MSSQLServer(host="192.168.1.87",port=1433, username='hlcsykqehr', password='hlcsykqehr123.',database='zy_hlc',charset="utf8")
    sql = "select userid,checktime,jlzt,sn_id,sn_name,un_name  FROM checkinout_zy where userid='110142'"
    sql1 = "insert into checkinout_zy(userid,checktime,sn_id,sn_name,un_name) values('{0}','{1}','{2}','{3}','{4}')".format('110142','2020-04-21 12:10:00','test001','test','test')

    # print(sql1)
    # mssql.execute(sql1)

    results = mssql.select(sql)
    print(len(results))
