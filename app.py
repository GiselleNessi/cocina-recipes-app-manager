# app.py
# Project "COCINA" Python/Flask/MongoDB web application built by Giselle Chacon Nessi, ©Giselle Chacon 2020
#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
import os
import json
from functools import wraps
from flask import Flask, render_template, redirect, request, url_for, session, flash, Markup
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#
app = Flask(__name__)
# Environment variables SECRET and MONGO_URI set in Heroku dashboard in production
app.config["MONGO_DBNAME"] = 'recipes_manager'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
app.secret_key = "cocina"

mongo = PyMongo(app)
user = mongo.db.user


def find_user(username):
    """Finds user from database matching the username """
    return user.find_one({"username": username})


# Home Page route
@app.route('/')
@app.route('/home')
def home():
    """Renders the index page with homepage information"""
    return render_template('index.html')


@app.route('/index')
def index():
    """
    Renders the index page with homepage information
    Includes counter function to display the total number of recipes
    added to database by all users
    """
    recipes = list(mongo.db.recipes.find())
    cursor = mongo.db.recipes.find({}, {'_id': 0, "username": 1,
                                        "recipe_name": 1, "category_name": 1,
                                        "tool_name": 1, "author": 1,
                                        "time": 1, "serves": 1,
                                        "recipe_added_by_username": 1})
    total_recipes = cursor.count()
    return render_template('index.html', recipes=recipes, total_recipes=total_recipes)


# Get recipes
@app.route('/get_recipes', methods=['GET', 'POST'])
def get_recipes():
    """
    Displays all recipes added by all users
    Collections should be display by category name
    """
    return render_template("recipes/recipes.html", recipes=mongo.db.recipes.find())


# Add recipes
@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    """
    Renders a form to allow user to add a new recipe to the database.
    """
    recipes = mongo.db.recipes.find()
    categories = mongo.db.categories.find()
    cooking_tools = mongo.db.cooking_tools.find()
    return render_template(
        'recipes/add_recipe.html', categories=categories, cooking_tools=cooking_tools, recipes=recipes)


# Insert recipes
@app.route('/insert_recipe', methods=['GET', 'POST'])
def insert_recipe():
    """
    Insert the new document into the database 
    and then redirect to the get recipe page
    """
    if request.method == 'POST':
        user = session['user'].lower()
        user_id = find_user(user)["_id"]
        recipes = mongo.db.recipes
        insert = {
            'recipe_name': request.form.get('recipe_name'),
            'category_name': request.form.get('category_name'),
            'tool_name': request.form.get('tool_name'),
            'author': request.form.get('author'),
            'image': request.form.get('image'),
            'recipe_description': request.form.get('recipe_description'),
            'time': request.form.get('time'),
            'serves': request.form.get('serves'),
            'ingredients': request.form.get('ingredients'),
            'method': request.form.get('method'),
            'recipe_added_by': user_id,
            'recipe_added_by_username': user
        }
        new_recipe = recipes.insert_one(insert)
        user = mongo.db.user
        user.update(
            {"_id": ObjectId(user_id)},
            {"$push": {"add_recipe": new_recipe.inserted_id}}
        )

    return redirect(url_for('get_recipes'))


# Edit recipes
@app.route('/edit_recipe/<recipes_id>', methods=['GET', 'POST'])
def edit_recipe(recipes_id):
    """
    Render a form to allow user to edit a selected recipe.
    """
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipes_id)})
    categories = mongo.db.categories.find()
    cooking_tools = mongo.db.cooking_tools.find()
    return render_template('recipes/edit_recipe.html', recipes=the_recipe,
                           categories=categories, cooking_tools=cooking_tools)


# Update recipes
@app.route('/update_recipe/<recipes_id>', methods=['GET', 'POST'])
def update_recipe(recipes_id):
    """
    Insert the updated document into database
    then redirects to getrecipe page
    """
    recipes = mongo.db.recipes
    user = session['user'].lower()
    user_id = find_user(user)["_id"]
    recipes.update({'_id': ObjectId(recipes_id)},
    {
        'recipe_name': request.form.get('recipe_name'),
        'category_name': request.form.get('category_name'),
        'tool_name': request.form.get('tool_name'),
        'author': request.form.get('author'),
        'image': request.form.get('image'),
        'recipe_description': request.form.get('recipe_description'),
        'time': request.form.get('time'),
        'serves': request.form.get('serves'),
        'ingredients': request.form.get('ingredients'),
        'method': request.form.get('method'),
        'recipe_added_by': user_id,
        'recipe_added_by_username': user
    })
    return redirect(url_for('get_recipes'))


