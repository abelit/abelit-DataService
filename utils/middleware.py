# -*- encoding: utf-8 -*-
'''
@File    :   middleware.py
@Time    :   2020/03/21 08:31:04
@Author  :   Abelit
@Version :   1.0
@Contact :   ychenid@live.com
@Copyright :   (C)Copyright 2020, dataforum.org
Licence :   BSD-3-Clause
@Desc    :   None
'''


class Middleware(object):
    def __init__(self, wsgi_app, request, *args):
        self.wsgi_app = wsgi_app
        self.requst = request
        print("初始化...")

    def __call__(self, *args, **kwargs):
        print("开始...")
        ret = self.wsgi_app(*args, **kwargs)
        print("结束...")
        return ret


class PermissionMiddleware(Middleware):
    def __init__(self, name):
        super().__init__()
        self.name = name
