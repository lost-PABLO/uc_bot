from loader import dp
from aiogram import types
from keyboards.inline.inline_btn import narxlar,boshqa_oyinlar,legends,clash


@dp.message_handler(text="💳 UC sotib olish")
async def s(message:types.Message):
    await message.delete()
    foto = open("static/foto/unnamed.jpg","rb")
    text = """60 UC - 13.000💰
90 UC - 19.000💰
120 UC - 26.000💰
150 UC - 33.000💰
180 UC - 38.000💰
325 UC - 59.000 💰
385 UC - 74.000 💰
660 UC - 119.000 💰
720 UC - 130.000 💰
1800 UC - 292.000 💰
3850 UC - 575.000 💰
8100 UC - 1.115.000 💰
16,200 UC - 2.195.000 💰

UC sotib olish uchun ma'lumotlaringizni kiriting 👇"""
    await message.answer_photo(photo=foto,caption=text,reply_markup=narxlar)


@dp.callback_query_handler(text="Karzinka1")
async def s(call:types.CallbackQuery):
    await call.message.delete()


@dp.message_handler(text="🎮 Boshqa o'yinlar")
async def d(message:types.Message):
    await message.delete()
    text = "O'yinlarni tanlang 👇"
    foto = open("static/foto/photo_2025-01-06_19-08-44.jpg","rb")
    await message.answer_photo(photo=foto,caption=text,reply_markup=boshqa_oyinlar)


@dp.callback_query_handler(text="legeds")
async def s(call:types.CallbackQuery):
    await call.message.delete()
    text = """8 Almaz - 3 900 💰
35 Almaz - 8 000 💰
88 Almaz - 17 000 💰
Haftalik Almaz - 23 000 💰
132 Almaz - 24 000 💰
264 Almaz - 45 000 💰
440 Almaz - 73 000 💰
734 Almaz - 123 000 💰
933 Almaz - 155 000 💰
1410 Almaz - 245 000 💰
1881 Almaz - 305 000 💰
2845 Almaz - 455 000 💰
6163 Almaz - 1 050 000 💰"""
    foto = open("static/foto/Без названия (1).jpg","rb")
    await call.message.answer_photo(photo=foto,caption=text,reply_markup=legends)


@dp.callback_query_handler(text="karzinka2")
async def s(call:types.CallbackQuery):
    await call.message.delete()


@dp.callback_query_handler(text="back")
async def d(call:types.CallbackQuery):
    await call.message.delete()
    text = "O'yinlarni tanlang 👇"
    foto = open("static/foto/photo_2025-01-06_19-08-44.jpg","rb")
    await call.message.answer_photo(photo=foto,caption=text,reply_markup=boshqa_oyinlar)


@dp.callback_query_handler(text="clans")
async def s(call:types.CallbackQuery):
    await call.message.delete()
    foto = open("static/foto/Без названия.jpg","rb")
    text = "Tez kunda..."
    await call.message.answer_photo(photo=foto,caption=text,reply_markup=clash)


@dp.callback_query_handler(text="Back")
async def d(call:types.CallbackQuery):
    await call.message.delete()
    text = "O'yinlarni tanlang 👇"
    foto = open("static/foto/photo_2025-01-06_19-08-44.jpg","rb")
    await call.message.answer_photo(photo=foto,caption=text,reply_markup=boshqa_oyinlar)
