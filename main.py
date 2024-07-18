import asyncio
import re
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import conf
from download import upload


dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Привет чтобы скачать видео с видео хостинга YouTube отправь мне URL адресс этого видео.')

@dp.message()
async def get_url(message: types.Message):
    text = message.text
    if not re.search(r'^https://(www\.youtube\.com|youtu\.be)/', text):
        await message.reply("Пожалуйста введите верную ссылку на ролик")
        return
    answer = await message.answer('Минутку...')

    try:
        result = upload(text)
        await message.answer_video(video=types.FSInputFile(result), caption="Ваше видео готово!")
        await answer.delete()
    except:
        await answer.delete()   
        await message.answer('Проблема с сервисом')
         
async def main():
    bot = Bot(token=conf.BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

