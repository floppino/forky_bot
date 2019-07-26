from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from utils.get_tok import get_token


TOKEN = get_token()


def start(bot, update):
    update.message.reply_text("Spazzaturaaa! 8D")


def hug(bot, update):
    update.message.reply_text("Vengo a darti un abbraccio caldo, sicuro ed un po' umidiccio! 8D")


def alive(bot, update):
    update.message.reply_text("I don't know")


def convert_uppercase(bot, update):
    update.message.reply_text(update.message.text.upper())


def main():
    # Create Updater object and attach dispatcher to it
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher
    print("Forky is here...")

    # Handlers
    start_handler = CommandHandler('start', start)
    hug_handler = CommandHandler('hug', hug)
    alive_handler = CommandHandler('alive', alive)
    upper_case = MessageHandler(Filters.text, convert_uppercase)

    # Dispatchers
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(hug_handler)
    dispatcher.add_handler(alive_handler)
    dispatcher.add_handler(upper_case)

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()


if __name__ == '__main__':
    main()
