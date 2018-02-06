#-*- encoding:utf-8 -*-
#2014-12-18
#author: orangleliu

import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop
import tornado-redis

class IndexPageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('templates/index.html')
class QuestionListhandler(tornado.web.RequestHandler):
    def get(self):
        self.write('{"code": "SUCCESS", "data": {"answerFalse": 0, "answerRight": 0, "countdown": 10, "integral": 0, "isover": 0, "options": [{"id": "A", "name": "65"}, {"id": "B", "name": "66"}, {"id": "C", "name": "68"} ], "title": "柯南道尔写了多少部侦探小说", "totalQuestion": 8, "uaId": "1691961"}, "msg": "成功"}')

class QuestionAnswerhandler(tornado.web.RequestHandler):
    def get(self):
        self.write('{"code": "SUCCESS", "data": {"answer": "C", "result": 0 }, "msg": "完成"}')


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        pass

    def on_message(self, message):
        self.write_message(u"Your message was: "+message)

    def on_close(self):
        pass

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', IndexPageHandler),
            (r'/ws', WebSocketHandler),
            (r'/question/answer', QuestionAnswerhandler),
            (r'/question/list', QuestionListhandler),
        ]

        settings = { "template_path": "."}
        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == '__main__':
    ws_app = Application()
    server = tornado.httpserver.HTTPServer(ws_app)
    server.listen(5000)
    print 'app is runing at 0.0.0.0:5000\nQuit the app with CONTROL-C'
    tornado.ioloop.IOLoop.instance().start()