# View recipes
@app.route('/view_recipe/<recipes_id>', methods=['GET', 'POST'])
def view_recipe(recipes_id):
    """
    Shows the selected recipe details
    Renders the recipe on the viewrecipe page. 
    """
    recipes = mongo.db.recipes.find_one({"_id": ObjectId(recipes_id)})
    categories = mongo.db.categories.find()
    cooking_tools = mongo.db.cooking_tools.find()
    return render_template('recipes/view_recipe.html', recipes=recipes, categories=categories, cooking_tools=cooking_tools)


# Delete recipes
@app.route('/delete_recipe/<recipes_id>', methods=['GET', 'POST'])
def delete_recipe(recipes_id):
    """
    Deletes a document/recipe found through its ObjectId
    from the database.
    """
    mongo.db.recipes.remove({'_id': ObjectId(recipes_id)})
    return redirect(url_for('get_recipes'))


# Cooking tools page
@app.route('/cooking_tools')
def cooking_tools():
    """
    Renders cooking tools page
    showing the collection from the database.
    """
    return render_template('recipes/cooking_tools.html', cooking_tools=mongo.db.cooking_tools.find())


# Login Page feature
@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Renders form to log in user includes data required 
    to only allow correct user information
    """
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
                "Hey, Welcome " + username.capitalize() + ", you are logged in"))
            session["user"] = username
            return redirect(url_for('index', username=session["user"]))

        else:
            # Login validation
            flash(Markup(
                "Those details do not match our records," + "either try again or register for an account."))
        return redirect(url_for('login'))

    return render_template('user/login.html')


# Register Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Renders form to register a new user, if the form validates
    It checks the database to prevent the creation of a
    duplicate (already existing) username.
    """
    if request.method == 'POST':
        # Add new user, lower case the name for access logic
        new_user = request.form.get('new_user').lower()
        new_pass = request.form.get('new_pass')
        new_email = request.form.get('new_email')
        reg_user = find_user(new_user)
        # Error handling
        if reg_user:
            flash(Markup(
                "The username " + new_user + " is already taken, please try another name"))
            return redirect(url_for('register'))
        # insert items to the database
        user.insert_one({
            "username": new_user,
            "password": generate_password_hash(new_pass),
            "email": new_email,
        })
        # Add new_user to session and display message
        session["user"] = new_user
        flash(Markup("Welcome aboard, " + new_user.capitalize() +
                     "<br>" + "Thanks for registering with us! You can login now"))

        return redirect(url_for('index', username=session["user"]))

    return render_template("user/register.html")


# Log out
@app.route('/logout')
def logout():
    """
    Logs user out, clear user session and redirect to index/homepage
    """
    session.pop('user', None)
    flash('You\'re outta here!')
    return redirect(url_for('index'))


# Account page
@app.route('/profile/<username>', methods=["GET", "POST"])
def profile(username):
    """ 
    Queries the database to check if the user is loged in,
    then shows profile page with use information.
    If not, redirects to index page
    """
    user = mongo.db.user
    if 'user' in session:
        # if the user is in session return profile.html for that user
        user_in_db = user.find_one({"username": username})
        return render_template('user/profile.html', user=user_in_db)
    else:
        return redirect(url_for('index'))


# Edit profile
@app.route('/edit_profile/<user_id>', methods=["GET", "POST"])
def edit_profile(user_id):
    """
    Allows to edit the account information 
    updating the account from the database.
    """
    the_user = mongo.db.user.find_one({"_id": ObjectId(user_id)})
    return render_template('user/edit_profile.html', user=the_user)


# Update profile
@app.route('/update_profile/<user_id>', methods=["GET", "POST"])
def update_profile(user_id):
    """
    Replaces the current information with the new information
    added by user from the database.
    """
    user = mongo.db.user
    new_pass = request.form.get('new_pass')
    user.update({'_id': ObjectId(user_id)}, {
        'username': request.form.get('new_user'),
        "password": generate_password_hash(new_pass),
        "email": request.form.get('new_email'),
    })
    return redirect(url_for('login'))


# Delete Profile
@app.route('/delete_account/<user_id>', methods=["GET", "POST"])
def delete_account(user_id):
    """
    Delete the current user
    Finds the current user in the database and removes it
    """
    user = session['user'].lower()
    delete_user = mongo.db.user
    delete_user.remove({'_id': ObjectId(user_id)})
    session.clear()
    flash(Markup(
        user.capitalize() + " Has left... Good Bye"))
    return redirect(url_for('index'))

# Run app
if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', 5000)),
            debug=False)
