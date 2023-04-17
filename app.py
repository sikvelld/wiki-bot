from aiogram import  executor
from aiogram import Bot, Dispatcher, types

bot = Bot(token='6058236831:AAGjteAVkGgnbsoKTItDuLtYNAxJLmib5ik')
dp = Dispatcher(bot)

async  def one_startup(_):
    print('Бот вышел в онлаин')
"""Клиент блок"""
@dp.message_handler(commands=['start', 'help'])
async def commands_starts(message: types.Message):
    try:
        await bot.send_message(
            message.from_user.id, 'Telegram Bot activated</>\nCommands(Команды):\n/start\n/Time - Во сколько мы в комнате\n/Places - Где мы\n/Admin - Кому скидывать\n/Cnacks - И так понятно я думаю\n/Drinks - Тоже думаю понятно:)'
        )
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/Backdoors_Bot')

@dp.message_handler(commands=['Time'])
async def room_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Пн: c 4:00PM - 3:00PM\n Вт: c 10:00AM - 3:00PM\n Ср по Вс: с 4:00PM - 3:00PM ')

@dp.message_handler(commands=['Places'])
async def room_places_commands(message: types.Message):
    await bot.send_message(message.from_user.id, 'Комната: 14/1\nЭтаж: 4')


@dp.message_handler(commands=['Admin'])
async def admins_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Номер: +79274449798\nБанк: Тинькофф Банк\nИмя: Данил Р.')

@dp.message_handler(commands=['Cnacks'])
async def cnacks_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Снеки:\nLays(Ребрышки гриль) 140г - over\nLays(Сметана и лук) 140г - over\nLays(Краб) 140г - over\nLays(Сыр) 140г - 1(пачка)\nLays(Лосось) 140г - over\nLays(Лобстер) 140г - over\nLays(Красная икра) 140г - over\n')

@dp.message_handler(commands=['Drinks'])
async def drinks_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Напитки:\nFlash 0.45л - over\nGorilla(mango) 0.45л - 65Rub\nНапиток добрый(Апельсин) 1л - over\nНапиток добрый(Кола) 1л - over\nНапиток добрый(Лимон-лайм) 1л - 69Rub\nAdrenalin(RUSH) 0.449 - over\nTornado Coconut 0.45л - 55Rub')

@dp.message_handler()
async def get_message(message: types.Message):
    if message.text == 'Привет':

        await message.answer('И вам того же')

executor.start_polling(dp, skip_updates=True, on_startup=one_startup)


