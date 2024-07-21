import re
from aiogram.types import Message, FSInputFile
from aiogram import Router
from download import upload
from aiogram.filters import CommandStart


router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer('Привет чтобы скачать видео с видео хостинга YouTube отправь мне URL адресс этого видео.')

@router.message()
async def get_url(message: Message):
    text = message.text
    if not re.search(r'^https://(www\.youtube\.com|youtu\.be)/', text):
        await message.reply("Пожалуйста введите верную ссылку на ролик")
        return
    answer = await message.answer('Минутку...')

    try:
        result = upload(text)
        await message.answer_video(video=FSInputFile(result), caption="Ваше видео готово!")
        await answer.delete()
    except:
        await answer.delete()   
        await message.answer('Проблема с сервисом')