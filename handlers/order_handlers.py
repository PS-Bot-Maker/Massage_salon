from aiogram import Router, types, F
from aiogram.filters.command import Command
from data.bot_config import db
import sqlite3


order_han_router = Router()

@order_han_router.message(Command('ordering'))
async def start_ordering(message: types.Message):
    clients_db = sqlite3.connect(db)
    await message.answer("Всё сработало как надо!", alert=True)