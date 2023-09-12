from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, ContentType, FSInputFile
from aiogram.filters import Command
from aiogram import flags
from aiogram.fsm.context import FSMContext
from telegramBot.utils import *
from telegramBot.states import Gen
from telegramBot.kb import *
from telegramBot.text import *
from database.DBHelper import DBHelper
from datetime import datetime

import requests


db = DBHelper('database\\telegramBot.db')
router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    id = db.insert_info_user(msg.from_user.id, msg.from_user.full_name, msg.from_user.username, datetime.strptime(datetime.now().strftime("%d-%m-%Y %H:%M:%S"), "%d-%m-%Y %H:%M:%S"))
    text = f'Привет, {msg.from_user.full_name}, я аналог character.ai (нейросеть, которая введет общение от лица персонажа). Нажми на кнопку, чтобы выбрать персонажа'
    await msg.answer(text, reply_markup=choice_character)

@router.message(Command("help"))
async def message_handler(msg: Message):
    await msg.answer('Ты можешь управлять ботом, используя эти команды:\n/start - начать работу с ботом\n/menu - меню с командами для работы с ботом')

# @router.callback_query(F.data == "choice_character")
# async def input_image_prompt(msg: Message):
#     await msg.answer(good_rating)
  

# @router.message(Command("menu"))
# async def message_handler(msg: Message):
#     await msg.answer('Выберите пункт меню', reply_markup=menu.as_markup(resize_keyboard=True))

# ##

# @router.message(lambda message: message.text == "История")
# @flags.chat_action("typing")
# async def get_history(msg: Message):
#     # req = requests.post(f'http://http://127.0.0.1:10000/history/{get_user_id(db_, msg.from_user.id)}')
#     # print(req)
    
#     global id
#     history = db.get_history_photos(id)
#     if history:
#         await msg.answer(history)
#     else:
#         await msg.answer('История запросов пуста\nНажмите загрузить фото :)')

# @router.message(lambda message: message.text == "Баланс")
# @flags.chat_action("typing")
# async def get_balance(msg: Message):
#     await msg.answer('Ваш баланс: 10 токенов')

# @router.message(lambda message: message.text == "Избранное")
# @flags.chat_action("typing")
# async def get_favorite(msg: Message):
#     global id
#     info_favorite = db.get_data_favorite_photos(id)
#     await msg.reply(favorite)
#     if info_favorite:
#         for el in range(len(info_favorite[0])):
#             photo_message = await msg.answer_photo(photo=info_favorite[1][el], caption=info_favorite[0][el], reply_markup=del_favorite_photo)
#             db.update_message_id(photo_message.message_id, el + 1)
#     else:
#         await msg.answer('У вас не избранных фото\nДобавьте в избранное :)')

# @router.callback_query(F.data == "del_photo")
# async def input_image_prompt(callback_query: CallbackQuery):
#     db.delete_favorite_photo(callback_query.message.message_id)
#     await callback_query.answer(delete_photo)

# @router.message(Command("admin"))
# async def message_handler(msg: Message):
#     if msg.from_user.id == 856088953:
#         await msg.answer('Выберите пункт меню', reply_markup=menu_admin.as_markup(resize_keyboard=True))
#     else:
#         await msg.answer('Вы не являетесь администратором')

# @router.message(lambda message: message.text == "Дать привилегию")
# @flags.chat_action("typing")
# async def make_user_admin(msg: Message):
#    usernames = db.get_usernames()
#    keyboard = create_buttons_usernames(usernames)
#    await msg.answer("Выберите пользователя", reply_markup=keyboard.as_markup(resize_keyboard=True))


# @router.message(lambda message: message.text == "Загрузить фото")
# async def load_photo_callback(message: Message, state: FSMContext):
#     await state.set_state(Gen.img_prompt)
#     await message.reply(gen_image)

# @router.message(Gen.img_prompt)
# @flags.chat_action("upload_photo")
# async def detected_image(msg: Message): 
#     global id
#     id_photo = msg.photo[-1].file_id
#     # await msg.photo[-1].download('photo/test.jpg')
#     # payload = {'skip': 0, 'limit': 10}  
#     # req = requests.post(f'http://127.0.0.1:10000/photos/{get_user_id(db_, msg.from_user.id)}', params=payload)
#     db.insert_photo(id, id_photo)
#     mesg = await msg.answer(gen_wait)
#     photo_res = photo_processing()
#     await mesg.delete()

#     db.insert_data_detected_photo(id, photo_res[0], photo_res[1], photo_res[2], id_photo)
#     photo_id = db.get_photo_id(id)

#     await msg.answer_photo(photo=photo_id.photo_id, 
#                            caption=f'Кол-во объектов: {photo_res[0]}\nСумма: {photo_res[1]}\n{img_watermark}', 
#                            reply_markup=evaluation_neural_network)
  
# @router.callback_query(F.data == "right")
# async def input_image_prompt(msg: Message):
#     await msg.answer(good_rating)
  
# @router.callback_query(F.data == "wrong")
# async def input_image_prompt(callback_query: CallbackQuery):
#     photo_id = db.get_id_photo_from_favorite(callback_query.message.message_id)
#     db.insert_data_incorrect_detected_photo(photo_id)
#     await callback_query.answer(bad_rating)

# @router.callback_query(F.data == "add_favorite")
# async def add_favorite(callback_query: CallbackQuery):
#     global id
#     count_object, summa_face_value, photo_id = db.get_data_detected_photos(id)
#     db.insert_data_favorite_photo(id, count_object, summa_face_value, photo_id, callback_query.message.message_id)
#     await callback_query.answer(add_favorite)

        


