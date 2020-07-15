
# [COCINA](https://recipes-manager-flask-mongo.herokuapp.com/) - Data Centric Project

## Table of Contents

- [**About**](#About)
- [**UX**](#UX)
  - [User Stories](#User-Stories)
  - [Design Development](#Design-Development)
  - [Wireframes](#Wireframes)
- [**Database Structure**](#Database-Structure)
- [**Features**](#Features)
  - [Existing Features](#Existing-Features)
  - [Features Left To Implement](#Features-Left-To-Implement)
- [**Technologies Used**](#Technologies-Used)
  - [Version Control](#Version-Control)
  - [Hosting](#Hosting)
- [**Testing**](#Testing)
  - [Tests Performed](#Tests-Performed)
  - [Known issue list](#Known-Issue-List)
  - [Code Validation](#Code-Validation)
- [**Deployment**](#Deployment)
  - [Live App Link](#Live-App-Link)
  - [Repository Link](#Repository-Link)
  - [Running Code Locally](#Running-Code-Locally)
- [**Credits**](#Credits)
  - [Content](#Content)
  - [Acknowledgements](#Acknowledgements)
  - [Disclaimer](#Disclaimer)

## About

Cocina is an online cookbook web application. It’s a place where users can add, edit, share and deletes their own recipes, as well as browse other users’ recipes for inspiration - all in one place.

In order to utilise their personal cookbook, users can register with their name, email and password in a secure manner. Once registered, users can log in and manage their cookbook.

The aim of the site for the owner is to promote their range of cooking tools and utensils while providing a place for users to get inspired to cook and create and manage their own cookbook. All this is met by providing this functional and easy to use web application.

Users will be able to manage their own profiles and recipes, through the implementation of CRUD (Create, Read, Update and Delete) operations.


### Project Rational

This app was created for the Data-Centric Development project of Code Institute Full Stack Software Development course. The project scope was to create a web app using Python and a no-SQL database (MongoDB), which uses CRUD operations to allow users to easily create, read, update and delete data from a database viewed through a web application.

This was developed as both a front-end and backend project. The technologies used for each are:
- Frontend: HTML, CSS, JavaScript
- Backend: Python, Flask, MongoDB
- Hosting: Heroku
- Database: MongoDB


## UX

### User Stories

“As a user_____”

- I often find myself on the lookout for recipe inspiration to cook at home.
- I’m passionate about cooking and I want to keep my recipes online in one place.
- I want to be able to share my recipes easily online with family and friends.
- I’m a very busy person - I would like to organise and manage my recipes for the week, sorting them by the 3 meals a day, to have them accessible on my mobile, and go shopping knowing what I’m going to cook each week.
- I’m new to cooking - I want to be able to easily find recipes, and add and manage my own recipes as I discover them.
- I want to be able to share my own recipes for others to try them.
- I live abroad - I would like to store the recipes my mother has given me online, so I can have them with me all the time on the go.


### Design Development

The direction taken for styling this web app was to prioritise a minimal design, which is easy and pleasant to read and navigate, as well as being responsive to provide the best possible user experience. 

**Primary Colour Palette** 

The colour palette was chosen to create a minimalist and unisex experience. A simple and earthy colour palette was chosen, to complement the vivid food photography images.

![Primary Colour Palette](static/images/colourpalette.jpg)

**Fonts**

This font was used for all titles and subtitles on the app.

Font-family: 'Libre Baskerville', serif.


**Responsivity**

This website is fully responsive on all screen sizes and devices, making the app easy to navigate.  


### Wireframes

Wireframes were developed using Adobe XD. This was a personal choice as I find it to be a rapid and iterative process for developing wireframes.  

The links to these images are available at the following links:


- [**_Wireframe 1_**](static/images/wireframe-homepage.jpg)

- [**_Wireframe 2_**](static/images/wireframe-allrecipes.jpg)

- [**_Wireframe 3_**](static/images/wireframe-addrecipeform.jpg)

- [**_Wireframe 4_**](static/images/wireframe-viewrecipe.jpg)

- [**_Wireframe 5_**](static/images/mobile-viewrecipe.jpg)

- [**_Wireframe 6_**](static/images/mobile-login.jpg)

- [**_Wireframe 7_**](static/images/mobile-allrecipes.jpg)

- [**_Wireframe 8_**](static/images/mobile-addrecipeform.jpg)


### Database Structure

The data is organised on MongoDB in four collections: Recipes, Categories, Cooking_tools and User.

DB Collections: 

```console
recipes: {
_id: 5d433657ddab2ebc9620c441
recipe_name: "string"
category_name: "string"
tool_name: "string"
author: "string"
image: "https://greenkitchenstories.com/"
reecipe_description: "string"
time: 30
serves: 4
ingredients: "string"
method: "string"
recipe_added_by: "string"
recipe_added_by_user: "string"
}

```

```console
categories: {
_id: 5d2dff3f9398ee10830e15f7
category_name: "lunch"
}

```

```console
cooking_tools: {
_id: 5d2dff3f9398ee10830e15f7
tool_name: "string"
Tool_image: "https://images.unsplash.com/photo.jpg&crop=alyson-mcphee-unsplash.jpg"
tool_description: "string"
tool_url: "https://www.ikea.com/gb/en/p/aptitlig-chopping-board-bamboo-80233430/"
}

```

```console
users: {
_id: 5d2dff3f9398ee10830e15f7
name: "string"
email: "string"
password: "string"
}

```


## Features

### Existing Features

**Login**

- Users can create an account and log in. This gives registered users the possibility to add recipes, edit them and delete them.

**Account management**

- Users can see and edit their account and change their information.
- Users have the possibility to delete their account.

**Recipes**

- Registered users are able to create, edit and delete recipes.
- All users and unregistered visitors can browse the full database and access all recipes.

**Registered users**

- Registered users have access to functionalities reserved only to them, such as
- Creating and editing a recipe
- Deleting a recipe
- Editing and deleting their account

**Kitchen tools promotion**

- When users a recipe, users are prompted to choose required kitchen tools from a dropdown menu.
- All kitchen tools are linked to the site owners range of cooking tools (in this case, IKEA) to promote the brand.
- The “Cooking tools” page displays all listed kitchen tools in the database.

**Recipe count feature**

- On the Homepage, there is a functionality that counts the total number of recipes added to the database, by all users.


### Features Left to Implement

- **Rating Recipes** - Add a feature for users to rate recipes. I would like to develop a rating feature which gives an average rating based on all likes against a recipe and display that average as a number or star rating on each listing.

- **Search or sort by recipe categories feature** - Add a feature to sort all recipes by categories or via a search bar by typing keywords. 

- **Statistics** - Expand on the recipe count feature to include more data points about the recipes (for example: time to cook, number of ingredients needed).

- **Add Reviews**  - Develop a feature for users to be able to add text reviews, comments and questions to each recipe to potentially be answered by the site owner or the user who added the recipe. This would be a great way for users to interact with each other.

- **Share** - Have an option for users to share directly from each recipe to a social media account, or by email, WhatsApp or other sharing apps. This could be developed using available APIs. This could make the app more sociable, with the ability to share easily with one click.


## Technologies Used

- [**HTML**](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
    - **HTML** Used for markup.
- [**CSS**](https://developer.mozilla.org/en-US/docs/Web/CSS)
    - **HTML** Used for markup.
- [**Materialize**](https://materializecss.com/)
    - The project uses the **Materialize** framework to add a responsive grid system, prebuilt components, plugins built on jQuery, and Materialize styles to my app, before adding my custom styles.
- [**jQuery**](https://jquery.com)
    - The project uses **jQuery** jQuery, to access and manipulate the DOM.
- [**Python**](https://www.python.org/)
    - The project uses **Python** for all backend logic.
- [**PyMongo**](https://api.mongodb.com/python/current/)
    - The project uses **PyMongo** as the Python API for MongoDB. This API enables linking the data from the back-end database to the front-end app.
- [**Werkzeug**](https://palletsprojects.com/p/werkzeug/)
    - The project uses **Werkzeug** Werkzeug is a python library which contains tools for implementation of secure user authentication system using python werkzeug. It will store secure passwords with salted hashes and later it will verify entered user password in plaintext against its password hash to authenticate the user.
- [**Flask**](https://flask.palletsprojects.com/en/1.0.x/)
    - The project uses **Flask**, which is a Python microframework.
- [**Jinja**](https://jinja.palletsprojects.com/en/2.10.x/)
    - The project uses **Jinja** for templating with Flask in the HTML code. I used **Jinja** to simplify my HTML code, avoid repetition, and allow simpler linking of the back-end to the front-end.
- [**MongoDB**](https://cloud.mongodb.com/)
    - The project uses **MongoDB** to store the database in the cloud. The information displayed in the front-end app is pulled and stored in and from the database.
- [**Font Awesome**](https://fontawesome.com/)
    - The project uses **Font Awesome** for all icons in my app.
- [**VScode**](https://code.visualstudio.com/)
    - Visual Studio Code was my IDE of choice for this project.

### Version Control

- [**Git**](https://git-scm.com/)
    - I've used **Git** as a version control system to regularly add and commit changes made to project and pushing them to GitHub.
- [**GitHub**](https://github.com/)
    - I've used **GitHub** as a remote repository to push and store the committed changes to my project from Git.

### Hosting
- [**Heroku**](https://www.heroku.com/)
    - I've used **Heroku** as the hosting platform to deploy my app.

## Testing

This app has been manually tested extensively during the development process. When bugs and errors were found I have either fixed them or noted them for later review.

Each time I introduce a new feature, change something or fix a bug, I have attempted to break the app when possible.

As this is my first Flask app developed by me, a number of issues were significant during the development process and required me to use mainly Stack Overflow to help me find solutions. Examples: getting file paths right, generating a system for the user to login with password, errors implementing jinja templates with my python code.

Extensive testing was required, and accessing pages from different starting points, registered and unregistered.

Tested mobile responsiveness in Chrome Dev Tools and on my iPhone and Ipad.

Testing planning, implementation, results and outcomes are described in detail, either in the readme, or a separate file.

### Tests Performed

- Navigation:
    - Regardless of what the user attempts to do, there's never the need to click the 'back' button to return to a page. Clicking either a button or a menu item would bring the user to their required spot in the app.
    - The “All recipes” page successfully displays all recipes from the database and can be seen by all users.
    - The “Cooking tools” page displays information from the database correctly.
    - The “My profile” page correctly displays information about a user account, update and delete buttons are available.

- Forms:
    - Forms are clear and explain what to do with them. Filling the form, dropdown menus work properly. When trying to submit the form without required fields it won’t allow it, it will indicate to fill the required fields.
    - Adding recipe: this only appears on the navbar when the user is logged in, once filling all the required fields on the “Add recipe” form, the user is redirected to the “All Recipes” page, where the newly added recipe will be displayed.
    - The “Update recipe” form displays current recipe information, then clicking on the edit button correctly updates the document.

- User:
    -Registering a new user works correctly, redirects to the homepage and displays a message letting the user know they are logged in. When trying to create a username that already exists, the message display advises to try another name.
    - When attempting to login with wrong credentials, a message appears suggesting username or password are incorrect.
    - Logging out redirects successfully to the homepage, a message is displayed informing the user that they have been logged out of their account.
    - Logged out users don’t have access to functionalities reserved only for logged in users, such as adding, editing or deleting recipes.

- Buttons and links:
    - Deleting a document always deletes the proper one selected by the user and identified by its ObjectId.
    - Edit buttons bring user successfully to the correct pages and forms.
    - Click on a recipe 'view recipe', redirects me to the single selected recipe page, when the user logged in, edit and delete buttons are available.
    - When performing specific actions I successfully get flash messages with correct feedback.

The testing of the site was extensive. As described above, I worked through all of these features to ensure all are working well. All actions performed by the add, edit, read and delete functionality are successfully reflected on both the front-end and the back-end on the database in MongoDB.

For the functionality just mentioned, I didn’t encounter any bugs. I also got a second person to test the same features mentioned above and no bugs were found.


### Known issue list

1. **Image:** I had an issue with allowing users to upload images to Heroku and MongoDB. Images did not display, causing an error.

    **Temporary solution:** I implemented a required field where users can put a URL link to an image. This seems to work fine, for now - images display properly without breaking.

    Ideally, later I would like to work on this to develop a better function to store images on a cloud for users to be able to upload images from their computers.

2. **Users:** During testing, I realised any user can edit or delete other users recipes.

    **Solution:** I didn’t have time but later I would like to further develop the existing function on my python code to specify that recipes can only be edited or deleted by the specific user who adds them. 

3. **Alerts and messages:** Initially I tried printing messages on different actions on the python code but this didn’t work properly, I tried looking at implementing javascript alerts but some didn’t display at all, leaving the user without any feedback on their actions.

    **Temporary solution:** I made use of flash messages - this seems to work very well for now. In the future, I would like to develop a better solution using javascript functionalities, as this means my python functions are sometimes focused on two tasks at the same time, rather than one, which may cause errors.

4. **Loading and resizing images:** Despite using frameworks like Materialised to ensure responsiveness, some images didn’t resize properly and are slow to load when the page is first opened. This is due to the images being heavy and loading time taking longer.

    **Solution:** In the future, I want to implement a cloud-based API, such as Cloudinary, for faster loading and resizing of images.


### Code Validation

- I used the [W3C HTML Validator tool](https://validator.w3.org/#validate_by_input) to validate my HTML code.
    - The validator doesn’t recognise the Jinja template. No other errors found.
- I used the [W3C CSS Validator tool](https://jigsaw.w3.org/css-validator/#validate_by_input) to validate my CSS code.
- I used the [Esprima Syntax Validator tool](http://esprima.org/demo/validate.html) to validate my JavaScript syntax.
- I used the [Pep8 Online tool](http://pep8online.com/) to validate my Python syntax.
    - Line too long, for now, this doesn’t affect functionality. One example is the second line in app.py importing the libraries from flask.


## Deployment 


#### Database Setup

Create database on MongoDB

Get data in place first, on atlas mongo website:
* Database with four collections: categories, cooking_tools, recipes and user
* Create a sample record in category collection called category_name: "Lunch"
* Create sample record in the cooking_tools collection with tool_name, tool_image, tool_description, tool_url
* Create sample record in the recipes collection with recipe_name, category_name, recipe_description, image, serves, method, ingredients
* Create sample record in the user collection with username, email, password


#### Setup using VS Code on a Mac using the terminal window

* **sudo pip3 install Flask** to install Flask
* **python3 -m venv env** to install virtual environment in that folder
* Open command palette, type **Python: Select Interpreter** and select the virtual environment in your project folder that starts with ./env or .\env
* In command pallette, run **Terminal: Create New Integrated Terminal**
* Install Flask in the virtual environment with **pip3 install Flask**
* **pip3 install flask_pymongo**
* Create app.py (In flask, the convention is to use run.py or app.py)
* **from flask import Flask** to import Flask in app.py Capital F indicates a class name.
* Create instance of flask within app.py with **app = Flask(name)**
* In Terminal **python3 app.py run** to run the app and serve

#### Deploying to Heroku

I used GitHub for my version control and Heroku to host the live version of my project. To deploy my app to Heroku, I used the following steps:

1. Created the app in Heroku.
2. Run the `brew tap heroku/brew && brew install heroku` command in the terminal window if using Mac to install heroku in my local workspace.
3. Run `heroku login` command in the terminal window and entered my credentials to login to Heroku.
4. Added and committed the files to Git using the `git add .` and `git commit -m ""` commands in the terminal window.
5. Linked the Heroku app as the remote master branch using the following command in the terminal window:

    ```heroku git:remote -a recipes-manager-flask-mongo```

6. Created a requirements.txt file using the following command in the terminal window:

    ```pip3 freeze --local > requirements.txt```

7. Created a Procfile using the following command in the terminal window:

    ```echo web: python app.py > Procfile```

8. Run the `git push heroku master` command in the terminal window to push the app to Heroku.
9. Run the `heroku: ps:scale web=1` command in the terminal window to run the app in Heroku.
10. Entered the following Config Var in Heroku:

    ```MONGO_URI : "mongodb+srv://root:r00tUser@myfirstcluster-naitp.mongodb.net/recipes_manager?retryWrites=true&w=majority"```

11. On Heroku web interface: Specify IP 0.0.0.0 and Port 5000


The app was successfully deployed to Heroku at this stage.



##### Connecting to MongoDB Atlas

    sudo pip3 install flask-pymongo
    
    
in new file env.py:
	import os
os.environ["MONGO_URI"] = "mongodb+srv://root:r00tUser@myfirstcluster-naitp.mongodb.net/recipes_manager?retryWrites=true&w=majority"


in app.py this will read the needed variables from the env.py file, created above):

	from os import path 
	if path.exists("env.py"):
    import env

    from flask_pymongo import PyMongo
    from bson.objectid import ObjectId

	app.config["MONGO_DBNAME"] = 'recipes_manager'
    app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')


On Mongo Website: Overview -> Connect -> Connect my app -> Choose Python3.6 or later

Copy connection string

Paste in connection string

**Ensure an environment variable for above is used when in production**

Create an instance of pymongo, add app with constructor method.

    mongo = Pymongo(app)


 #### <a name="local-deployment"></a> Local Deployment 

With the above setup, to deploy locally on a mac:

1. Open a terminal for the virtual environment where the project resides
2. Type python3 app.py 
3. Browse to http://0.0.0.0:5000/ 

### Live Version App Link

Click the link below to run my project in the live environment:

[COCINA](https://recipes-manager-flask-mongo.herokuapp.com/)

### Repository Link

Click the link below to visit my project's GitHub repository:

[COCINA](https://github.com/GiselleNessi/cocina-recipes-app-manager)

### Running Code Locally

To run the code locally, users can download a local copy of my code to their desktop by completing the following steps:

1. Go to (https://github.com/GiselleNessi/cocina-recipes-app-manager)
2. Click on 'Clone or Download' under the repository name.
3. Copy the clone URL for the repository in the 'Clone with HTTPs section'.
4. Open 'Terminal' in your local IDE.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, then paste the URL you copied in Step 3:

    ```git clone https://github.com/USERNAME/REPOSITORY```

7. Press `Enter` to complete the process and create your local clone.
8. Create a new Database in MongoDB  
9. Create collections 
9. Navigate to the `.bashrc` terminal and add your MongoDB URI in the following format:

    ```MONGO_URI="insert your mongo uri details here"```

10. In the terminal, run the `pip3 install -r requirements.txt` command to install the requirements.txt file.
11. You should now be able to run the app locally using the `python3 app.py` command.

## Credits

- All of the code was written by the author and inspired on occasions by freely available tutorials, instructional documentation and open source examples.
- Sources of information, inspiration and to sort problems are [Stack Overflow](https://stackoverflow.com/) and [W3Schools](https://www.w3schools.com/).
- This video was used to understand the general idea of how to create a register and login system [Login Video](https://www.youtube.com/watch?list=PLXmMXHVSvS-Db9KK1LA7lifcyZm4c-rwj&v=vVx1737auSE&app=desktop) 
- This article was helpful to implement messages in the app. [Flash Messages Article](https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/).


### Content

The recipe content for the app was taken from (https://greenkitchenstories.com/) and other text created by the author

Kitchen tools promotion was taken from the IKEA website for the purpose of this project only (https://www.ikea.com/gb/en/cat/kitchen-appliances-ka001/)

### Media

All the images for this app were taken from 

[**_Unsplash_**](https://unsplash.com/)

[**_Green Kitchen Stories_**](https://greenkitchenstories.com/)


### Acknowledgements

Thank you to the tutoring team for their invaluable support in guiding me through the issues I had.

Thank you to my mentor, Rohit, for his review of my project.


### Disclaimer

This project is for educational purposes only not intended commercial use in any way.

<div align="right">
    <b><a href="#table-of-contents">↥ Back To Top</a></b>
</div>
