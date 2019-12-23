from tornado import web, ioloop
from tornado.options import define, options, parse_command_line

# define 定义一些可以在命令中传递的参数以及类型
define("port", default=8008, help="run on the given port", type=int)
define("debug", default=True, help="set tornado debug mode", type=bool)

# options.parse_command_line()
options.parse_config_file("conf.cfg")


# options是一个类， 全局只有一个options

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


if __name__ == '__main__':
    app = web.Application([
        ("/", MainHandler)
    ], debug=options.debug)

    app.listen(options.port)
    ioloop.IOLoop.current().start()
