from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

start1 = InlineKeyboardButton(callback_data='сезоны', text='Все сезоны')
start = InlineKeyboardMarkup(row_width=2).add(start1)
start.add(InlineKeyboardButton('Все персонажи', callback_data='персонажи'))
start.add(InlineKeyboardButton('Обо всем', callback_data='обо всем'))

ses1 = InlineKeyboardButton(callback_data='1', text='1 сезон')
ses = InlineKeyboardMarkup(row_width=2).add(ses1)
ses.add(InlineKeyboardButton('2 сезон', callback_data='2'))
ses.add(InlineKeyboardButton('Назад', callback_data='start'))

