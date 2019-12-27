import asyncio
import aiomysql
import tornado.ioloop


async def test_example():
    pool = await aiomysql.create_pool(host='cdh3', port=3306,
                                      user='sunmengzi', password='sunmengzi',
                                      db='data_webserver', charset="utf8")
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT name from message;")
            print(cur.description)
            (msg,) = await cur.fetchone()
            print(msg)
            # assert r == 42
    pool.close()
    await pool.wait_closed()

if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(test_example(loop))
    io_loop = tornado.ioloop.IOLoop.current()
    io_loop.run_sync(test_example)
