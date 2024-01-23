from aiogram import Bot, Dispatcher,executor,types
from dotenv import load_dotenv
import os,sys,time

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAAMOZbAIb3rH_mjDy3qqud_Soxkw4FcAAqkYAAIjdeBJmzhaCBy9ZUs0BA')
    await message.answer(f"{message.from_user.first_name}, добро пожаловать в KOPOSIARY - VAPE КИРОВ")

@dp.message_handler(content_types=['photo','text','document','voice','video','animation','sticker'])
async def forward_message(message: types.Message):
    await bot.forward_message(os.getenv('GROUP_ID'), message.from_user.id, message.message_id)

if __name__ == '__main__':
    start_time = time.time()
    executor.start_polling(dp,skip_updates=True)
    print("--- %s seconds ---" % (time.time() - start_time))
