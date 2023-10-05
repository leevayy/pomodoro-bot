import telebot
from  telebot import types
BOT_TOKEN = open('BOT_TOKEN.txt').readline()
print(BOT_TOKEN)
test = '5331015593:AAFKPyLXfkBN8TSCi0Ik_5qZP7LMJkaCxOM'
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Старт таймера')
    btn2 = types.KeyboardButton('Настройки таймера')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text=f'Привет {message.from_user.first_name}! Готов работать?', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def reply(message):
    ans = message.text
    if ans == 'Настройки таймера':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Время работы')
        btn2 = types.KeyboardButton('Время отдыха')
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text=f'Какой параметр вы хотите поменять?', reply_markup=markup)

    elif ans == 'Время работы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)
        bot.send_message(message.chat.id, text='Установите время работы командой /work', reply_markup=markup)

    elif ans == 'Время отдыха':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)
        bot.send_message(message.chat.id, text='Установите время работы командой /rest', reply_markup=markup)

    elif ans == 'Старт таймера':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Стоп')
        markup.add(btn1)
        bot.send_message(message.chat.id, text='Таймер запущен', reply_markup=markup)

    elif ans == 'Назад' or ans == 'Стоп':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Старт таймера')
        btn2 = types.KeyboardButton('Настройки таймера')
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text=f'Работа таймера приостановлена', reply_markup=markup)


bot.infinity_polling()