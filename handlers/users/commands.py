from data.loader import bot
from telebot.types import Message
from keyboards.reply import generate_wikipedia_button

@bot.message_handler(commands=['start'])
def command_start(message: Message):
    chat_id = message.chat.id
    text = f"""Здравствуйте, {message.from_user.first_name}
Я википедия бот готов вам помочь"""
    bot.send_message(chat_id, text, reply_markup=generate_wikipedia_button())














