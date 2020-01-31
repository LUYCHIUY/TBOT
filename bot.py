import telebot

bot = telebot.TeleBot('765437824:AAHiyUz4N8zTuv5Z435i6HNRREiJ2wS1A7I')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

bot.polling()