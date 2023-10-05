from bot.botConnection import bot

def start_polling():
    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id,"Привет ✌️ ")
    
    bot.infinity_polling()

def send_work_message(chat_id: str):
    bot.send_message(chat_id, f'Время для работы! ⏰')
    
def send_chill_message(chat_id: str):
    bot.send_message(chat_id, f'Время отдыхать! 🌊')

if __name__ == "__main__":
    start_polling()

