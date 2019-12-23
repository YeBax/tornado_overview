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


class PeopleIdHandler(web.RequestHandler):
    def initialize(self, name):
        self.db_name = name

    async def get(self, id, *args, **kwargs):
        self.write("用户ID：{}".format(id))
        # self.redirect(self.reverse_url("people_name", "bobby"))


class PeopleNameHandler(web.RequestHandler):
    async def get(self, id, *args, **kwargs):
        self.write("用户姓名：{}".format(id))


class PeopleInfoHandler(web.RequestHandler):
    async def get(self, id, name, age, gender, *args, **kwargs):
        self.write("用户姓名：{}\n年龄:{}\n性别:{}".format(name, age, gender))

peolpe_db = {
    "name":"people"

}

urls = [
    web.URLSpec("/", MainHandler, name="index"),
    web.URLSpec(r"/people/(\d+)/?", PeopleIdHandler, name="people_id"),
    web.URLSpec(r"/people/(\w+)/?", PeopleNameHandler, name="people_name"),
    # web.URLSpec(r"/people/(\w+)/(\d+)/(\w+)/?", PeopleInfoHandler, name="people_info"),
    web.URLSpec(r"/people/(?P<name>\w+)/(?P<age>\d+)/(?P<gender>\w+)/?", PeopleInfoHandler, name="people_info"),

]
if __name__ == '__main__':
    app = web.Application(urls, debug=True)

    app.listen(8888)
    ioloop.IOLoop.current().start()

# 1.url的各种参数配置
# 2.url命名 reverse_url
# 3.给handler传入初始值