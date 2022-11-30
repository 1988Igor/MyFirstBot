import telebot 
from telebot import TeleBot, types
bot =  telebot.TeleBot('5839806750:AAHa-DvgcG_BcCswZwkvpUTRaTpC9CEcCP4')

# USD = 74.24
# EUR = 90.77
# GBP = 95.65

import requests
import json

r = requests.get('https://www.cbr-xml-daily.ru/latest.js')
texts = json.loads(r.content)
Rates = texts.get('rates')
# #print(Rates)
global EUR
USD = str(Rates.get('USD'))
EUR= str(Rates.get('EUR'))
GBP = str(Rates.get('GBP'))
# #/start - выбор валют - вводит сумму в рублях 
# print(EUR)
class ConvertionException(Exception):
    pass
@bot.message_handler(content_types=['text']) 
def start(message):
        if message.text == '/start':
                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                markup.row('€ EUR', '$ USD', 'AZN', 'CHF', 'TRY', 'GBP')
                msg = bot.send_message(message.chat.id, 'Выберите валюту', reply_markup=markup)
                bot.register_next_step_handler(msg, currency)

def currency(message):
        if message.text == '€ EUR':
                msg = bot.send_message(message.chat.id, 'Введите сумму в рублях') 
                bot.register_next_step_handler(msg, eur) 
        elif message.text == 'USD':
                msg = bot.send_message(message.chat.id, 'Введите сумму в рублях')
                bot.register_next_step_handler(msg, usd)
        elif message.text == 'GBP':
                msg = bot.send_message(message.chat.id, 'Введите сумму в рублях')
                bot.register_next_step_handler(msg, gbp)
        else:
                msg = bot.send_message(message.chat.id, 'Введите корректные данные')
                bot.register_next_step_handler(msg, currency)

def eur(message):
    r = requests.get('https://www.cbr-xml-daily.ru/latest.js')
    texts = json.loads(r.content)
    Rates = texts.get('rates')
    EUR = float(Rates.get('EUR'))
    print(EUR)
    amount = float(message.text) # конвертируем входящие данные в число
    total = float(round((amount*EUR),2)) # находим нужное количество
    result = f'{amount} Рублей равно {total} EUR' # выводим результат
    if type(amount) == str:
        raise ConvertionException(f'Не удалось обработать количество {amount}')
 
    bot.send_message(message.chat.id, result)



# def eur(message):
#         try:
#                 bot.send_message(message.chat.id, float(message.text) / EUR)
#         except ValueError:
#                 bot.send_message(message.chat.id, 'Введите число')

def usd(message):
        try:
                bot.send_message(message.chat.id, float(message.text) / USD)
        except ValueError:
                bot.send_message(message.chat.id, 'Введите число')
def gbp(message):
        try:
                bot.send_message(message.chat.id, float(message.text) / GBP)
        except ValueError:
                bot.send_message(message.chat.id, 'Введите число') 




bot.polling()
       

