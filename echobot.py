import telebot

bot = telebot.TeleBot("863992561:AAFzD5yt1v_5u7Fx5PXnvm1YKJi7TyIHhJI")

@bot.message_handler(commands= ['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Hello, how are you?')


@bot.message_handler(func= lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling()


