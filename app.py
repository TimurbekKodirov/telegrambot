import logging
from aiogram import Bot, Dispatcher, executor, types
from data.config import API_TOKEN
from keyboards.default.KeyBoard import mainMenu
# tokens


# Configure logging
logging.basicConfig(level=logging.INFO)

# init bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# start
@dp.message_handler(commands=['start', 'help'])
async def sendWelcome(message: types.Message) -> object:
    await message.reply('1')
    await message.reply("Who are you", reply_markup=mainMenu)






if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
