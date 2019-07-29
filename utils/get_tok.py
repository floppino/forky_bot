# Function to get the bot token


def get_token():
    with open("utils/token.txt", 'rt') as file:
        token = file.read()
    return token
