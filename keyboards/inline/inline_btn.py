from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

narxlar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✍️ Ma'lumotlarni kiritish",callback_data="kiritish")
        ],[
            InlineKeyboardButton(text="📩 Telegram orqali bog'lanish",url="https://t.me/ADM1N0909")
        ],[
            InlineKeyboardButton(text="🗑",callback_data="Karzinka1")
        ]
    ]
)
boshqa_oyinlar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🕹️ Moblie Legeds",callback_data="legeds")
        ],[
            InlineKeyboardButton(text="⚔️ Clash of Clans",callback_data="clans")
        ],[
            InlineKeyboardButton(text="📞 Admin bilan bog'lanish",url="https://t.me/ADM1N0909")
        ],[
            InlineKeyboardButton(text="🗑",callback_data="karzinka2")
        ]
    ]
)
legends = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✍️ Ma'lumotlarni kiritish",callback_data="Kiritish")
        ],[
            InlineKeyboardButton(text="📞 Admin bilan bog'lanish",url="https://t.me/ADM1N0909")
        ],[
            InlineKeyboardButton(text="↩️ Back",callback_data="back")
        ]
    ]
)
clash = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✍️ Ma'lumotlarni kiritish",callback_data="Mkiritish")
        ],[
            InlineKeyboardButton(text="📞 Admin bilan bog'lanish",url="https://t.me/ADM1N0909")
        ],[
            InlineKeyboardButton(text="↩️ Back",callback_data="Back")
        ]
    ]
)

ha_yoq = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅Ha",callback_data="ha"),
            InlineKeyboardButton(text="🚫Yo'q",callback_data="yoq")
        ]
    ]
)

ha_yoq1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅Ha",callback_data="ha1"),
            InlineKeyboardButton(text="🚫Yo'q",callback_data="yoq1")
        ]
    ]
)


ha_yoq2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅Ha",callback_data="ha2"),
            InlineKeyboardButton(text="🚫Yo'q",callback_data="yoq")
        ]
    ]
)


mobile_ha_yoq1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅Ha",callback_data="HA1"),
            InlineKeyboardButton(text="🚫Yo'q",callback_data="YOQ1")
        ]
    ]
)


mobile_ha_yoq2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅Ha",callback_data="HA2"),
            InlineKeyboardButton(text="🚫Yo'q",callback_data="YOQ2")
        ]
    ]
)

mobile_ha_yoq3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅Ha",callback_data="HA3"),
            InlineKeyboardButton(text="🚫Yo'q",callback_data="YOQ3")
        ]
    ]
)
yuborish = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Yuborish",callback_data="yuborish")
        ]
    ]
)