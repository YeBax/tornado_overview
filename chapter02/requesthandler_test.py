from tornado import web, ioloop
from tornado.web import RequestHandler

import json

class MainHandler(RequestHandler):
    # 入口
    # def initialize(self, db) -> None:
    #     # 用于初始化handler类的过程
    #     self.db = db

    def prepare(self):
        # prepare 方法用于真正调用求情处理之前的初始化方法
        # 1.打印日志, 打开文件
        pass

    def on_finish(self) -> None:
        # 关闭句柄，清理内存
        pass

    # http方法
    def get(self, *args, **kwargs):
        data1 = self.get_query_argument("name")  # 多个name，取最后一个
        data2 = self.get_query_arguments("name")  # 获取全部的name值，一个list
        data3 = self.get_argument("name")
        data4 = self.get_arguments("name")
        pass

    # 输入的方法
    def post(self, *args, **kwargs):
        data_all = self.request.arguments  # 所有的参数
        data1 = self.get_argument("name")
        data2 = self.get_arguments("name")
        # data_body1 = self.get_body_argument("name")
        # data_body2 = self.get_body_arguments("name")
        param = self.request.body.decode("utf8")
        data_json = json.loads(param)
        data_json_name = data_json["name"]
        data_heard = self.request.headers
        pass

    def delete(self, *args, **kwargs):
        pass

    def put(self):
        self.write("hello")
        self.flush()
        self.write("world")
        self.finish("put")
        self.redirect("") # 页面跳转
        self.write_error(500) # 自定义返回的错误页面

    def write_error(self, status_code: int, **kwargs) -> None:
        pass

    # 输出:
    # set_status, write, finish, redirect, write_error





urls = [
    web.URLSpec("/", MainHandler, name="index"),
]
if __name__ == '__main__':
    app = web.Application(urls, debug=True)

    app.listen(8888)
    ioloop.IOLoop.current().start()
