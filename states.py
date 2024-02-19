from aiogram.fsm.state import StatesGroup, State

class Gen(StatesGroup):
    choose_test = State()
    create_test = State()