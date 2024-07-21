import logging
import asyncio
from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from handlers import router


load_dotenv()

dp = Dispatcher()
TOKEN = getenv('BOT_TOKEN')


async def main():
    bot = Bot(token=TOKEN)
    dp.include_router(router=router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except:
        print('Exit')


