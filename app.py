import os
from flask import Flask, render_template, redirect, request, url_for, session, flash, Markup
from functools import wraps
from flask_pymongo import PyMongo, pymongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId 
import json
if os.path.exists("env.py"):
  import env 


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'recipes_manager'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
app.secret_key = "cocina"

mongo = PyMongo(app)

#Database refeerences
user = mongo.db.user


# Quick functions
def find_user(username):
    return user.find_one({"username": username})


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())


@app.route('/index')
def index():
    recipes = list(mongo.db.recipes.find().sort(
        "views", pymongo.DESCENDING).limit(4))
    return render_template('index.html', recipes=recipes)


@app.route('/view_recipe/<recipes_id>')
def view_recipe(recipes_id):
    recipes = mongo.db.recipes.find_one({"_id": ObjectId(recipes_id)})
    return render_template('view_recipe.html', recipes=recipes)



@app.route('/edit_recipe/<recipes_id>')
def edit_recipe(recipes_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipes_id)})
    all_categories = mongo.db.categories.find()
    return render_template('edit_recipe.html', recipes=the_recipe,
                           categories=all_categories)


@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html', categories=mongo.db.categories.find())



@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))

#sign up feature

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    # if the request method is post then return then login.html
    if request.method == "POST":
        # Get form elemnts
        username = request.form.get('username')
        password = request.form.get("user_password")
        reg_user = find_user(username)
        # User and password check
        if reg_user and check_password_hash(reg_user["password"], password):
            # Confirmation message
            flash(Markup(
                "Hey, Welcome "
                + username.capitalize() +
                ", you are logged in"))
            session["user"] = username
            return redirect(url_for('index', username=session["user"]))

        else:
            # Login validation
            flash(Markup(
                "Those details do not match our records," +
                "either try again or register for an account."))
        return redirect(url_for('login'))

    return render_template('login.html')


# Register Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        # Add new user, lower case the name for access logic

        new_user = request.form.get('new_user').lower()
        new_pass = request.form.get('new_pass')
        new_email = request.form.get('new_email')
        reg_user = find_user(new_user)

        # Error handling

        if reg_user:
            flash(Markup(
                "The username " + new_user +
                " is already taken, please try another name"))
            return redirect(url_for('register'))

        # insert items to the database
        user.insert_one({
            "username": new_user,
            "password": generate_password_hash(new_pass),
            "email": new_email,
        })

        # Add new_user to session and display message
        session["user"] = new_user
        flash(Markup("Welcome aboard, "
                     + new_user.capitalize() +
                     "<br>" +
                     "You're now part of the team, and logged in!"))

        return redirect(url_for('index', username=session["user"]))

    return render_template("register.html")



if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', 5000)),
            debug=True)