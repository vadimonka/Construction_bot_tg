from math import ceil

from main import dp
from keyboards import floor

from aiogram.types import Message
from aiogram.dispatcher.filters import Command, Text

stack1 = []


@dp.message_handler(Command("floor"))
async def show_menu_floor(message: Message):
    await message.answer(text="Выберите стяжку для рассчета", reply_markup=floor)


@dp.callback_query_handler(Text(startswith="floor_"))
async def button_block(call):
    await call.answer(cache_time=30)
    global stack1
    if call.data == 'floor_base':
        await call.message.answer("Вы выбрали <b>Базовую стяжку</b>.")
        stack1 = []
    if call.data == 'floor_uni':
        await call.message.answer("Вы выбрали <b>Универсальную стяжка</b>.")
        stack1 = []
    if call.data == 'floor_finish':
        await call.message.answer("Вы выбрали <b>Финишную стяжку</b>.")
        stack1 = []
    if call.data == 'floor_knauf':
        await call.message.answer("Вы выбрали <b>Кнауф супер пол</b>.")
        stack1 = []
    await call.message.answer("Напишите размеры пола через пробел"
                              "или сразу площадь пола")

    @dp.message_handler()
    async def calc(message: Message):
        input_data = [float(x) for x in message.text.split(' ')]
        result = 0
        stack1.clear()
        await message.reply(result, reply_markup=floor)
