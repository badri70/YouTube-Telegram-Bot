import logging
import asyncio
from aiogram import Bot, Dispatcher
import conf
from handlers import router


dp = Dispatcher()
         
         
async def main():
    bot = Bot(token=conf.BOT_TOKEN)
    dp.include_router(router=router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except:
        print("Exit")

