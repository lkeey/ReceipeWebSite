import json

"""
Пользователи
"""

users = {
    "aleksey": {
        "username": "aleksey",
        "email": "l.key14@mail.ru",
        "password": "12345678",
    },
    "maksim": {
        "username": "maksim",
        "email": "maksim@mail.ru",
        "password": "ahwduahwidaiwd",
    },
}

# для добавления данных
with open("database/users.json", "w") as f:
    json.dump(users, f)

# для чтения
with open("database/users.json", "r") as f:
    users_read = json.load(f)
    print("users read:", users_read)


"""
Рецепты
"""

receipes = {
    "лазания": {
        "name": "лазания",
        "description": "крутой рецепт",
        "image_url": "url",
        "category": "лапша",
        "time": 30,
        "portion": 5,
        "type": "средне",
        "ingredients": ["мука", "масло"],
    },
    "борщ": {
        "name": "борщ",
        "description": "крутой борщ",
        "image_url": "url",
        "category": "суп",
        "time": 120,
        "portion": 10,
        "type": "легко",
        "ingredients": ["картофель", "капуста"],
    },
}

with open("database/receipes.json", "w") as file:
    json.dump(receipes, file)

with open("database/receipes.json", "r") as file:
    receipe_read = json.load(file)
    print("receipe read:", receipe_read)
