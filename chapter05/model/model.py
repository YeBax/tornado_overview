from datetime import datetime

from peewee import *
from peewee import Model
import peewee_async

db = MySQLDatabase()


class Message(Model):
    id = AutoField()
    name = CharField(max_length=10, verbose_name="姓名")
    email = CharField(max_length=10, verbose_name="邮箱")
    address = CharField(max_length=10, verbose_name="地址")
    message = TextField(verbose_name="留言")

    class Meta:
        datebase = db
        table_name = "message"
