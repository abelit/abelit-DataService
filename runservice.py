from tornado.httpserver import HTTPServer
from tornado.wsgi import WSGIContainer
from main import app
from tornado.ioloop import IOLoop

s = HTTPServer(WSGIContainer(app))
# 监听 5060 端口
s.listen(5060)
IOLoop.current().start()