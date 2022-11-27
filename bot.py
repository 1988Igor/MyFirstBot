import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from bot_commands import *
from telegram import ReplyKeyboardMarkup
updater = Updater('5839806750:AAHa-DvgcG_BcCswZwkvpUTRaTpC9CEcCP4')

updater.dispatcher.add_handler(CommandHandler('hi',  hi_command))
updater.dispatcher.add_handler(CommandHandler('time',time_command))
updater.dispatcher.add_handler(CommandHandler('help',help_command))
updater.dispatcher.add_handler(CommandHandler('sum',sum_command))
updater.dispatcher.add_handler(CommandHandler('exchange',exchange_Rates))

print('server is starting')
updater.start_polling()
updater.idle()




