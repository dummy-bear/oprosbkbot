from aiogram import Router, F
from aiogram.filters import CommandStart, CommandObject, Command
from aiogram.types import Message
from dbhan.dao import set_user
from keyboards.all_kb import main_kb

def get_refer_id(command_args):
    try:
        return int(command_args)
    except (TypeError, ValueError):
        return None

start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: Message, command: CommandObject):
	refer_id = get_refer_id(command.args)
	user = await set_user(tg_id=message.from_user.id, username=message.from_user.username, full_name=message.from_user.full_name)
	await message.answer('Привет, ' + str(message.from_user.first_name) + '! Этот бот проводит опросы! Хочешь пройти опрос или создать новый?' + str(refer_id), reply_markup=main_kb(message.from_user.id))
	

@start_router.message(Command('start_2'))
async def cmd_start_2(message: Message):
    await message.answer('Запуск сообщения по команде /start_2 используя фильтр Command()')

@start_router.message(F.text == '/start_3')
async def cmd_start_3(message: Message):
    await message.answer('Запуск сообщения по команде /start_3 используя магический фильтр F.text!')
