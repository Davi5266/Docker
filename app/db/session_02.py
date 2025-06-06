import asyncio

from sqlalchemy.ext.asyncio import create_async_engine


async def async_main():
    engine = create_async_engine(
        "postgresql+asyncpg://datauser:123456789@localhost/meubanco",
        echo=True,
    )

    async with engine.begin() as conn:
        await conn.run_sync(meta.drop_all)
        await conn.run_sync(meta.create_all)

        await conn.execute(
            t1.insert(), [{"name": "some name 1"}, {"name": "some name 2"}]
        )

    async with engine.connect() as conn:
        # select a Result, which will be delivered with buffered
        # results
        result = await conn.execute(select(t1).where(t1.c.name == "some name 1"))

        print(result.fetchall())

    # for AsyncEngine created in function scope, close and
    # clean-up pooled connections
    await engine.dispose()


asyncio.run(async_main())
