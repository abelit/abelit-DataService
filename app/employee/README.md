# MSSQL测试
SQLCMD.EXE -U hlcsykqehr -P ****** -S 192.168.1.87

# API
## 1. Device

url: /api/employee/device

format: json

method:

- GET：获取设备信息
- POST：添加设备信息
- PUT：更新设备信息
- DELETE：删除设备信息

parameter:



demo:

http://localhost:5060/api/employee/device


response:

```dotnetcli

```


## 2. Attendance

url: /api/employee/attend

format: json

method:

- GET：获取打卡信息
- POST：添加打卡信息

parameter:



demo:

http://localhost:5060/api/employee/attend


response:

```dotnetcli

```