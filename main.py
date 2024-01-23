from aiogram import Bot, Dispatcher,executor,types
from dotenv import load_dotenv
from aiogram.types import ReplyKeyboardMarkup,InlineKeyboardMarkup,InlineKeyboardButton
import os,sys,time


load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)


main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('Каталог').add('Контакты')


admin = ReplyKeyboardMarkup(resize_keyboard=True)
admin.add('Каталог').add('Контакты').add('БО$$')


admin_panel = ReplyKeyboardMarkup(resize_keyboard=True)
admin_panel.add('Добавить товар').add('Удалить товар').add('Рассылка')


@dp.message_handler(commands = ['start'])
async def cmd_start(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAAMOZbAIb3rH_mjDy3qqud_Soxkw4FcAAqkYAAIjdeBJmzhaCBy9ZUs0BA')
    await message.answer(f'{message.from_user.first_name}, добро пожаловать в KOPOSIARY - VAPE КИРОВ', reply_markup=main)
    if message.from_user.id == int(os.getenv('ADMIN_ID')) or int(os.getenv('ADMIN_ID2')):
        await message.answer(f'Вы авторизованы как админ!', reply_markup=admin)


@dp.message_handler(commands = ['YaTojePidor'])
async def cmd_id(message: types.Message):
    await message.answer(f'{message.from_user.id}')


@dp.message_handler(text = 'Каталог')
async def catalog(message: types.Message):
    await message.answer(f'У нас нихуя нет, все вопросы и жалобы ему - @vountmama')


@dp.message_handler(text = 'Контакты')
async def contacts(message: types.Message):
    await message.answer(f'Он пидор, пиши ему - @vountmama')


@dp.message_handler(text = 'БО$$')
async def boss(message: types.Message):
    if message.from_user.id == int(os.getenv('ADMIN_ID')) or int(os.getenv('ADMIN_ID2')):
        await message.answer_sticker(f'CAACAgIAAxkBAANWZbAkTclvEYsjODKALD8pl4pzhXUAAgMBAAJlogMssyhwGWhp1Z00BA')
        await message.answer(f'Ты админ, поздравляю!', reply_markup=admin_panel)
    else:
        await message.answer(f'Сори, ты не админ :(')


@dp.message_handler(content_types = ['photo','text','document','voice','video','animation','sticker'])
async def forward_message(message: types.Message):
    await bot.forward_message(os.getenv('GROUP_ID'), message.from_user.id, message.message_id)


if __name__ == '__main__':
    start_time = time.time()
    executor.start_polling(dp, skip_updates=True)
    print("--- %s seconds ---" % (time.time() - start_time))
