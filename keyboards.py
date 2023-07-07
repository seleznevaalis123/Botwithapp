from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup


markup = InlineKeyboardMarkup(row_width=2)
menuitem1 = InlineKeyboardButton(text="🍽️ORDER FOOD", url='https://grandbazar.io/ru/collection/robocraft')
menuitem2 = InlineKeyboardButton(text="🪷SPA", callback_data='spa')
menuitem3 = InlineKeyboardButton(text="🧘‍YOGA", callback_data='yoga')
menuitem4 = InlineKeyboardButton(text="📣EVENTS", callback_data='events')
menuitem5 = InlineKeyboardButton(text="⚙️BOT SETTINGS", callback_data='settings')
markup.add(menuitem1, menuitem2, menuitem3, menuitem4, menuitem5,)

markup2 = InlineKeyboardMarkup(row_width=2)
menuitem1 = InlineKeyboardButton(text="Spa Menu", callback_data='spa menu')
menuitem2 = InlineKeyboardButton(text='📞WhatsApp', url="https://wa.me")
menuitem3 = InlineKeyboardButton(text='↩️Main menu', callback_data='main menu')
markup2.add(menuitem1, menuitem2, menuitem3)

markup3 = InlineKeyboardMarkup(row_width=1)
menuitem1 = InlineKeyboardButton(text="Massage Menu(2)", callback_data='massage menu')
menuitem2 = InlineKeyboardButton(text='Scrub(1)', callback_data='scrub')
menuitem3 = InlineKeyboardButton(text='↩️Back', callback_data='back_spa')
markup3.add(menuitem1, menuitem2, menuitem3)

markup4 = InlineKeyboardMarkup(row_width=2)
menuitem1 = InlineKeyboardButton(text='↩️Back', callback_data='️back_spa_menu')
markup4.add(menuitem1)



