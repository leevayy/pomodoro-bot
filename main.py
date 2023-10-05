from bot.botConnection import bot
import messages

def start_polling():
    @bot.message_handler(commands=['start', 'work', 'rest'])
    def start_message(message):
        messages.commands(message, bot)

    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        messages.reply(message, bot)
    
    bot.infinity_polling()

def send_work_message(chat_id: str):
    bot.send_message(chat_id, f'Время для работы! ⏰')
    
def send_chill_message(chat_id: str):
    bot.send_message(chat_id, f'Время отдыхать! 🌊')

if __name__ == "__main__":
    start_polling()

