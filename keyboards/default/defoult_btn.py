from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,web_app_info,WebAppInfo

uc_narxlari = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("💳 UC sotib olish")
        ],[
            KeyboardButton("🎮 Boshqa o'yinlar"),
            KeyboardButton("📱 ACAUNT vidolar")
        ],[
            KeyboardButton("📞 Admin bilan bog'lanish")
        ],[
            KeyboardButton("♻️ Takliflar"),
            KeyboardButton("⭐️ Botni baholash")
        ]
    ],resize_keyboard=True
)
contact = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("📞 Contact yuborish",request_contact=True)
        ]
    ],resize_keyboard=True
)
botni_baholash = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("⭐⭐⭐⭐⭐ | A'lo"),
        ],[
            KeyboardButton("⭐⭐⭐⭐ | Yaxshi"),
        ],[
            KeyboardButton("⭐⭐⭐ | O'rtacha"),
        ],[
            KeyboardButton("⭐⭐ | Qoniqarli"),
        ],[
            KeyboardButton("⭐ | Qoniqarsiz"),
        ],[
            KeyboardButton("❌ Bekor qilish")
        ]
    ]
)
admin_button = ReplyKeyboardMarkup(
    keyboard=[
        [

            KeyboardButton("💳 UC sotib olish")
        ],[
            KeyboardButton("🎮 Boshqa o'yinlar"),
            KeyboardButton("📱 ACAUNT vidolar")
        ],[
            KeyboardButton("📞 Admin bilan bog'lanish")
        ],[
            KeyboardButton("♻️ Takliflar"),
            KeyboardButton("⭐️ Botni baholash")

        ],[
            KeyboardButton("📥 Vido joylash"),
            KeyboardButton("🗑️ Vidoni olib tashlash"),
        ],[
            KeyboardButton(text="🐱 GITHUB",web_app=WebAppInfo(url="https://github.com/lost-PABLO?tab=repositories"))
        ]
    ],resize_keyboard=True
)