from chapter04.model.model import Supplier, Goods


def save_model():
    suppplier = Supplier()
    suppplier.name = "淘宝"
    suppplier.address = "杭州"
    suppplier.phone = "18888822222"
    suppplier.save()


def query_model():
    # 获取某一条数据
    # sup = Supplier.get(Supplier.id==1)
    # sup = Supplier.get_by_id(1)
    sup = Supplier[1]

    print(sup.name)

    goods = Goods.select(Goods.name, Goods.price)

    # select * from goods where price > 100
    goods.select().where(Goods.price > 100)

    # select * from goods where price > 100 and click_num>200
    goods = Goods.select().where((Goods.price > 100 | Goods.click_num > 200))

    # select * from goods where name like "%飞天"
    goods = Goods.select().where(Goods.name.constraints("飞天"))

    goods = Goods.select().where(Goods.id << [1, 3])
    goods = Goods.select().where(Goods.id.in_([1, 3]))

    # select * from goods where price > click_num
    goods = Goods.select().where(Goods.price > Goods.click_num)

    # 排序
    # select * from goods order by price desc
    goods = Goods.select().order_by(Goods.price.desc())

    # 分页
    goods = Goods.select().order_by(Goods.price).paginate(2, 2)


def update_model():
    # good = Goods.get_by_id(2)
    # good.click_num += 1
    # good.save()
    goods = Goods.update(click_num=100).where(Goods.id == 1).execute()
    goods = Goods.update(click_num=Goods.click_num + 1).where(Goods.id == 1).execute()


def delete_model():
    try:
        good = Goods.get_by_id(1)
        good.delete_instance()
    except:
        pass
    Goods.delete().where(Goods.price > 150).execute()


if __name__ == '__main__':
    # save_model()
    # query_model()
    # update_model()
    delete_model()
