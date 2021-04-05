from math import ceil

from main import dp
from keyboards import block

from aiogram.types import Message
from aiogram.dispatcher.filters import Command, Text

stack = []


@dp.message_handler(Command("block"))
async def show_menu_block(message: Message):
    await message.answer(text="Выберите материал для рассчета", reply_markup=block)


@dp.callback_query_handler(Text(startswith="block_"))
async def button_block(call):
    await call.answer(cache_time=30)
    global stack
    if call.data == 'block_kirpich_65':
        await call.message.answer("Вы выбрали <b>Кирпич 65</b>.")
        stack = [0.26, 0.13, 0.075, 512]
    if call.data == 'block_kirpich_88':
        await call.message.answer("Вы выбрали <b>Кирпич 88</b>.")
        stack = [0.26, 0.13, 0.098, 378]
    if call.data == 'block_kirpich_euro_65':
        await call.message.answer("Вы выбрали <b>Кирпич евро 65</b>.")
        stack = [0.26, 0.1, 0.075, 683]
    if call.data == 'block_kirpich_euro_88':
        await call.message.answer("Вы выбрали <b>Кирпич евро 88</b>.")
        stack = [0.26, 0.1, 0.098, 505]
    if call.data == 'block_keramzit_90':
        await call.message.answer("Вы выбрали <b>Керамзит 90</b>.")
        stack = [0.40, 0.1, 0.198, 304]  # расход на керамзтоблок в 2 раза меньше, поэтому берем не 72(куб) а 144(2куб)
    if call.data == 'block_keramzit_120':
        await call.message.answer("Вы выбрали <b>Керамзит 120</b>.")
        stack = [0.40, 0.13, 0.198, 228]  # расход на керамзтоблок в 2 раза меньше, поэтому берем не 72(куб) а 144(2куб)
    if call.data == 'block_keramzit_190':
        await call.message.answer("Вы выбрали <b>Керамзит 190</b>.")
        stack = [0.40, 0.20, 0.198, 144]  # расход на керамзтоблок в 2 раза меньше, поэтому берем не 72(куб) а 144(2куб)
    if call.data == 'block_keramzit_290':
        await call.message.answer("Вы выбрали <b>Керамзит 290</b>.")
        stack = [0.40, 0.3, 0.198, 95]  # расход на керамзтоблок в 2 раза меньше, поэтому берем не 72(куб) а 144(2куб)
    if call.data == 'block_gazobeton_100':
        await call.message.answer("Вы выбрали <b>Газобетон 100</b>.")
        stack = [0.625, 0.1, 0.25, 64, 75]
    if call.data == 'block_gazobeton_200':
        await call.message.answer("Вы выбрали <b>Газобетон 200</b>.")
        stack = [0.625, 0.2, 0.25, 32, 37]
    if call.data == 'block_gazobeton_300':
        await call.message.answer("Вы выбрали <b>Газобетон 300</b>.")
        stack = [0.625, 0.3, 0.25, 21, 25]
    if call.data == 'block_gazobeton_400':
        await call.message.answer("Вы выбрали <b>Газобетон 400</b>.")
        stack = [0.625, 0.4, 0.25, 16, 20]
    await call.message.answer("Напишите размеры через пробел | длина ширина высота ряды | "
                              "или сразу площадь стен и ряды")
    await call.message.answer("*<i>под рядами понимается количество блоков при продольной кладке</i>")

    @dp.message_handler()
    async def calc(message: Message):
        input_data = [float(x) for x in message.text.split(' ')]
        if len(input_data) > 2:
            wall_area = (input_data[0] + input_data[1]) * 2 * input_data[2]
        else:
            wall_area = input_data[0]
        print(stack)
        quantity_blocks = wall_area / stack[0] / stack[2] * input_data[-1]
        if len(stack) > 4:
            quantity_solution = quantity_blocks / stack[3]
            quantity_glue = quantity_blocks / stack[4]
            result = f"{ceil(quantity_blocks)} шт блоков \n" \
                     f"{ceil(quantity_solution)} меш смеси \n" \
                     f"{ceil(quantity_glue)} бал пена-клея"
        else:
            quantity_solution = quantity_blocks / stack[3]
            result = f"{ceil(quantity_blocks)} шт блоков \n" \
                     f"{ceil(quantity_solution)} меш смеси"

        stack.clear()
        await message.reply(result, reply_markup=block)
