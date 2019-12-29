from tornado import web, ioloop, template
from tornado.web import StaticFileHandler
import aiomysql

from chapter05.forms import MessageForm
from chapter05.model.model import Message


class MainHandler(web.RequestHandler):
    def initialize(self, db):
        self.db = db

    async def get(self, *args, **kwargs):
        message_form = MessageForm()
        self.render("message.html", message_form = message_form)

    async def post(self, *args, **kwargs):
        message_form = MessageForm(self.request.arguments)
        if message_form.validate():
            name = message_form.data
            email = message_form.data
            address = message_form.data
            message_data = message_form.data

            message = Message(name=name, email=email, address=address, message=message_data)
            message.save()

            self.render("message.html", message_form=message_form)

        else:
            self.render("message.html", message_form=message_form)

    async def put(self, *args, **kwargs):
        pass


settings = {
    "static_path": r"E:\tornado_overview\chapter03\static",
    "static_url_prefix": "/static/",
    "template_path": "templates",
    "db": {
        "host": 'cdh3',
        "port": 3306,
        "user": 'sunmengzi',
        "password": 'sunmengzi',
        "db": 'data_webserver',
        "charset": "utf8"
    }
}

if __name__ == '__main__':
    app = web.Application([
        ("/", MainHandler, {"db": settings["db"]}),
        # ("/static/(.*)", StaticFileHandler, {"path": r"E:\tornado_overview\chapter03\templates"})

    ], debug=True, **settings)

    app.listen(8889)
    ioloop.IOLoop.current().start()
