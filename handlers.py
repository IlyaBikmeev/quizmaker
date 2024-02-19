from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from random import choice
from aiogram.fsm.context import FSMContext
from aiogram.types.callback_query import CallbackQuery

import kb
import text

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)

@router.callback_query(F.data == 'my_tests')
async def all_user_tests(clbck: CallbackQuery, state: FSMContext):
    await clbck.message.answer(text.msg, reply_markup=kb.exit_kb)

@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)