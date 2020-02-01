import telebot
import config
import schedule
import time

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Оу , мне написали')
    bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAIf7V41tb65v4vrhoBt-7ce2pevbf-AAAJ_AANLae4QVPPmclI6esMYBA')


@bot.message_handler(commands=["ping"])
def on_ping(message):
    bot.reply_to(message, "Я до сих пор работаю")
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIf9F41t5PWT3f5h-pvVEwLz3x4LyA6AAJ7AQACFKL1E6IZp7zvnesXGAQ')


@bot.message_handler(commands=['help'])
def command_help(message):
    bot.send_message(message, "Тебе понадобилась HelP?")


@bot.message_handler(content_types=['text'])
def send_hi(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет)')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Пока(')


@bot.message_handler(regexp='((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)')
def command_url(message):
    bot.reply_to(message, "Я не могу распознать этот url")


@bot.message_handler(func=lambda message: message.document.mime_type == 'text/plain', content_types=['document'])
def command_handle_document(message):
    bot.reply_to(message, "Я получил присланный Document")


if __name__ == '__main__':
    bot.polling(none_stop=True)


@bot.message_handler(content_types=['text'])
def mor_msg(message):
    mor_msg = []
    bot.send_message(message.chat.id, mor_msg)

schedule.every().day.at("7.00").do(mor_msg)
while True:
    schedule.run_pending()
    time.sleep(1)
