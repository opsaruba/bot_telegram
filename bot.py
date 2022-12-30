import telebot

# inisialisasi Token Bot Kita
bot = telebot.TeleBot('5976026050:AAEjIf0VZ9LqK5-adpVQ08NAJlcJs2OpJ20')

# Menghandle Pesan /start
@bot.message_handler(commands=['start'])
def welcome(message):
    # membalas pesan
    bot.reply_to(message, 'Halo bro, ada apa?')

while True:
    try:
        bot.polling()
    except:
        pass
