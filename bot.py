import telebot

bot = telebot.TeleBot('765437824:AAHiyUz4N8zTuv5Z435i6HNRREiJ2wS1A7I')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай')
    else:
        bot.send_message(message.chat.id, 'Извините , но я не понимаю вас')
@bot.message_handler(commands=['help'])
def command_help(message):
    bot.reply_to(message, "Тебе понадобилась помощь?")

@bot.message_handler(regexp='((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)')
def command_url(message):
    bot.reply_to(message, "Я не могу распознать этот url")

@bot.message_handler(func=lambda message: message.document.mime_type == 'text/plain', content_types=['document'])
def command_handle_document(message):
    bot.reply_to(message, "Я получил присланный документ")



bot.polling(none_stop=True)