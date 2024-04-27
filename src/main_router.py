from aiogram import Bot, Router
from aiogram.filters import Command
from aiogram.types import Message

from src.config import token

bot = Bot(token=token)
router = Router()


@router.message(Command(commands=["start"]))
async def start(message: Message) -> None:
    await message.reply("https://youtu.be/dQw4w9WgXcQ")
