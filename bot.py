from tracemalloc import stop
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from keybord import *
import random
bot = Bot(token="5484671194:AAGbVwLRsK1xjcTk2Q4ix4KRhiBf3LMI6mI")
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши /help для подробной информации")
@dp.message_handler(commands=['secret'])
async def process_sec_command(message: types.Message):
    await message.reply("Ты нашел секретку! это фото кокоса имеет очень важную роль как кокос из игры Team Fortress 2, без этого кокоса бот и игра не запустятся, в игре от Valve никто не знает что делает этот кокос но в моем боте он служит наполнителем переменной пока она не используется")
    photo = open("imeg/спасалка.jpg", "rb")
    await bot.send_photo(message.from_user.id, photo = photo)
    photo.close()
@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("""
Напиши /open чтобы открыть мегаящик
Шанс выпадения леги/хроматика 1 процент
Шанс выпадения мифика/эпика 5 процентов
Шанс выпадения сверх редкого 10 процентов
Шанс выпадения редкого 34 процентов
Шанс выпадения очков силы 50 процентов
https://www.donationalerts.com/r/askel_900\n поддержать автора
Кстати тут есть 1 секретка
    """)
@dp.message_handler(commands=['open'])
async def process_help_command(message: types.Message):
    save = ["Спасалка.jpg"]
    No = ["Ничего.jpg"]
    Rare = ["Примо.jpg", "Барли.jpg", "Поко.jpg", "Роза.jpg", "Шелли.jpg", "Нита.jpg", "Кольт.jpg", "Булл.jpg", "Джеси.jpg", "Брок.jpg", "Диномайк.jpg", "Тик.jpg", "Бит.jpg", "Эмз.jpg", "Бо.jpg"]
    Super_rare = ["Рико.jpg", "Деррил.jpg", "Пенни.jpg", "Карл.jpg", "Джеки.jpg"]
    Epic = ["Пайпер.jpg", "Пем.jpg", "Френк.jpg", "Биби.jpg", "Беа.jpg", "Нани.jpg", "Эдгар.jpg", "Гриф.jpg", "Гром.jpg", "Бонни.jpg"]
    Mythic = ["Мортис.jpg", "Тара.jpg", "Джин.jpg", "Макс.jpg", "Пи.jpg", "Спраут.jpg", "Байрон.jpg", "Сквик.jpg"]
    Legendary = ["Спайк.jpg", "Ворон.jpg", "Леон.jpg", "Сенди.jpg", "Амбер.jpg", "Мег.jpg",  "Джанет.jpg", "Отис.jpg", "Гейл.jpg", "Вольт.jpg", "Колетт.jpg", "Лу.jpg", "Гавс.jpg", "Бель.jpg", "Базз.jpg", "Эш.jpg", "Лола.jpg", "Фенг.jpg", "Ева.jpg"]
    p = random.randint(1, 103)    
    kat = save    
    if p == 1:
        kat = Legendary
    elif p >= 2 and p <= 6:
        kat = Mythic
    elif p >= 6 and p <= 10:
        kat = Epic
    elif p >= 10 and p <= 19:
        kat = Super_rare
    elif p >= 19 and p < 54:
        kat = Rare
    elif p >= 54 and p <= 103:
        kat = No

    kat1 = random.choice(kat)
    print(p)   
    photo = open("imeg/{}".format(kat1), "rb")
    await bot.send_photo(message.from_user.id, photo=photo)
    photo.close()
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)




