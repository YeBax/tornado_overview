from tornado import web, ioloop, template
from tornado.web import StaticFileHandler
import aiomysql


class MainHandler(web.RequestHandler):
    def initialize(self, db):
        self.db = db

    async def get(self, *args, **kwargs):
        id = ""
        name = ""
        email = ""
        address = ""
        message = ""

        async with await aiomysql.create_pool(**self.db) as pool:
            async with pool.acquire() as conn:
                async with conn.cursor() as cur:
                    await cur.execute("SELECT id, name, email, address, message from message;")
                    print(cur.description)
                    try:
                        id, name, email, address, message = await cur.fetchone()
                    except:
                        pass
        self.render("message.html", id=id, name=name, email=email, address=address, message=message)

    async def post(self, *args, **kwargs):
        id = self.get_body_argument("id")
        name = self.get_body_argument("name")
        email = self.get_body_argument("email")
        address = self.get_body_argument("address")
        message = self.get_body_argument("message")

        async with await aiomysql.create_pool(**self.db) as pool:
            async with pool.acquire() as conn:
                async with conn.cursor() as cur:
                    if not id:
                        await cur.execute(
                            "insert into message(name,email, address, message) VALUES('{}','{}','{}','{}')".format(name,
                                                                                                                   email,
                                                                                                                   address,
                                                                                                                   message))
                    else:
                        await cur.execute(
                            "update message set name='{}', email='{}', address='{}', message='{}' where id={}".format(
                                name, email, address, message, id))
                    await conn.commit()
        self.render("message.html", name=name, email=email, address=address, message=message)


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
