import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
from bot_commands import *
from telegram import ReplyKeyboardMarkup

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
# updater = Updater('5839806750:AAHa-DvgcG_BcCswZwkvpUTRaTpC9CEcCP4')

# updater.dispatcher.add_handler(CommandHandler('hi',  hi_command))
# updater.dispatcher.add_handler(CommandHandler('time',time_command))
# updater.dispatcher.add_handler(CommandHandler('help',help_command))
# updater.dispatcher.add_handler(CommandHandler('sum',sum_command))
# updater.dispatcher.add_handler(CommandHandler('exchange',exchange_Rates))


# print('server is starting')
# updater.start_polling()
# updater.idle()


def start(update: Update, context: CallbackContext) -> None:
    """Sends a message with three inline buttons attached."""

    update.message.reply_text('выбирите тип информаций:',
                              reply_markup = keyboard_main_menu())


def main_menu(update: Update, context: CallbackContext) -> None:
    """ Displays the main menu keyboard when called. """

    query = update.callback_query
    query.answer()
    query.edit_message_text(text         = 'выбирите тип информаций :',
                            reply_markup = keyboard_main_menu())


def keyboard_main_menu():
    """ Creates the main menu keyboard """

    keyboard = [
        [InlineKeyboardButton("Курс валют", callback_data='1'),
         InlineKeyboardButton("Конвертор валют", callback_data='2'),],
    ]

    return InlineKeyboardMarkup(keyboard)


def confirm(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""

    query = update.callback_query
    query.answer()

    keyboard = [
        [InlineKeyboardButton("Да", callback_data=f'YES{query.data}'),
         InlineKeyboardButton("Нет",  callback_data='main'),],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text(text=f"Выбранно {query.data}."
                                 f"Вы уверенны ? ",
                            reply_markup=reply_markup)


def do_action_1(update: Update, context: CallbackContext) -> None:

    keyboard = [[InlineKeyboardButton("Основное меню", callback_data='main')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    query = update.callback_query
    query.answer()
    query.edit_message_text(text=f"Выбранно опция {query.data}\n",
                                 
                            reply_markup=reply_markup)
    


def do_action_2(update: Update, context: CallbackContext) -> None:

    keyboard = [[InlineKeyboardButton("Основное меню", callback_data='main')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    query = update.callback_query
    query.answer()
    query.edit_message_text(text=f"Выбранно опция {query.data}\n",
                                 
                            reply_markup=reply_markup)


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("5839806750:AAHa-DvgcG_BcCswZwkvpUTRaTpC9CEcCP4")

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
    updater.dispatcher.add_handler(CallbackQueryHandler(confirm, pattern='^(|1|2)$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(do_action_1, pattern='YES1'))
    updater.dispatcher.add_handler(CallbackQueryHandler(do_action_2, pattern='YES2'))
   


    # Start the Bot
    updater.start_polling()
    print('started')

if __name__ == '__main__':
    main()



