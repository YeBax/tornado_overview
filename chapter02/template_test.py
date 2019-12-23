from tornado import web, ioloop, template
from tornado.web import StaticFileHandler


class MainHandler(web.RequestHandler):
    # 当客户端发起不同的http方法的时候，只需要重载 handler中的对应方法即可
    async def get(self, *args, **kwargs):
        # web框架 都会有模版功能
        word = "hello tornado"

        # t = template.Template("<h1>{{ word }}</h1>")
        loader = template.Loader(r"E:\tornado_overview\chapter02\templates")
        # self.write(loader.load("hello.html").generate(word=word)) # 了解就行了
        orders = [{
            "name":"",
            "image":"",
            "price":39,
            "nums":3
        }]
        self.render("index.html")


class MainHandler2(web.RequestHandler):
    # 当客户端发起不同的http方法的时候，只需要重载 handler中的对应方法即可
    async def get(self, *args, **kwargs):
        self.write("hello word3")


settings = {
    "static_path": r"E:\tornado_overview\chapter02\static",
    "static_url_prefix": "/static/",
    "template_path": "templates",
}

if __name__ == '__main__':
    app = web.Application([
        ("/", MainHandler),
        # ("/static/(.*)", StaticFileHandler, {"path": r"E:\tornado_overview\chapter02\templates"})

    ], debug=True, **settings)

    app.listen(8888)
    ioloop.IOLoop.current().start()
