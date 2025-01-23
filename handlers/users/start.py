from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.defoult_btn import uc_narxlari,admin_button
from data.config import ADMINS, CHANNELS
from loader import dp
from utils.misc import subscription
from keyboards.inline.tekshirish_btn import tekshirish


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if message.from_user.id in ADMINS:
        await message.answer("Xush kelibsiz, admin!", reply_markup=admin_button)
    else:
        await message.answer("Xush kelibsiz!", reply_markup=uc_narxlari)

@dp.callback_query_handler(text="tekshirish")
async def checker(call: types.CallbackQuery, check_button=None):
    await call.answer()
    result = str()
    for channel in CHANNELS:
        status = await subscription.check(user_id=call.from_user.id,
                                          channel=channel)
        if status:
            await call.message.delete()
            result += (f"Yaxshi, {call.from_user.full_name} foydalanishingiz mumkin👇🏻")
            await call.message.answer(result, disable_web_page_preview=True)  # reply_markup=start_btn)
        else:
            await call.message.delete()
            result += (
                f"🚫Obuna bo'lmadingiz, qayta urinib ko'ring\n\n♻️Kanalga obuna bo'lib \"🔄 Obunani tekshirish\" ni bosing")
            await call.message.answer(result, disable_web_page_preview=True, reply_markup=tekshirish)