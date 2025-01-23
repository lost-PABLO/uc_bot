from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType
from loader import dp
from data.config import ADMINS
from states.register1 import VIDO

# Videolarni saqlash uchun lug'at
vidos = {}  # {video_id: caption}

# Adminlar uchun video qabul qilish
@dp.message_handler(text="📥 Vido joylash")
async def request_video(message: types.Message):
    await message.delete()
    if message.from_user.id in ADMINS:
        await message.answer("Videoni yuboring!")
        await VIDO.vido.set()
    else:
        await message.answer("Sizda bunday huquq yo'q.")

# Videoni saqlash
@dp.message_handler(content_types=ContentType.VIDEO, state=VIDO.vido)
async def save_video(message: types.Message, state: FSMContext):
    await message.delete()
    await state.update_data(video_id=message.video.file_id)
    await message.answer("Matnni yuboring!")
    await VIDO.text.set()

# Matnni saqlash
@dp.message_handler(content_types=ContentType.TEXT, state=VIDO.text)
async def save_caption(message: types.Message, state: FSMContext):
    await message.delete()
    data = await state.get_data()
    video_id = data.get("video_id")
    caption = message.text
    vidos[video_id] = caption  # Video va matnni saqlash
    await message.answer("Video va matn saqlandi!")
    try:
       await state.finish()
    except KeyError:
        pass
# Saqlangan videolarni ko'rsatish
@dp.message_handler(text="📱 ACAUNT vidolar")
async def show_videos(message: types.Message):
    await message.delete()
    if vidos:
        for idx, (video_id, caption) in enumerate(vidos.items(), start=1):
            await message.answer_video(video_id, caption=f"{idx}. {caption}")
    else:
        await message.answer("Videolar mavjud emas.")

# Videoni olib tashlash
@dp.message_handler(text="🗑️ Vidoni olib tashlash")
async def request_delete_video(message: types.Message):
    await message.delete()
    if message.from_user.id in ADMINS:
        if vidos:
            text = "O'chirish uchun video indeksini kiriting:\n\n"
            for idx, caption in enumerate(vidos.values(), start=1):
                text += f"{idx}. {caption}\n"
            await message.answer(text)
        else:
            await message.answer("Hech qanday video mavjud emas.")

@dp.message_handler(lambda message: message.text.isdigit())
async def delete_video_by_index(message: types.Message):
    await message.delete()
    if message.from_user.id in ADMINS:
        index = int(message.text) - 1
        if 0 <= index < len(vidos):
            video_id = list(vidos.keys())[index]
            del vidos[video_id]
            await message.answer("Video muvaffaqiyatli o'chirildi!")
        else:
            await message.answer("Noto'g'ri indeks!")
    else:
        await message.answer("Sizda bunday huquq yo'q.")
