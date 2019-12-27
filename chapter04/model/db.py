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


if __name__ == '__main__':
    # save_model()
    query_model()
