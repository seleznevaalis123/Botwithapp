from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from aiogram import Bot, types
import config

bot = Bot(config.bot_token)

markup = InlineKeyboardMarkup(row_width=2)
menuitem1 = InlineKeyboardButton(text="🍽️ORDER FOOD", url='https://grandbazar.io/ru/collection/robocraft')
menuitem2 = InlineKeyboardButton(text="🪷SPA", callback_data='None')
menuitem3 = InlineKeyboardButton(text="🧘‍YOGA", callback_data='None')
menuitem4 = InlineKeyboardButton(text="📣EVENTS", callback_data='None')
menuitem5 = InlineKeyboardButton(text="⚙️BOT SETTINGS", callback_data='None')
markup.add(menuitem1, menuitem2, menuitem3, menuitem4, menuitem5,)

