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