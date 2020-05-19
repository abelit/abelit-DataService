# abelit-DataService

# API
```bash
 curl http://127.0.0.1:5000/api/employee/attend -X POST -d '{"ID": 110142, "Name": "陈英", "TP": 36.51, "Time": "2020-04-08"}' --header "Content-Type: application/json"
```

# Run
```bash
 python3 manage.py runserver -h 0.0.0.0 -p 5060
 & 
 python3 main.py
```

# API

```
http://localhost:5060/api/employee/attend
POST:


GET:


http://localhost:5060/api/employee/device
POST:
{
	"snid": "23423dfa5462345",
	"snname": "花果园购物中心1",
	"unname": "宏立城商业集团"
}

GET:
[
    {
        "id": 1,
        "snid": "23423dfa5462345",
        "snname": "花果园购物中心1",
        "unname": "宏立城商业集团",
        "created_timestamp": "Wed, 15 Apr 2020 15:28:11 GMT"
    },
    {
        "id": 2,
        "snid": "23423dfa5462345",
        "snname": "花果园购物中心1",
        "unname": "宏立城商业集团",
        "created_timestamp": "Wed, 15 Apr 2020 15:36:26 GMT"
    }
]
```


# Python Oracle
```bash
#.bash_rc
export ORACLE_HOME=/opt/oracle/instantclient_12_2
export TNS_ADMIN=$ORACLE_HOME/network/admin
export NLS_LANG="SIMPLIFIED CHINESE_CHINA.ZHS16GBK"
export LD_LIBRARY_PATH=$ORACLE_HOME:$LD_LIBRARY_PATH
```

# Deploy
## Windows Server: Nginx+Flask+Tornado

### 1. Install Nginx on Windows Server


### 2. wsgi server: tornado as wsgi
```python
# runservice.py
from tornado.httpserver import HTTPServer
from tornado.wsgi import WSGIContainer
from main import app
from tornado.ioloop import IOLoop

s = HTTPServer(WSGIContainer(app))
# 监听 9900 端口
s.listen(5060)
IOLoop.current().start()
```

### 3. Nginx Configuration
```conf
http {   
    server {
        listen       80;
        server_name  localhost;
        server_name  127.0.0.1;     
        charset     utf-8;           

        location / {
            root   html;
            index  index.html index.htm;
            proxy_pass  http://localhost:9900;
        }
        # other configurations
    }
}
```


## Windows Server: IIS+wFastCGI

#### D:\App\abelit-DataService-master\web.config
```xml
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <system.webServer>
    <handlers>
      <add name="PythonFastCGI" path="*" verb="*" modules="FastCgiModule"
        scriptProcessor="c:\python37\python.exe|c:\python37\lib\site-packages\wfastcgi.py"
        resourceType="Unspecified" requireAccess="Script" />
    </handlers>
  </system.webServer>
  <appSettings>
    <!-- Required settings -->
    <add key="PYTHONPATH" value="D:\App\abelit-DataService-master" />
    <add key="WSGI_HANDLER" value="main.app" />
    <add key="WSGI_LOG" value="D:\logs\web.log" />
  </appSettings>
</configuration>
```

- 注意事项： 1. python需要安装到"C:\Python37"且为全局安装; 2. 日志目录需要提前创建，但具体的日志文件不能预先建立。