# MSSQL测试
SQLCMD.EXE -U hlcsykqehr -P ****** -S 192.168.1.87

```dotnetcli
CREATE TABLE `employee` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(200) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
`password` varchar(200) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `name` varchar(200) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `avatar` varchar(200) CHARACTER SET utf8 COLLATE utf8_bin,
`introduction` varchar(200) CHARACTER SET utf8 COLLATE utf8_bin,
`email` varchar(200) CHARACTER SET utf8 COLLATE utf8_bin,
`phone` varchar(200) CHARACTER SET utf8 COLLATE utf8_bin,
`roles` varchar(200) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `status` int NOT NULL,
  `created_timestamp` datetime NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=1276 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
```

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