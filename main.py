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

if __name__ == "__main__":
    start_polling()

