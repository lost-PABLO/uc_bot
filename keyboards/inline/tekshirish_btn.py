from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton


tekshirish = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Obuna bo'lish",url="https://t.me/arzonuc09"),
            InlineKeyboardButton(text="Tekshirish",callback_data="tekshirish")
        ]
    ]
)