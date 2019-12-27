from peewee import *
from peewee import Model

import datetime

db = MySQLDatabase(
    host='172.17.209.30',
    port=3306,
    user="sunmengzi",
    password="LASO_sunmengzi",
    database="webserver"
)


class BaseModel(Model):
    add_time = DateTimeField(default=datetime.datetime.now, verbose_name="添加时间")

    class Meta:
        database = db


class Supplier(BaseModel):
    name = CharField(max_length=100, verbose_name="名称", index=True)
    address = CharField(max_length=100, verbose_name="联系地址")
    phone = CharField(max_length=11, verbose_name="联系方式")

    class Meta:
        table_name = "supplier"


class Goods(BaseModel):
    supplier = ForeignKeyField(Supplier, verbose_name="商家", backref="goods")
    name = CharField(max_length=100, index=True, verbose_name="商品名称", help_text="名称哦")
    click_num = IntegerField(default=0, verbose_name="点击数")
    goods_num = IntegerField(default=0, verbose_name="库存数")
    price = FloatField(default=0.0, verbose_name="价格")
    brief = TextField(verbose_name="商品介绍")
    birthday = DateField()

    class Meta:
        table_name = "goods"


db.create_tables([Goods, Supplier])
