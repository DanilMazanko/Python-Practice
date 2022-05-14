from email import message
from multiprocessing import parent_process
import telebot
from telebot import types
bot = telebot.TeleBot('5361727946:AAHSoOOBoi3UrSaUJsx-KRpsmkYY95Lw5LE')


@bot.message_handler(commands=['start'])
def start2(message):
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(
        "Граматика база", callback_data='grammar')
    item2 = types.InlineKeyboardButton("IELTS",  callback_data='ielts')
    markup.add(item1, item2)
    bot.send_message(
        message.chat.id, "Здравствуйте, над чем бы вы хотели рабоатать сегодня?", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'grammar':
                bot.send_message(call.message.chat.id,
                                 'Здесь будут ресурсы по граматики')
            elif call.data == "ielts":
                bot.send_message(call.message.chat.id,
                                 'Здесь будут ресурсы')
    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)
