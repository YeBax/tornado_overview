import asyncio
from chapter04.model.async_model import Goods, Supplier
from chapter04.model.async_model import objects
import tornado.ioloop


async def handler():
    # await objects.create(Goods, supplier_id=1, name="53度茅台",
    #                      click_num=20, goods_nums=100, price=500, brief="贵州茅台酒厂")
    all_objects = await objects.execute(Supplier.select())
    for obj in all_objects:
        print(obj.name)


loop = asyncio.get_event_loop()
loop.run_until_complete(handler())
# io_loop = tornado.ioloop.IOLoop.current()
# io_loop.run_sync(handler)
# loop.close()

# # Clean up, can do it sync again:
# with objects.allow_sync():
#     Supplier.drop_table(True)
