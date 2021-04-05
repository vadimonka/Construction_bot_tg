from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

block = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Кирпич 65", callback_data="block_kirpich_65"),
            InlineKeyboardButton(text="Кирпич 88", callback_data="block_kirpich_88"),
        ],
        [
            InlineKeyboardButton(text="Кирпич евро 65", callback_data="block_kirpich_euro_65"),
            InlineKeyboardButton(text="Кирпич евро 88", callback_data="block_kirpich_euro_88"),
        ],
        [
            InlineKeyboardButton(text="Керамзит 90", callback_data="block_keramzit_90"),
            InlineKeyboardButton(text="Керамзит 120", callback_data="block_keramzit_120"),
        ],
        [
            InlineKeyboardButton(text="Керамзит 190", callback_data="block_keramzit_190"),
            InlineKeyboardButton(text="Керамзит 290", callback_data="block_keramzit_290"),
        ],
        [
            InlineKeyboardButton(text="Газобетон 100", callback_data="block_gazobeton_100"),
            InlineKeyboardButton(text="Газобетон 200", callback_data="block_gazobeton_200"),
        ],
        [
            InlineKeyboardButton(text="Газобетон 300", callback_data="block_gazobeton_300"),
            InlineKeyboardButton(text="Газобетон 400", callback_data="block_gazobeton_400"),
        ],
    ],
    resize_keyboard=True
)

floor = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Базовая стяжка", callback_data="floor_base"),
        ],
        [
            InlineKeyboardButton(text="Универсальная стяжка", callback_data="floor_uni"),
        ],
        [
            InlineKeyboardButton(text="Финишная стяжка", callback_data="floor_finish"),
        ],
        [
            InlineKeyboardButton(text="Кнауф супер пол", callback_data="floor_knauf"),
        ],
    ],
    resize_keyboard=True
)
