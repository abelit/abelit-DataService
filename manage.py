# -*- encoding: utf-8 -*-
'''
@File    :   manage.py
@Time    :   2020/03/23 10:22:20
@Author  :   Abelit 
@Version :   1.0
@Contact :   ychenid@live.com
@Copyright :   (C)Copyright 2020, dataforum.org
@Licence :   BSD-3-Clause
@Desc    :   None
'''


from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from db import db

from main import create_app

app = create_app()

migrate = Migrate(app, db)
manager = Manager(app)

# 添加数据库迁移命令
manager.add_command('db', MigrateCommand)

# Add Custom Command
@manager.option("-n", "--name", dest="name", default="www.baidu.com")
def hello(name):
    print("hello world!")
    print(name)

@manager.option("-n", "--name", dest="name", default="www.baidu.com")
def world(name):
    print("haha")


if __name__ == '__main__':
    manager.run()
