import telebot
from config import TOKEN
from utilits import ConversionException, CryptoConverter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу, введите команду боту в следующем формате в следующем формате:\n<имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты> \
<например: USD RUB 100>\nУвидеть список всех доступных валют: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Вам доступно 167 валют, признаных ООН стран!'
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    values = message.text.split(' ')
    try:
        if len(values) != 3:
            raise ConversionException('Неправильные параметры параметры.')

        quote, base, amount = values
        total = CryptoConverter.convert(quote, base, amount)
    except ConversionException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total['conversion_result']}'
        bot.send_message(message.chat.id, text)

bot.polling()