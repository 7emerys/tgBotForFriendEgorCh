from aiogram.types import ReplyKeyboardMarkup,InlineKeyboardMarkup,InlineKeyboardButton


main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('Каталог').add('Контакты')


catalog_panel = ReplyKeyboardMarkup(resize_keyboard=True)
catalog_panel.add('Жидкость').add('Электронные сигареты')


admin = ReplyKeyboardMarkup(resize_keyboard=True)
admin.add('Каталог').add('Контакты').add('БО$$')


electronic_cigarettes_panel = ReplyKeyboardMarkup(resize_keyboard=True)
electronic_cigarettes_panel.add('Под').add('Одноразка').add('Расходники')


admin_panel = ReplyKeyboardMarkup(resize_keyboard=True)
admin_panel.add('Добавить товар').add('Удалить товар').add('Рассылка')


Liquids_list = InlineKeyboardMarkup(row_width=2)
Liquids_list.add(InlineKeyboardButton(text='TOYZ', url='https://t.me/KOPOSIARY'),
                InlineKeyboardButton(text='Brusko', url='https://t.me/KOPOSIARY'),
                InlineKeyboardButton(text='Слово пацана', url='https://t.me/KOPOSIARY'),
                InlineKeyboardButton(text='Трава', url='https://t.me/KOPOSIARY'),
                InlineKeyboardButton(text='Dota', url='https://t.me/KOPOSIARY'),
                InlineKeyboardButton(text='Анархия', url='https://t.me/KOPOSIARY'),
                InlineKeyboardButton(text='Анархия V2', url='https://t.me/KOPOSIARY'),
                InlineKeyboardButton(text='MAD', url='https://t.me/KOPOSIARY'),
                InlineKeyboardButton(text='BLOOD', url='https://t.me/KOPOSIARY'),
                InlineKeyboardButton(text='Рик&Морти', url='https://t.me/KOPOSIARY'))


Pod_list = InlineKeyboardMarkup(row_width=2)
Pod_list.add(InlineKeyboardButton(text='TOYZ', url='https://t.me/KOPOSIARY'),
                InlineKeyboardButton(text='Brusko', url='https://t.me/KOPOSIARY'),
                InlineKeyboardButton(text='Слово пацана', url='https://t.me/KOPOSIARY'),
                InlineKeyboardButton(text='Трава', url='https://t.me/KOPOSIARY'),
                InlineKeyboardButton(text='Dota', url='https://t.me/KOPOSIARY'),
                InlineKeyboardButton(text='Анархия', url='https://t.me/KOPOSIARY'),
                InlineKeyboardButton(text='Анархия V2', url='https://t.me/KOPOSIARY'),
                InlineKeyboardButton(text='MAD', url='https://t.me/KOPOSIARY'),
                InlineKeyboardButton(text='BLOOD', url='https://t.me/KOPOSIARY'),
                InlineKeyboardButton(text='Рик&Морти', url='https://t.me/KOPOSIARY'))


One_size_fits_all_list = InlineKeyboardMarkup(row_width=2)
One_size_fits_all_list.add(InlineKeyboardButton(text='TOYZ', url='https://t.me/KOPOSIARY'),
                InlineKeyboardButton(text='Brusko', url='https://t.me/KOPOSIARY'),
                InlineKeyboardButton(text='Слово пацана', url='https://t.me/KOPOSIARY'),
                InlineKeyboardButton(text='Трава', url='https://t.me/KOPOSIARY'),
                InlineKeyboardButton(text='Dota', url='https://t.me/KOPOSIARY'),
                InlineKeyboardButton(text='Анархия', url='https://t.me/KOPOSIARY'),
                InlineKeyboardButton(text='Анархия V2', url='https://t.me/KOPOSIARY'),
                InlineKeyboardButton(text='MAD', url='https://t.me/KOPOSIARY'),
                InlineKeyboardButton(text='BLOOD', url='https://t.me/KOPOSIARY'),
                InlineKeyboardButton(text='Рик&Морти', url='https://t.me/KOPOSIARY'))


Consumables_list = InlineKeyboardMarkup(row_width=2)
Consumables_list.add(InlineKeyboardButton(text='TOYZ', url='https://t.me/KOPOSIARY'),
                InlineKeyboardButton(text='Brusko', url='https://t.me/KOPOSIARY'),
                InlineKeyboardButton(text='Слово пацана', url='https://t.me/KOPOSIARY'),
                InlineKeyboardButton(text='Трава', url='https://t.me/KOPOSIARY'),
                InlineKeyboardButton(text='Dota', url='https://t.me/KOPOSIARY'),
                InlineKeyboardButton(text='Анархия', url='https://t.me/KOPOSIARY'),
                InlineKeyboardButton(text='Анархия V2', url='https://t.me/KOPOSIARY'),
                InlineKeyboardButton(text='MAD', url='https://t.me/KOPOSIARY'),
                InlineKeyboardButton(text='BLOOD', url='https://t.me/KOPOSIARY'),
                InlineKeyboardButton(text='Рик&Морти', url='https://t.me/KOPOSIARY'))
