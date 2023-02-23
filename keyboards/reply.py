from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def generate_wikipedia_button():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton(text='🌎 Wikipedia')
    markup.add(btn)
    return markup