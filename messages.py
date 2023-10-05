from telebot import types


def commands(message, bot):
    text = message.text.split()[0][1:]
    arg = 0
    if text in ['work', 'rest']:
        try:
            arg = int(message.text.split()[1])
        except IndexError:
            text = 'incorrect time'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    ans = 'incorrect input'
    match text:
        case 'start':
            btn1 = types.KeyboardButton('Старт таймера')
            btn2 = types.KeyboardButton('Настройки таймера')
            markup.add(btn1, btn2)
            ans = f'Привет {message.from_user.first_name}! Готов работать?'

        case 'work':
            # Добавить перенос данных в БД
            btn1 = types.KeyboardButton('Назад')
            markup.add(btn1)
            ans = f'Вы установили время работы - {arg} минут'

        case 'rest':
            # Добавить перенос данных в БД
            btn1 = types.KeyboardButton('Назад')
            markup.add(btn1)
            ans = f'Вы установили время отдыха - {arg} минут'

    bot.send_message(message.chat.id, text=ans, reply_markup=markup)


def reply(message, bot):
    user_ans = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    ans = "incorrect input"
    match user_ans:
        case 'Настройки таймера':
            btn1 = types.KeyboardButton('Время работы')
            btn2 = types.KeyboardButton('Время отдыха')
            markup.add(btn1, btn2)
            ans = 'Какой параметр вы хотите поменять?'

        case 'Время работы':
            btn1 = types.KeyboardButton('Назад')
            markup.add(btn1)
            ans = 'Установите время работы командой /work'

        case 'Время отдыха':
            btn1 = types.KeyboardButton('Назад')
            markup.add(btn1)
            ans = 'Установите время работы командой /rest'

        case 'Старт таймера':
            btn1 = types.KeyboardButton('Стоп')
            markup.add(btn1)
            ans = 'Таймер запущен'

        case 'Назад' | 'Стоп':
            btn1 = types.KeyboardButton('Старт таймера')
            btn2 = types.KeyboardButton('Настройки таймера')
            markup.add(btn1, btn2)
            ans = f'Работа таймера приостановлена'

    bot.send_message(message.chat.id, text=ans, reply_markup=markup)
