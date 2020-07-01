import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo, pymongo
import bcrypt
from bson.objectid import ObjectId 
import json
if os.path.exists("env.py"):
  import env 
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'recipes_manager'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
app.secret_key = "cocina"

mongo = PyMongo(app)

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



@app.route('/login', methods=['GET', 'POST'])
def login():
   
    logged_in = False
    if request.method == 'GET' and not 'username' in session:
        return render_template('login.html',
                               logged_in=logged_in)
    elif request.method == 'GET' and 'username' in session:
        logged_in = True
        recipes = mongo.db.recipes.find()
        
        recipes_dict = {}
        
        for i, recipe in enumerate(recipes):
            recipe.pop('_id', None)
            recipes_dict[i] = recipe
        
        recipes_dict = json.dumps(recipes_dict)

        return render_template('login.html',
                               username=session['username'],
                               logged_in=logged_in,
                               recipes=recipes_dict)
    if request.method == 'POST':
        session['username'] = request.form["username"]
        logged_in = True
        recipes=mongo.db.recipes.find()
        recipes_dict = {}
        
        for i, recipe in enumerate(recipes):
            recipe.pop('_id', None)
            recipes_dict[i] = recipe
        
        recipes_dict = json.dumps(recipes_dict)
            
        return render_template('login.html',
                              username=session['username'],
                              logged_in=logged_in,
                              recipes=recipes_dict)


@app.route('/logout')
def logout():
        print('logged out')
        session.clear()
        return redirect(url_for('home'))


@app.route('/my_recipes', methods=['GET', 'POST'])
def my_recipes():
    if not 'username' in session:
        return redirect('/login')
    else:
        recipes = mongo.db.recipes.find()
        return render_template('my_recipes.html',
                           username=session['username'],
                           recipes=recipes)


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))


@app.route('/add_recipe')
def add_recipe():
    if 'username' in session:
        return 'You are logged in as ' + session['username']

    return render_template('add_recipe.html', categories=mongo.db.categories.find())



if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', 5000)),
            debug=True)