# 1.什么是协程
# 1.回调过深造成代码很难维护
# 2.栈撕裂造成异常无法向上抛出
# 协程，可被暂停并且切换到其他的协程运行的函数
from tornado.gen import coroutine

# 两种协程的写法，一种装饰器，一种3.6之后的原生的写法，推荐async

# @coroutine
# def yield_test():
#     yield 1
#     yield 2
#     yield 3
#
#     yield from yield_test()
#
#     return "hello"

async def yield_test():
    yield 1
    yield 2
    yield 3

async def main():
    # await 只能写在 async下面
    await yield_test()

async def main2():
    # await 只能写在 async下面
    # 按顺序执行，上面 遇到暂停，就进入此处的 await
    await yield_test()


my_yield = yield_test()
for item in my_yield:
    print(item)
