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