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

if __name__ == '__main__':
    app = web.Application([
        ("/", MainHandler)
    ], debug=True)

    app.listen(8888)
    ioloop.IOLoop.current().start()
