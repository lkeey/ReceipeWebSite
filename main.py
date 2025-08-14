from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(debug=True, port=8080)
