import telebot
from telebot import types
import requests
import json
from telegram import *
from telegram.ext import*
from requests import*
from datetime import date
import datetime

TOKEN = '5839806750:AAHa-DvgcG_BcCswZwkvpUTRaTpC9CEcCP4'
bot = telebot.TeleBot(TOKEN)
new_line = '\n'
@bot.message_handler(commands=['start'])
def start(message):
    markup =types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('💱 Курсы валют')
    item2 = types.KeyboardButton('💱 Конвертор валют')

    markup.add(item1, item2)

    bot.send_message(message.chat.id, 'Привет 👋 , {0.first_name}! "\n" Ниже в меню можно выбрать тип информации который ты хочешь получить '. format(message.from_user), reply_markup=markup)


def main_menu(message):
    markup =types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('💱 Курсы валют')
    item2 = types.KeyboardButton('💱 Конвертор валют')

    markup.add(item1, item2)

    bot.send_message(message.chat.id, '{0.first_name} вы находитесь в основное меню '. format(message.from_user), reply_markup=markup)





@bot.message_handler(content_types=['text']) 
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == '💱 Конвертор валют':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('Назад')
            item1 = types.KeyboardButton('€ EUR')
            item2 = types.KeyboardButton('$ USD')
            item3 = types.KeyboardButton('₼ AZN')
            item4 = types.KeyboardButton('₣ CHF')
            item5 = types.KeyboardButton('₺ TRY')
            item6 = types.KeyboardButton('£ GBP')
            markup.add(item1, item2, item3, item4, item5, item6, back)
            msg = bot.send_message(message.chat.id, 'Выберите валюту', reply_markup=markup)
            bot.register_next_step_handler(msg, currency)
        elif message.text == '💱 Курсы валют':
            Exchage_Rates(message)
        else:
                
                currency(message)
            # msg2 = bot.send_message(message.chat.id, 'h' )
            # bot.register_next_step_handler(msg2, Exchage_Rates, )





def currency(message):
   
        if message.text == '€ EUR':
                msg = bot.send_message(message.chat.id, 'Введите сумму в рублях') 
                bot.register_next_step_handler(msg, eur) 
        elif message.text == '$ USD':
                msg = bot.send_message(message.chat.id, 'Введите сумму в рублях')
                bot.register_next_step_handler(msg, usd)
        elif message.text == '₼ AZN':
                msg = bot.send_message(message.chat.id, 'Введите сумму в рублях')
                bot.register_next_step_handler(msg, azn)
        elif message.text == '₣ CHF':
                msg = bot.send_message(message.chat.id, 'Введите сумму в рублях')
                bot.register_next_step_handler(msg, chf)
        elif message.text == '₺ TRY':
                msg = bot.send_message(message.chat.id, 'Введите сумму в рублях')
                bot.register_next_step_handler(msg, _try)
        elif message.text == '£ GBP':
                msg = bot.send_message(message.chat.id, 'Введите сумму в рублях')
                bot.register_next_step_handler(msg, gbp)
        elif message.text == 'Назад':
            main_menu(message)
                # msg = bot.send_message(message.chat.id,' confirm one more time')
                # bot.register_next_step_handler(msg, start )
        else:
                msg = bot.send_message(message.chat.id, 'Введите корректные данные')
                bot.register_next_step_handler(msg, currency)

def eur(message):    
    r = requests.get('https://www.cbr-xml-daily.ru/latest.js')
    texts = json.loads(r.content)
    Rates = texts.get('rates')
    EUR = float(Rates.get('EUR'))
    print(EUR)
    try:
        amount = int(message.text) 
    except:
        bot.send_message(message.chat.id, " Вы ввели не число")
    total = float(round((amount*EUR),2)) # находим нужное количество
    result = f'{amount} рублей  =  {total} EUR' # выводим результат
   
    bot.send_message(message.chat.id, result)

def usd(message):
    r1 = requests.get('https://www.cbr-xml-daily.ru/latest.js')
    texts1 = json.loads(r1.content)
    Rates1 = texts1.get('rates')
    USD = float(Rates1.get('USD'))
    print(USD)
    amount1 = int(message.text) # конвертируем входящие данные в число
    total1 = float(round((amount1*USD),2)) # находим нужное количество
    result1 = f'{amount1} рублей = {total1} USD' # выводим результат
    
    bot.send_message(message.chat.id, result1)

def azn(message):
    r2 = requests.get('https://www.cbr-xml-daily.ru/latest.js')
    texts2 = json.loads(r2.content)
    Rates2 = texts2.get('rates')
    AZN = float(Rates2.get('AZN'))
    print(AZN)
    amount2 = int(message.text) # конвертируем входящие данные в число
    total2 = float(round((amount2*AZN),2)) # находим нужное количество
    result2 = f'{amount2} рублей = {total2} AZN' # выводим результат
   
    bot.send_message(message.chat.id, result2)


def chf(message):
    r3 = requests.get('https://www.cbr-xml-daily.ru/latest.js')
    texts3 = json.loads(r3.content)
    Rates3 = texts3.get('rates')
    CHF = float(Rates3.get('CHF'))
    print(CHF)
    amount3 = int(message.text) # конвертируем входящие данные в число
    total3 = float(round((amount3*CHF),2)) # находим нужное количество
    result3 = f'{amount3} рублей = {total3} CHF' # выводим результат
  
    bot.send_message(message.chat.id, result3)

def _try(message):
    r4 = requests.get('https://www.cbr-xml-daily.ru/latest.js')
    texts4 = json.loads(r4.content)
    Rates4 = texts4.get('rates')
    TRY = float(Rates4.get('TRY'))
    print(TRY)
    amount4 = int(message.text) # конвертируем входящие данные в число
    total4 = float(round((amount4*TRY),2)) # находим нужное количество
    result4 = f'{amount4} рублей = {total4} TRY' # выводим результат
    
    bot.send_message(message.chat.id, result4)

def gbp(message):
    r5 = requests.get('https://www.cbr-xml-daily.ru/latest.js')
    texts5 = json.loads(r5.content)
    Rates5 = texts5.get('rates')
    GBP = float(Rates5.get('GBP'))
    print(GBP)
    amount5 = int(message.text) # конвертируем входящие данные в число
    total5 = float(round((amount5*GBP),2)) # находим нужное количество
    result5 = f'{amount5} рублей = {total5} GBP' # выводим результат
   
    bot.send_message(message.chat.id, result5)
  

def Exchage_Rates(message):
    r8 = requests.get('https://www.cbr-xml-daily.ru/latest.js')
    texts8 = json.loads(r8.content)
    Rates8 = texts8.get('rates')
    Valutes = str(round(Rates8.get('USD'),3))+"\b"f'USD '
    Valutes1 =str(round(Rates8.get('EUR'),3))+"\b"f'EUR '
    Valutes2 =str(round(Rates8.get('AZN'),3))+"\b"f'AZN '
    Valutes3 =str(round(Rates8.get('CHF'),3))+"\b"f'CHF '
    Valutes4 =str(round(Rates8.get('TRY'),3))+"\b"f'TRY'
    Valutes5 =str(round(Rates8.get('GBP'),3))+"\b"f'GBP'
    new_line = '\n'
 
    all_currencies = f'1 рубль (RUB) на сегодняшний день {date.today()} равен : {new_line} {Valutes} {new_line} {Valutes1} {new_line} {Valutes2} {new_line} {Valutes3} {new_line} {Valutes4} {new_line}  {Valutes5}'
     
    bot.send_message(message.chat.id, all_currencies)



bot.polling(none_stop=True)