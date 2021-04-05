import asyncio

from aiogram import Bot, Dispatcher, executor

BOT_TOKEN = None
admin_id = None

with open("token.txt") as f:
    BOT_TOKEN = f.read().strip()

with open("admin_id.txt") as f:
    admin_id = f.read().strip()

# variables
stack = []

loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)


async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text="Бот запущен")


if __name__ == "__main__":
    from handlers_block import dp
    from handlers_floor import dp
    executor.start_polling(dp, on_startup=send_to_admin, skip_updates=True)
