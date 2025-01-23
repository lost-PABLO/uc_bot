from aiogram.dispatcher.filters.state import State,StatesGroup


class Register(StatesGroup):
    full_name = State()
    phone = State()
    ID = State()
    game_nik = State()
    miqdor = State()
    username = State()

