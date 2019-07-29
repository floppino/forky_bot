from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from utils.get_tok import get_token
from utils.message import mess_handler, start
from utils.spam import send_it
import time
import schedule

# It will get the bot token form the file 'token.txt' that you created with the token in it
TOKEN = get_token()


def main():
    # Create Updater object and attach dispatcher to it
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher
    print("Forky is alive! ¦8D")

    # Dispatchers and handlers
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text, mess_handler))

    # Start the bot
    updater.start_polling()

    schedule.every().hour.do(send_it)

    while True:
        schedule.run_pending()
        time.sleep(1)

    # Run the bot until you press Ctrl-C
    updater.idle()


if __name__ == '__main__':
    main()
