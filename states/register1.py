from aiogram.dispatcher.filters.state import State,StatesGroup



class Register1(StatesGroup):
    full_name = State()
    phone = State()
    ID = State()
    zone = State()
    miqdor = State()
    username = State()



class VIDO(StatesGroup):
    vido = State()
    text = State()