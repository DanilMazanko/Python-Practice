from multiprocessing import parent_process
import telebot

bot = telebot.TeleBot('5361727946:AAHSoOOBoi3UrSaUJsx-KRpsmkYY95Lw5LE')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello fdf", parse_mode="html")


@bot.message_handler()
def get_user_text(message):
    if message.text == "времена":
        bot.send_message(message.chat.id, 'tensences', parse_mode='html')

# @bot.message_handler(commands=['stop'])
# def start(message):
#     bot.send_message(message.chat.id, "Hello fdf", parse_mode="html")
#     bot.polling(none_stop=False)


bot.polling(none_stop=True)
