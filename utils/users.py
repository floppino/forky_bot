import json


with open("utils/users.json", 'r+') as file:
    data = json.load(file)
    data['martiina'] = 147127841298  # <--- add `id` value.
    file.seek(0)  # <--- should reset file position to the beginning.
    json.dump(data, file, indent=4)
    file.truncate()
with open("utils/users.json", 'r+') as file:
    data = json.load(file)
    print(data)