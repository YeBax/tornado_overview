from tornado.web import StaticFileHandler, RedirectHandler

# 1.RedirectHandler
# 301是永久重定向，302是临时重定向，获取用户个人信息

# 2.StaticFileHandler

from tornado import web, ioloop


class MainHandler(web.RequestHandler):
    # 当客户端发起不同的http方法的时候，只需要重载 handler中的对应方法即可
    async def get(self, *args, **kwargs):
        self.write("hello word3")

    def post(self, *args, **kwargs):
        pass

    def put(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass


class MainHandler2(web.RequestHandler):
    # 当客户端发起不同的http方法的时候，只需要重载 handler中的对应方法即可
    async def get(self, *args, **kwargs):
        self.write("hello word3")


settings = {
    "static_path": "",
    "static_url_prefix": "/static/"
}

if __name__ == '__main__':
    app = web.Application([
        ("/", MainHandler),
        ("/2/", RedirectHandler, {"url": "/"})

    ], debug=True, **settings)

    app.listen(8888)
    ioloop.IOLoop.current().start()

# self.redirect 方法和 RedirectHandler方法 区别是什么
# self.redirect业务逻辑的重定向，临时性的
# RedirectHandler方法 永久性的
