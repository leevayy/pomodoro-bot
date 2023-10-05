from bot.botConnection import bot

def start_polling():
    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id,"Привет ✌️ ")
    
    bot.infinity_polling()

if __name__ == "__main__":
    start_polling()

