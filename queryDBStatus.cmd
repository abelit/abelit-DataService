echo %date% -- %time% >> queryDBStatus.log
SQLCMD.EXE -U hlcsykqehr -P hlcsykqehr123. -S 192.168.1.87 -Q "select 1" >> queryDBStatus.log

curl http://localhost:5060/api/scheduler/add