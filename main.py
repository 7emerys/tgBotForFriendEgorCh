from aiogram import Bot, Dispatcher,executor,types
from dotenv import load_dotenv
from app import keyboards as kb
from app import bossCommand
from app import sellersCommand
import os,sys,time
from app import database as db
import asyncio


load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)


async def on_startup(_):
    await db.db_start()


@dp.message_handler(commands = ['start'])
async def cmd_start(message: types.Message):
    await db.cmd_db_start(message.from_user.id)
    await message.answer_sticker('CAACAgIAAxkBAAMOZbAIb3rH_mjDy3qqud_Soxkw4FcAAqkYAAIjdeBJmzhaCBy9ZUs0BA')
    await message.answer(f'{message.from_user.first_name}, добро пожаловать в KOPOSIARY - VAPE КИРОВ', reply_markup=kb.main)
    if message.from_user.id == int(os.getenv('ADMIN_ID')) or int(os.getenv('ADMIN_ID2')):
        await message.answer(f'Вы авторизованы как админ!', reply_markup=kb.admin)

#дописать условие что чел должен иметь ранг чтобы ему отвечал бот
@dp.message_handler(commands=['sellers_help'])
async def sellsHelp_command(message: types.Message):
    if message.from_user.id==message.chat.id:
        await bot.send_message(chat_id=message.from_user.id,
                               text=sellersCommand.HELP_COMMAND_SELLERS,
                               parse_mode='HTML')
    else:
        new_msg = await message.reply("Пользуйтесь ботом в личных сообщениях!\n"
                                      "Сообщение удалиться через <b>5 секунд!</b>",
                                      parse_mode='HTML')
        await asyncio.sleep(5)
        try:
            await new_msg.delete()
            await message.delete()
        except Exception as e:
            pass


@dp.message_handler(commands=['boss_help'])
async def sellsHelp_command(message: types.Message):
    if message.from_user.id==message.chat.id:
        await bot.send_message(chat_id=message.from_user.id,
                               text=bossCommand.HELP_COMMAND_BOSS,
                               parse_mode='HTML')
    else:
        new_msg = await message.reply("Пользуйтесь ботом в личных сообщениях!\n"
                                      "Сообщение удалиться через <b>5 секунд!</b>",
                                      parse_mode='HTML')
        await asyncio.sleep(5)
        try:
            await new_msg.delete()
            await message.delete()
        except Exception as e:
            pass



@dp.message_handler(commands = ['YaTojePidor'])
async def cmd_id(message: types.Message):
    await message.answer(f'{message.from_user.id}')


@dp.message_handler(text = 'Каталог')
async def catalog(message: types.Message):
    await message.answer(f'Что вы хотите приобрести', reply_markup=kb.catalog_panel)


@dp.message_handler(text = 'Жидкость')
async def Liquids(message: types.Message):
    await message.answer(f'Что вы хотите приобрести', reply_markup=kb.Liquids_list)


@dp.message_handler(text = 'Электронные сигареты')
async def Electronic_cigarettes(message: types.Message):
    await message.answer(f'Что вы хотите приобрести?', reply_markup=kb.electronic_cigarettes_panel)


@dp.message_handler(text = 'Под')
async def Pod(message: types.Message):
    await message.answer(f'Какой под вы хотите приобрести?', reply_markup=kb.Pod_list)


@dp.message_handler(text = 'Одноразка')
async def One_size_fits_all(message: types.Message):
    await message.answer(f'Какую одноразку вы хотите приобрести?', reply_markup=kb.One_size_fits_all_list)

@dp.message_handler(text='Расходники')
async def Consumables(message: types.Message):
    await message.answer(f'Что из расходников вы хотите приобрести?', reply_markup=kb.Consumables_list)


@dp.message_handler(text = 'Контакты')
async def contacts(message: types.Message):
    await message.answer(f'Наши представители - @koposyara и @EgorCh17. Также подписывайтесь на нашу оффициальную группу - https://t.me/KOPOSIARY')


@dp.message_handler(text = 'БО$$')
async def boss(message: types.Message):
    if message.from_user.id == int(os.getenv('ADMIN_ID')) or int(os.getenv('ADMIN_ID2')):
        await message.answer_sticker(f'CAACAgIAAxkBAANWZbAkTclvEYsjODKALD8pl4pzhXUAAgMBAAJlogMssyhwGWhp1Z00BA')
        await message.answer(f'Ты админ, поздравляю!', reply_markup=kb.admin_panel)
    else:
        await message.answer(f'Сори, ты не админ :(')


@dp.message_handler(text = 'Добавить товар')
async def plus(message: types.Message):
    await message.answer(f'Какой товар хочешь?')


@dp.message_handler(text = 'Удалить товар')
async def minus(message: types.Message):
    await message.answer(f'Какой товар хочешь удалить?')


@dp.message_handler(text = 'Рассылка')
async def mailing(message: types.Message):
    await message.answer(f'Гл.пидор - @vountmama')


@dp.message_handler(content_types = ['photo','text','document','voice','video','animation','sticker'])
async def forward_message(message: types.Message):
    await bot.forward_message(os.getenv('GROUP_ID'), message.from_user.id, message.message_id)


if __name__ == '__main__':
    start_time = time.time()
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    print("--- %s seconds ---" % (time.time() - start_time))
