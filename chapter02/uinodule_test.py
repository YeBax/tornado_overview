from tornado import web, ioloop, template
from tornado.web import StaticFileHandler


class OrderModule(web.UIModule):
    def cal_total(self, price, nums):
        return price * nums

    def render(self, order, *args, **kwargs):
        return self.render_string("ui_modules/order-list.html", order=order, cal_total=self.cal_total)

    # def embedded_css(self):
    #     return "body {background-color:green}"

    def css_files(self):
        return ["ui_modules/order-list.css"]


class MainHandler(web.RequestHandler):
    # 当客户端发起不同的http方法的时候，只需要重载 handler中的对应方法即可
    async def get(self, *args, **kwargs):
        # web框架 都会有模版功能
        word = "hello tornado"

        # t = template.Template("<h1>{{ word }}</h1>")
        loader = template.Loader(r"E:\tornado_overview\chapter02\templates")
        # self.write(loader.load("hello.html").generate(word=word)) # 了解就行了
        orders = [{
            "name": "小米T恤 忍者米兔双截棍 军绿 XXL",
            "image": "http://i1.mifile.cn/a1/T11lLgB5YT1RXrhCrK!40x40.jpg",
            "price": 0,
            "nums": 2
        },
            {
                "name": "小米T恤 忍者米兔双截棍 军绿 XXL",
                "image": "http://i1.mifile.cn/a1/T11lLgB5YT1RXrhCrK!40x40.jpg",
                "price": 39,
                "nums": 3
            },
            {
                "name": "招财猫米兔 白色",
                "image": "http://i1.mifile.cn/a1/T14BLvBKJT1RXrhCrK!40x40.jpg",
                "price": 49,
                "nums": 2
            },
            {
                "name": "小米圆领纯色T恤 男款 红色 XXL",
                "image": "http://i1.mifile.cn/a1/T1rrDgB4DT1RXrhCrK!40x40.jpg",
                "price": 59,
                "nums": 2
            }
        ]
        self.render("index2.html", orders=orders)


class MainHandler2(web.RequestHandler):
    # 当客户端发起不同的http方法的时候，只需要重载 handler中的对应方法即可
    async def get(self, *args, **kwargs):
        self.write("hello word3")


settings = {
    "static_path": r"E:\tornado_overview\chapter02\static",
    "static_url_prefix": "/static/",
    "template_path": "templates",
    "ui_modules":{
        "OrderModule":OrderModule
    }
}

if __name__ == '__main__':
    app = web.Application([
        ("/", MainHandler),
        # ("/static/(.*)", StaticFileHandler, {"path": r"E:\tornado_overview\chapter02\templates"})

    ], debug=True, **settings)

    app.listen(8889)
    ioloop.IOLoop.current().start()
