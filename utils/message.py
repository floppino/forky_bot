from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from utils.get_tok import get_token
from utils.users import get_user, get_users, add_user
import random

TOKEN = get_token()

# Create Updater object and attach dispatcher to it
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher


def start(bot, update):
    user_id = update.message.chat.id
    user_name = update.message.chat.username
    try:
        get_user(user_name)
    except:
        add_user(user_name, user_id)
    update.message.reply_text("Forky is alive!¦8D\nHello {}! How are you? ¦8D".format(user_name))


def mess_handler(bot, update):
    sad_list = ['sad', 'unhappy', 'heartbroken', 'sorry', 'depressed']
    good_list = ['good', 'well', 'fine', 'happy', 'fortunate', 'cheerful', 'joyful']
    greetings_list = ['Hello', 'Hi', 'Greetings', 'Howdy', 'Yo', 'Ciao', 'Hey', 'What\'s up', 'How you doing', 'G’day ']
    no_list = ['no', 'nope', 'nah']
    yes_list = ['yes', 'yeah', 'sure', 'of course', 'si']
    thank_list = ['thank you', 'thanks', 'appreciated', 'nice of you']
    text = update.message.text
    first_name = update.message.from_user.first_name
    lowertext = text.lower()
    if lowertext == 'how am i alive?':
        update.message.reply_text("I don't know ¦8D")
    elif "toy" in lowertext:
        update.message.reply_text(
            """I am not a toy. I was made for soup, salad, maybe chili, and then the trash.\nI'm litter!\nFREEDOM! >8D""")
    elif any(word in lowertext for word in sad_list):
        update.message.reply_text("""{}, somebody’s whispering in your ear.\nEverything is going to be okay ¦8)""".format(
                update.message.from_user.first_name))
    elif any(word in lowertext for word in good_list):
        update.message.reply_text(
            """{}, I'm happy to hear that ¦8)\ndo you want to hear a story??""".format(
                update.message.from_user.first_name))
    elif any(word in lowertext for word in thank_list) or any(word.lower() in lowertext for word in thank_list):
        update.message.reply_text("""{You are very welcome ¦8)""")
    elif any(word in lowertext for word in yes_list):
        update.message.reply_text("""'{}' what? ¦8)""".format(text))
    elif any(word in lowertext for word in no_list):
        update.message.reply_text("""Go fuck yourself ¦8)""".format(text))
    elif 'help' == lowertext:
        update.message.reply_text("These are the many many commands you can use:\n\
            start : to start or restart me\n\
            hug : to receive a special hug\n\
            hi : let me say hello to you!")
    elif 'start' == lowertext:
        user_id = update.message.chat.id
        user_name = update.message.chat.username
        try:
            get_user(user_name)
        except:
            add_user(user_name, user_id)
        update.message.reply_text("Hello {}! How are you? ¦8D".format(first_name))
    elif 'hug' == lowertext:
        update.message.reply_text("Let me give you a warm, cozy and squishy hug! ¦8D")
    elif '?' in lowertext:
        update.message.reply_text("I don't know! ¦8D")
    elif any(word in lowertext for word in greetings_list) or any(word.lower() in lowertext for word in greetings_list):
        greet = random.choice(greetings_list)
        update.message.reply_text('{0} {1} ¦8D'.format(greet, first_name))
    elif 'story' in lowertext:
        update.message.reply_text(
            """Once upon a time there was a spork and it was bought to be used to eat ravioli. After the meal it was then brutally threw in the trash. It was the best trash it could ever asked for. It lived in there happily ever after ¦8D""".format(text))
    else:
        update.message.reply_text(
            """{}, I know what your problem is: you're just like me. Trash!\nJust kidding, ask me anything ¦8D""".format(
                update.message.from_user.first_name))
