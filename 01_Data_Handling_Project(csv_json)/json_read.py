import json

with open('users.json', 'r') as file:
    users_data = json.load(file)

for user in users_data['users']:
    print(user['name'], user['age'])