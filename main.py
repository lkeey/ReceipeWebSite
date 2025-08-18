from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)
receipes = {}


@app.route("/")
def main():
    return render_template("main.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        confirmed_password = request.form["confirmed_password"]

        if password != confirmed_password:
            return "пароли не совпадают"
        if len(username) < 3:
            return "имя короткое"

        with open("database/users.json", "r") as f:
            users = json.load(f)

        users[username] = {
            "username": username,
            "email": email,
            "password": password,
        }

        with open("database/users.json", "w") as f:
            json.dump(users, f)

        return redirect("/")

    return render_template("register.html")


@app.route("/receipe", methods=["POST", "GET"])
def create_receipe():
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        image_url = request.form["image_url"]
        category = request.form["category"]
        time = request.form["time"]
        portion = request.form["portion"]
        type = request.form["type"]
        ingredients = request.form["ingredients"]

        with open("database/receipes.json", "r") as f:
            receipes = json.load(f)

        receipes[name] = {
            "name": name,
            "description": description,
            "image_url": image_url,
            "category": category,
            "time": time,
            "portion": portion,
            "type": type,
            "ingredients": ingredients.split(", "),
        }

        with open("database/receipes.json", "w") as f:
            json.dump(receipes, f)

        return redirect("/")

    return render_template("create_receipe.html")


if __name__ == "__main__":
    app.run(debug=True, port=8080)
