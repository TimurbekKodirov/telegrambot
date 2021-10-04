from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


Customer = KeyboardButton("Customer")
Master = KeyboardButton("Master")
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(Customer, Master)
