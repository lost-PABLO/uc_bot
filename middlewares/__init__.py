from aiogram import Dispatcher

from loader import dp
from .throttling import ThrottlingMiddleware
from .cheksub import BigBrother

if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(BigBrother())
