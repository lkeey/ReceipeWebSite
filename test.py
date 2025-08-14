import json

user = {
    "username": "aleksey",
    "email": "l.key14@mail.ru",
    "password": "12345678",
}

# для добавления данных
with open("database/users.json", "w") as f:
    json.dump(user, f)

# для чтения
with open("database/users.json", "r") as f:
    users_read = json.load(f)
    print("users read:", users_read)


# receipe = {
#     "name": "",
#     "description": "",
#     "image_url": "",
#     "category": "",
#     "time": 30,
#     "portion": 5,
#     "type": "",
#     "ingredients": ["мука", "масло"],
# }
