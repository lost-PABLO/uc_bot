from aiogram import types
from loader import dp,bot
from keyboards.default.defoult_btn import botni_baholash,uc_narxlari,admin_button
from data.config import ADMINS

@dp.message_handler(text="📞 Admin bilan bog'lanish")
async def s(message:types.Message):
    malumot = ("Ism Familiya: Umarbekov Ozodbek\n"
               "username: @ADM1N_OZODBEK\n")
    await message.answer(malumot)


@dp.message_handler(text="♻️ Takliflar")
async def s(message:types.Message):
    malumot = ("username: @ADM1N_OZODBEK\n"
               "Takliflaringizni yozib qoldiring")
    await message.answer(malumot)


@dp.message_handler(text="⭐️ Botni baholash")
async def s(message:types.Message):
    await message.answer("Bot faoliyatiga baho bering! 👇",reply_markup=botni_baholash)


@dp.message_handler(text="⭐⭐⭐⭐⭐ | A'lo")
async def f(message:types.Message):
    malumot = ("Foydalanuvchi botni baholadi.\n"
               "⭐⭐⭐⭐⭐ | A'lo")
    await message.answer("Tayyor!",reply_markup=uc_narxlari)
    for i in ADMINS:
        await bot.send_message(i,malumot)


@dp.message_handler(text="⭐⭐⭐⭐ | Yaxshi")
async def c(message: types.Message):
    malumot = ("Foydalanuvchi botni baholadi.\n"
               "⭐⭐⭐⭐ | Yaxshi")
    await message.answer("Tayyor!",reply_markup=uc_narxlari)
    for i in ADMINS:
        await bot.send_message(i,malumot)


@dp.message_handler(text="⭐⭐⭐ | O'rtacha")
async def f(message:types.Message):
    malumot = ("Foydalanuvchi botni baholadi.\n"
               "⭐⭐⭐ | O'rtacha")
    await message.answer("Tayyor!",reply_markup=uc_narxlari)
    for i in ADMINS:
        await bot.send_message(i,malumot)


@dp.message_handler(text="⭐⭐ | Qoniqarli")
async def f(message:types.Message):
    malumot = ("Foydalanuvchi botni baholadi.\n"
               "⭐⭐ | Qoniqarli")
    await message.answer("Tayyor!",reply_markup=uc_narxlari)
    for i in ADMINS:
        await bot.send_message(i,malumot)


@dp.message_handler(text="⭐ | Qoniqarsiz")
async def f(message:types.Message):
    malumot = ("Foydalanuvchi botni baholadi.\n"
               "⭐ | Qoniqarsiz")
    await message.answer("Tayyor!",reply_markup=uc_narxlari)
    for i in ADMINS:
        await bot.send_message(i,malumot)


@dp.message_handler(text="❌ Bekor qilish")
async def f(message:types.Message):
    await message.answer("Bekor qilindi",reply_markup=uc_narxlari)
    if message.from_user.id in ADMINS:
        await message.answer("Bekor qilindi",reply_markup=admin_button)

