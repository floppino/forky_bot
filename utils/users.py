import json


def get_user(user_name):
    with open("utils/users.json", 'r+') as file:
        data = json.load(file)
        user_id = data[user_name]
        file.truncate()
        return user_id


def add_user(user_name, user_id):
    with open("utils/users.json", 'r+') as file:
        data = json.load(file)
        data[user_name] = user_id
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()


def get_users():
    with open("utils/users.json", 'r+') as file:
        users = []
        data = json.load(file)
        for user in data:
            users.append(user)
        file.truncate()
        return users
