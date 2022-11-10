from aiogram import *
# from telebot import *
from pytube import YouTube
from config import *
import os

bot = Bot(TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_message(message:types.Message):
    chat_id= message.chat.id
    await bot.send_message(chat_id, f'Привет, я могу скачивать видео с Youtube \nотправь мне ссылку\n')

@dp.message_handler()
async def text_message(message:types.Message):
    chat_id= message.chat.id
    url = message.text
    yt=YouTube(url)
    if message.text.startswith== "https://youtu.be/" or 'https://www.youtube.com/':
        await bot.send_message(chat_id, f'*Начинаю загрузку видео*: *{yt.title}*\n'
                                  f'*c канала*: [{yt.author}]({yt.channel_url})', parse_mode='Markdown')    
        await download_youtube_video(url, message ,bot)

async def download_youtube_video(url, message,bot):
    
    yt=YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4')
    stream.get_highest_resolution().download(f'{message.chat.id}', f'{message.chat.id}_{yt.title}')
    with open (f'{message.chat.id}/{message.chat.id}_{yt.title}', 'rb') as video:
        await bot.send_video(message.chat.id, video, caption= "*Вот ваше видео*", parse_mode="Markdown" )
        os.remove(f"{message.chat.id}/{message.chat.id}_{yt.title}")



   


# @dp.message_handler(commands=['start'])
# def start(message):
#     mess = f"Привет, <b>{message.from_user.first_name} <u> {message.from_user.last_name}</u></b>"
#     bot.send_message(message.chat.id, mess, parse_mode='html')


# @bot.message_handler(content_types=['text'])
# def get_user_text(message):
#     if message.text == 'Hello':
#         bot.send_message(message.chat.id, 'И тебе привет!', parse_mode='html')
#     elif message.text == 'id':
#         bot.send_message(message.chat.id, f'Твой ID: {message.from_user.id}', parse_mode='html')
#     elif message.text == 'photo':
#         photo = open ('XO.png', 'rb')
#         bot.send_photo(message.chat.id, photo)
    # else:
    #     bot.send_message(message.chat.id, 'Я тебя не понимаю', parse_mode='html')


# @bot.message_handler(content_types=['photo'])
# def get_user_photo(message):
#      bot.send_message(message.chat.id, 'Вау, крутое фото')


# @bot.message_handler(commands=['website'])
# def website(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton('Посетить веб сайт', url='https://mail.ru'))
#     bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)



# @bot.message_handler(commands=['help'])
# def website(message):
    
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#     website = types.KeyboardButton('Веб сайт')
#     start = types.KeyboardButton('Start')

#     markup.add(website, start)
#     bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)

# @bot.message_handler(commands=['help'])

# def download(message):
#     file_info = tb.get_file(file_id)

#     file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(API_TOKEN, file_info.file_path))

if __name__ == '__main__':
    executor.start_polling(dp)
