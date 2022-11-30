import telebot 
from telebot import TeleBot, types
bot =  telebot.TeleBot('5839806750:AAHa-DvgcG_BcCswZwkvpUTRaTpC9CEcCP4')


import requests
import json




# @bot.message_handler(commands=['start', 'help'])
# def help(message: telebot.types.Message):
#     text = 'Валютные операции /conversion'
#     bot.reply_to(message,text)
 
@bot.message_handler(content_types=['text']) 
def start(message):
        if message.text == '/start':
                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                markup.row('€ EUR', '$ USD', '₼ AZN', '₣ CHF', '₺ TRY', '£ GBP')
                msg = bot.send_message(message.chat.id, 'Выберите валюту', reply_markup=markup)
                bot.register_next_step_handler(msg, currency)

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
    result = f'{amount} рублей равно {total} EUR' # выводим результат
   
    bot.send_message(message.chat.id, result)

def usd(message):
    r1 = requests.get('https://www.cbr-xml-daily.ru/latest.js')
    texts1 = json.loads(r1.content)
    Rates1 = texts1.get('rates')
    USD = float(Rates1.get('USD'))
    print(USD)
    amount1 = int(message.text) # конвертируем входящие данные в число
    total1 = float(round((amount1*USD),2)) # находим нужное количество
    result1 = f'{amount1} рублей равно {total1} USD' # выводим результат
    
    bot.send_message(message.chat.id, result1)

def azn(message):
    r2 = requests.get('https://www.cbr-xml-daily.ru/latest.js')
    texts2 = json.loads(r2.content)
    Rates2 = texts2.get('rates')
    AZN = float(Rates2.get('AZN'))
    print(AZN)
    amount2 = int(message.text) # конвертируем входящие данные в число
    total2 = float(round((amount2*AZN),2)) # находим нужное количество
    result2 = f'{amount2} рублей равно {total2} AZN' # выводим результат
   
    bot.send_message(message.chat.id, result2)


def chf(message):
    r3 = requests.get('https://www.cbr-xml-daily.ru/latest.js')
    texts3 = json.loads(r3.content)
    Rates3 = texts3.get('rates')
    CHF = float(Rates3.get('AZN'))
    print(CHF)
    amount3 = int(message.text) # конвертируем входящие данные в число
    total3 = float(round((amount3*CHF),2)) # находим нужное количество
    result3 = f'{amount3} рублей равно {total3} CHF' # выводим результат
  
    bot.send_message(message.chat.id, result3)

def _try(message):
    r4 = requests.get('https://www.cbr-xml-daily.ru/latest.js')
    texts4 = json.loads(r4.content)
    Rates4 = texts4.get('rates')
    TRY = float(Rates4.get('TRY'))
    print(TRY)
    amount4 = int(message.text) # конвертируем входящие данные в число
    total4 = float(round((amount4*TRY),2)) # находим нужное количество
    result4 = f'{amount4} рублей равно {total4} TRY' # выводим результат
    
    bot.send_message(message.chat.id, result4)

def gbp(message):
    r5 = requests.get('https://www.cbr-xml-daily.ru/latest.js')
    texts5 = json.loads(r5.content)
    Rates5 = texts5.get('rates')
    GBP = float(Rates5.get('GBP'))
    print(GBP)
    amount5 = int(message.text) # конвертируем входящие данные в число
    total5 = float(round((amount5*GBP),2)) # находим нужное количество
    result5 = f'{amount5} рублей равно {total5} GBP' # выводим результат
   
    bot.send_message(message.chat.id, result5)
  


bot.polling()
       
