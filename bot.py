import telegram

def main():
    # Membuat instance dari bot dengan menggunakan API token yang diberikan oleh @BotFather
    bot = telegram.Bot(token='5976026050:AAEjIf0VZ9LqK5-adpVQ08NAJlcJs2OpJ20')

    # Memeriksa apakah ada pesan yang masuk
    updates = bot.get_updates()
    for update in updates:
        # Jika pesan yang masuk adalah perintah "/start", maka bot akan mengirim pesan kembali kepada pengguna yang mengirimkan perintah tersebut
        if update.message.text == '/start':
            bot.send_message(chat_id=update.message.chat_id, text="Halo! Saya adalah bot yang dibuat dengan menggunakan GitHub dan Telegram.")

if __name__ == '__main__':
    main()
