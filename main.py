from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)
receipes = {}


@app.route("/<user_name>")
@app.route("/")
def main(user_name="none"):
    with open("database/receipes.json", "r") as f:
        receipes = json.load(f)

    return render_template(
        "main.html", receipes=receipes, size=len(receipes.keys()), user_name=user_name
    )


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

        return redirect(f"/{username}")

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


@app.route("/like/<user_name>/<receipe_name>", methods=["POST"])
def like(user_name, receipe_name):
    with open("database/receipes.json", "r") as f:
        receipes = json.load(f)

    if "likes" not in receipes[receipe_name]:
        receipes[receipe_name]["likes"] = [user_name]
    else:
        if user_name in receipes[receipe_name]["likes"]:
            receipes[receipe_name]["likes"].remove(user_name)
        else:
            receipes[receipe_name]["likes"].append(user_name)

    with open("database/receipes.json", "w") as f:
        json.dump(receipes, f, ensure_ascii=False, indent=4)

    return str(len(receipes[receipe_name].get("likes", [])))


@app.route("/profile/<user_name>", methods=["GET"])
def profile(user_name):
    liked_receipes = {}

    with open("database/receipes.json", "r") as f:
        receipes = json.load(f)

    for receipe in receipes:
        if ("likes" in receipes[receipe]) and (user_name in receipes[receipe]["likes"]):
            liked_receipes[receipe] = receipes[receipe]

    return liked_receipes
    # return render_template("profile.html", liked_receipes=liked_receipes)


@app.route("/receipe/<receipe_name>/<user_name>", methods=["GET"])
def detail_receipe(receipe_name, user_name):
    with open("database/receipes.json", "r") as f:
        receipes = json.load(f)

    if receipe_name in receipes:
        current_receipe = receipes[receipe_name]
        return render_template(
            "detail_receipe.html",
            receipe=current_receipe,
            user_name=user_name,
            key=receipe_name,
        )
    else:
        return "Рецепт не найден"


if __name__ == "__main__":
    app.run(debug=True, port=8080)
