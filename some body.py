import telebot
import wikipedia
import keep_alive


bot= telebot.TeleBot("")
@bot.message_handler(content_types=['text'])

def start(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Напиши мне слово, и я дам тебе его значения!")
    else:
        get_text_message(message)

def get_text_message(message):
    try:
        wikipedia.set_lang("ru")
        bot.send_message(message.from_user.id, wikipedia.summary(str(message.text)))
    except:
        bot.send_message(message.from_user.id, "Проверь корректность написанного тобой слова, либо же такого слова нету!")


keep_alive.keep_alive()


bot.polling(none_stop=True, interval=0)












