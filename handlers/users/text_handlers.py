from telebot.types import Message, ReplyKeyboardRemove
from keyboards.reply import generate_wikipedia_button
from data.loader import bot
import wikipedia


# @bot.message_handler(lambda message: '🌎 Wikipedia' in message.text)
@bot.message_handler(regexp='🌎 Wikipedia')
def reaction_to_wiki(message: Message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, 'Что хотите узнать?',
                           reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, wiki_func)


def wiki_func(message: Message):
    chat_id = message.chat.id
    text = message.text
    try:
        result = wikipedia.summary(text)
        bot.send_message(chat_id, result)
        bot.send_message(chat_id, 'Что еще найти?',
                         reply_markup=generate_wikipedia_button())
    except:
        bot.send_message(chat_id, 'Не удалось найти. Проверьте правильно ввода.',
                         reply_markup=generate_wikipedia_button())
