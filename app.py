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


@app.route('/index')
def index():
    recipes = list(mongo.db.recipes.find().sort(
        "views", pymongo.DESCENDING).limit(4))
    return render_template('index.html', recipes=recipes)


#Get recipes
@app.route('/get_recipes', methods=['GET', 'POST'])
def get_recipes():
    return render_template("recipes/recipes.html", recipes=mongo.db.recipes.find())

#Add recipes
@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    recipes = mongo.db.recipes.find()
    categories = mongo.db.categories.find()
    cooking_tools = mongo.db.cooking_tools.find()
    return render_template(
        'recipes/add_recipe.html', categories=categories, cooking_tools=cooking_tools, recipes=recipes)

#Insert recipes
@app.route('/insert_recipe', methods=['GET', 'POST'])
def insert_recipe():
    if request.method == 'POST':
        user = session['user'].lower()
        user_id = find_user(user)["_id"]
        recipes = mongo.db.recipes
        insert = {
            'recipe_name':request.form.get('recipe_name'),
            'category_name':request.form.get('category_name'),
            'tool_name': request.form.get('tool_name'),
            'author':request.form.get('author'),
            'image': request.form.get('image'),
            'recipe_description': request.form.get('recipe_description'),
            'time': request.form.get('time'),
            'serves': request.form.get('serves'),
            'ingredients':request.form.get('ingredients'),
            'method':request.form.get('method') ,
            "recipe_added_by": user_id,
            "recipe_added_by_username": user
        }
        new_recipe = recipes.insert_one(insert)
        user = mongo.db.user
        user.update(
            {"_id": ObjectId(user_id)},
            {"$push": {"add_recipe": new_recipe.inserted_id}}
        )

    return redirect(url_for('get_recipes'))

#Edit recipes
@app.route('/edit_recipe/<recipes_id>', methods=['GET', 'POST'])
def edit_recipe(recipes_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipes_id)})
    categories = mongo.db.categories.find()
    cooking_tools = mongo.db.cooking_tools.find()
    return render_template('recipes/edit_recipe.html', recipes=the_recipe,
                           categories=categories, cooking_tools=cooking_tools)

# Update recipes
@app.route('/update_recipe/<recipes_id>', methods=['GET', 'POST'])
def update_recipe(recipes_id):
    recipes = mongo.db.recipes
    recipes.update({'_id': ObjectId(recipes_id)},
    {
        'recipe_name':request.form.get('recipe_name'),
        'category_name':request.form.get('category_name'),
        'tool_name': request.form.get('tool_name'),
        'author':request.form.get('author'),
        'image': request.form.get('image'),
        'recipe_description': request.form.get('recipe_description'),
        'time': request.form.get('time'),
        'serves': request.form.get('serves'),
        'ingredients':request.form.get('ingredients'),
        'method':request.form.get('method') ,
        'recipe_added_by': user_id,
        'recipe_added_by_username': user,
    })
    return redirect(url_for('get_recipes'))

#View recipes
@app.route('/view_recipe/<recipes_id>', methods=['GET', 'POST'])
def view_recipe(recipes_id):
    recipes = mongo.db.recipes.find_one({"_id": ObjectId(recipes_id)})
    categories = mongo.db.categories.find()
    cooking_tools = mongo.db.cooking_tools.find()
    return render_template('recipes/view_recipe.html', recipes=recipes, categories=categories, cooking_tools=cooking_tools)


@app.route('/cooking_tools')
def cooking_tools():
    return render_template('recipes/cooking_tools.html', cooking_tools=mongo.db.cooking_tools.find())

#Delete recipes
@app.route('/delete_recipe/<recipes_id>', methods=['GET', 'POST'])
def delete_recipe(recipes_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipes_id)})
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

    return render_template('user/login.html')


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

    return render_template("user/register.html")


# Log out
@app.route('/logout')
def logout():
    # Clear the session
    session.pop('user', None)
    flash('You\'re outta here!')
    return redirect(url_for('index'))


# Account page
@app.route('/profile/<username>', methods=["GET", "POST"])
def profile(username):
    # Check if user is logged in
    if 'user' in session:
        # if the user is in session return profile.html for that user
        user_in_db = user.find_one({"username": username})
        return render_template('user/profile.html', user=user_in_db)
    else:
        return redirect(url_for('index'))


# Edit profile
@app.route('/edit_profile/<user_id>', methods=["GET", "POST"])
def edit_profile(user_id):
    the_user = mongo.db.user.find_one({"_id": ObjectId(user_id)})
    return render_template('user/edit_profile.html', user=the_user)


# Update profile
@app.route('/update_profile/<user_id>', methods=["GET", "POST"])
def update_profile(user_id):
    user = mongo.db.user
    new_pass = request.form.get('new_pass')
    user.update({'_id': ObjectId(user_id)}, {
        'username': request.form.get('new_user'),
        "password": generate_password_hash(new_pass),
        "email": request.form.get('new_email'),
        "add_recipe": []
    })
    return redirect(url_for('logout'))


# Delete Profile
@app.route('/delete_account/<user_id>', methods=["GET", "POST"])
def delete_account(user_id):
    user = session['user'].lower()
    delete_user = mongo.db.user
    delete_user.remove({'_id': ObjectId(user_id)})
    session.clear()
    flash(Markup(
        user.capitalize() + " Has left... Good Bye"))
    return redirect(url_for('index'))




if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', 5000)),
            debug=True)