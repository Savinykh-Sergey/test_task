from aiogram.types import KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo
from database.DBHelper import DBHelper

choice_character = [
    [InlineKeyboardButton(text="выбрать персонажа", web_app=WebAppInfo(url='https://xd.adobe.com/view/58fface2-d5a1-4572-af02-5fac362d3fa4-0dac/'))],
]
choice_character = InlineKeyboardMarkup(inline_keyboard=choice_character)
