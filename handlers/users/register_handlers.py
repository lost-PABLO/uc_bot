from aiogram import types
from aiogram.dispatcher import FSMContext
from data.config import ADMINS
from loader import dp,bot
from states.register import Register
from keyboards.inline.inline_btn import ha_yoq,ha_yoq1,ha_yoq2,mobile_ha_yoq1,mobile_ha_yoq2,mobile_ha_yoq3
from keyboards.default.defoult_btn import uc_narxlari,contact




@dp.callback_query_handler(text="kiritish")
async def start_registration(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("✍️ Ma'lumotlarni kiritishni boshlaymizmi?", reply_markup=ha_yoq)


@dp.callback_query_handler(text="ha2")
async def start_registration(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("✍️ Ma'lumotlarni kiritishni boshlaymizmi?", reply_markup=ha_yoq)


@dp.callback_query_handler(text="ha")
async def confirm_registration(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("‼️ Hozir sizga bir nechta savollar beriladi ‼️")
    await call.message.answer("😊 Ism Familiyangizni kiriting:")
    await Register.full_name.set()


# Foydalanuvchi to'liq ismini olish
@dp.message_handler(state=Register.full_name)
async def get_full_name(message: types.Message, state: FSMContext):
    await message.delete()
    full_name = message.text
    await state.update_data({"full_name": full_name})
    await message.answer("📞 Telefon raqamingizni kiriting (masalan: +998901234567):", reply_markup=contact)
    await Register.phone.set()

# Foydalanuvchi telefon raqamini olish
@dp.message_handler(content_types=types.ContentType.CONTACT, state=Register.phone)
async def get_phone_number(message: types.Message, state: FSMContext):
    await message.delete()
    phone = message.contact.phone_number
    await state.update_data({"phone": phone})
    await message.answer("🆔 Pubg ID raqamingizni kiriting:")
    await Register.ID.set()


@dp.message_handler(state=Register.ID)
async def get_pubg_id(message: types.Message, state: FSMContext):
    await message.delete()
    pubg_id = message.text
    await state.update_data({"ID": pubg_id})
    await message.answer("🥇 PUBGdagi niknemingizni kiriting:")
    await Register.game_nik.set()


@dp.message_handler(state=Register.game_nik)
async def get_game_nickname(message: types.Message, state: FSMContext):
    await message.delete()
    nik_name = message.text
    await state.update_data({"nik_name":nik_name})
    await message.answer("💰 Sotib olmoqchi bo'lgan uc miqdoringizni kiriting:")
    await Register.miqdor.set()


@dp.message_handler(state=Register.miqdor)
async def s(message:types.Message,state:FSMContext):
    await message.delete()
    username = message.from_user.username
    miqdor = message.text
    await state.update_data({"miqdor":miqdor})
    await state.update_data({"username":username})
    data = await state.get_data()
    full_name = data["full_name"]
    username = data["username"]
    phone = data["phone"]
    ID = data["ID"]
    nik_name = data["nik_name"]
    miqdor = data["miqdor"]
    malumot = (f"📋 Sizning ma'lumotlaringiz:\n"
               f"👤 Ism Familiya: {full_name}\n"
               f"👤 username: @{username}\n"
               f"📞 Telefon raqamingiz: +{phone}\n"
               f"🆔 PUBG ID raqamingiz: {ID}\n"
               f"🥇 PUBGdagi niknemingiz: {nik_name}\n"
               f"💰 UC miqdoringiz: {miqdor}")
    await message.answer(text=f"{malumot}\n❗️❓ Ma'lumotlaringiz tog'rimi ❗️❓",reply_markup=ha_yoq1)


@dp.callback_query_handler(state=Register,text="ha1")
async def sc(call:types.CallbackQuery,state:FSMContext):
    username = call.message.from_user.username
    await call.message.delete()
    data = await state.get_data()
    full_name = data["full_name"]
    username = data["username"]
    phone = data["phone"]
    ID = data["ID"]
    nik_name = data["nik_name"]
    miqdor = data["miqdor"]
    malumot = (f"📋 Foydalanuvchi ma'lumotlari:\n"
               f"👤 Ism Familiyasi: {full_name}\n"
               f"👤 username: @{username}\n"
               f"📞 Telefon raqami: +{phone}\n"
               f"🆔 PUBG ID raqami: {ID}\n"
               f"🥇 PUBGdagi niknemi: {nik_name}\n"
               f"💰 UC miqdori: {miqdor}")
    for i in ADMINS:
        await bot.send_message(i,f"📩 Foydalanuvchi sizga ma'lumot yubordi:\n{malumot}")
        await call.message.answer("📲 Ma'lumotlringiz yuborildi tez orada @ADM1N_OZODBEK siz bilan aloqaga chiqadi ‼️️",reply_markup=uc_narxlari)
    try:
        await state.finish()
    except KeyError:
        pass


@dp.callback_query_handler(state=Register,text="yoq1")
async def sc(call:types.CallbackQuery,state:FSMContext):
    await call.message.delete()
    await call.message.answer("♻️ Qayta kiritasizmi",reply_markup=ha_yoq2)
    try:
        await state.finish()
    except KeyError:
        pass

@dp.callback_query_handler(text="yoq",state=Register)
async def cancel_registration(call: types.CallbackQuery,state:FSMContext):
    await call.message.answer("📛 Bekor qilindi!", reply_markup=uc_narxlari)
    await call.message.delete()
    await state.finish()