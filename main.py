from aiogram import Bot, Dispatcher,executor,types


bot = Bot('6636165347:AAHz2Zw-B_ibYi46fM1r870AlzsvXxMgmS0')
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def cmd_start(message:types.Message):
    await message.answer(f"{message.from_user.first_name}, добро пожаловать в KOPOSIARY - VAPE КИРОВ")



if __name__ == '__main__':
    executor.start_polling(dp)

