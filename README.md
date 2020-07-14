
# [COCINA](https://recipes-manager-flask-mongo.herokuapp.com/) - Data Centric Project

![COCINA]IMAGE HERE


## Table of Contents

- [**About**](#About)
- [**UX**](#UX)
  - [User Stories](#User-Stories)
  - [Design Development](#Design-Development)
  - [Wireframes](#Wireframes)
  - [Database Structure](#Database-Structure)
- [**Features**](#Features)
  - [Functionality](#Functionality)
  - [Existing Features](#Existing-Features)
  - [Features Left To Implement](#Features-Left-To-Implement)
- [**Technologies Used**](#Technologies-Used)
  - [Version Control](#Version-Control)
  - [Hosting](#Hosting)
- [**Testing**](#Testing)
  - [Testing User Stories](#Testing-User-Stories)
  - [Responsive and Functional Testing](#Responsive-and-Functional-Testing)
  - [Additional Testing](#Additional-Testing)
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

Cocina is an online cookbook web application. It’s a place where users can add, edit, share and deletes their own recipes as well as browse other users recipes for inspiration all in on place.
In order to add, edit and store recipes, users can register with their name, email and password in a save manner. Once registered users can loggin and manage their cookbook.

The aim of the site from the owner and is to promote owners cooking tools and utensil while providing a place for users, to get inspired to cook and create and manage their own cookbook all this is met by providing this functional and easy to use web application.

Users will be able to perform CRUD (Create, Read, Update and Delete) profiles and recipes. Users will be able to update all their recipes once they are signed up and logged in.

A free to join site that brings people together and allows them to share their passion for cooking.


### Project Rational

This app was created for the Data-Centric Development project of Code Institute Full Stack Software Development course. The project scope was to create a web app using Python and a no-SQL database (MongoDB), which uses CRUD operations to allow users to easily create, read, update and delete data from a database viewed through a web application

This was developed as both a front-end and backend project. The technologies used for each are:
- Frontend: HTML, CSS, JavaScript
- Backend: Python, Flask, MongoDB
- Hosting: Heroku
- Database: MongoDB

## UX

### User Stories

“As a user_____”

- I often find myself on the lookout for recipe inspirations to cook at home
- I’m passionate about cooking, I want to keep my recipes online in one place
- I want to be able to share my recipes easily online with family and friends
- I’m a very busy person, I would like to organize and manage my recipes for the week, sorting them by the 3 meals a day, to have them accessible on my mobile, and go shopping knowing what I’m going to cook each week
- I’m new to cooking, I want to be able to easily find recipes, and add and manage my own recipes as a cook them
- I want to be able to share via link my own recipes for others to try them
- I live abroad, I would like to keep the recipes my mom send me online so I can have them with me all the time on the go



### Design Development

The direction taking for styling this web app was to prioritise a minimal design, easy to read, navigate and to be responsive. Providing the best user expirience possible together with a pleasent user interface to navigate to.

Primary Colour Palette: 

The colour palette was chosen to create an elegant and minimalistic approach. The vivid colour that comes from the food photography combine with a beautiful and simple colour palette for a unisex feel yet an earthy feeling of healthy foods.

![Primary Colour Palette](static/images/colourpalette.jpg)

Fonts

Font-family: 'Libre Baskerville', serif; from google fonts.


Responsivity

This website is fully responsive to all screen sizes and devices, making the app easy to navigate. 


### Wireframes

Wireframes where developed usgin Adobe XD. A personal choice as I find it a rapid and iterative process for me to develop wireframes.  

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

The data is organized on MongoDB in four collections: Recipes, Categories, Cooking_tools and User.

Main goal when designing the database was to keep it simple to deliver the best result.

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

### Functionality

This app makes use of Python logic to enable users to register and/or login with a private account. The CRUD features are available using Python and MongoDB, allow users to create, read, update and delete records in a variety of manners:

- Create recipes
- Read recipes
- Update their recipes
- Delete their recipes
- Create a secure user account
- Update their profile account
- Read their profile information
- Delete their user account


### Existing Features

**Navbar Links** 
The navbar contains the following links to all users:

- Branding Icon( Also home button )
- Home Button
- All Recipes button (this page has a list of all the added recipes by all users)
- Cooking Tools 
- Login (Authorization checks are used to check that the username and password ( password is hashed ) with the details checked against the stored values in the database before users are logged in.)
- Register (Facility to allow new users to register for an account. Checks are in place to ensure that the username doesn't already exist in the database before users are successfully registered. The passwords stored in the database are hashed for security purposes.)

When the user is registered and logged in, the navbar will add buttons for Account, Add Recipe and Log out, the navbar will remove login and register buttons from the UI.

**Navbar Links logged in**

The following are the nav bar links available when a user is logged in:

- Branding Icon (Also a home button)
- Home Button
- All Recipes button
- Cooking Tools button
- My Profile Button (to take the user to their specific profile page)
    - Edit Account Details - Assuming a user exists, then the user will have the facility to update their user profile account details, this will update on the database as well.
    - Delete Account - Feature allows user to delete their account. This will perform the action of removing the entire set of user details from the database.
- Add Recipe Button ( this feature is only available to registered users to be able to add their own recipes. This listing data is then posted to the MongoDB database for retrieval in the All Recipes page.)
    - Edit Recipes - This feature allows registered and logged in users to edit their recipes. This action updates the selected recipe from the database.
    - Remove Recipes - This feature allows registered and logged in users to delete their recipes. This action removes the selected recipe from the database.
- Logout - Allows users to log out of their account by clicking the 'Logout' link in the navbar. Upon clicking the button, the user session ends.


### Features Left to Implement

- **Rating Recipes** - To add a feature for users to rate recipes. I would like to develop a rating feature to give an average rating based on all likes against a listing id and display that average as a number or star icons on each listing.

- **Search or sort by recipe categories feature** - Add feature to sort all recipes by categories or via a search bar typing key words. 

- **Add Reviews**  - Develop a feature for users to be able to add text reviews, comments and questions to each recipes to potentially be answer by the site owneer or user who added recipe. This would be a great way for users to interact with each other.

- **Share** - Have an option for users to share directly from each recipe to social media account, or by email, whatsapp and diferent apps. This could be develop connecting each app API provided. this could make the app more connected with the ability to share easily with one click.


## Technologies Used

- [**HTML**](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
    - This project makes use of **HTML** as the main structural element of the app.
- [**Materialize**](https://materializecss.com/)
    - The project uses the **Materialize** framework to add a responsive grid system, prebuilt components, plugins built on jQuery, and Materialize styles to my app, before adding my custom styles.
- [**jQuery**](https://jquery.com)
    - The project uses **jQuery** as the primary JavaScript functionality. This is both the standard jQuery that is built with Materialize components, and my custom jQuery used in my script.js file.
- [**Python**](https://www.python.org/)
    - The project uses **Python** as the back-end programming language for my app.
- [**PyMongo**](https://api.mongodb.com/python/current/)
    - The project uses **PyMongo** as the Python API for MongoDB. This API enables linking the data from the back-end database to the front-end app.
- [**Werkzeug**](https://palletsprojects.com/p/werkzeug/)
    - The project uses **Werkzeug** Werkzeug is a python library which contains tools for implementation of secure user authentication system using python werkzeug. It will store secure passwords with salted hashes and later it will verify entered user password in plaintext against its password hash to authenticate the user.
- [**Flask**](https://flask.palletsprojects.com/en/1.0.x/)
    - The project uses **Flask**, which is a Python microframework.
- [**Jinja**](https://jinja.palletsprojects.com/en/2.10.x/)
    - The project uses **Jinja** for templating with Flask in the HTML code. I used **Jinja** to simplify my HTML code, avoid repetition, and allow simpler linking of the back-end to the front-end.
- [**MongoDB**](https://cloud.mongodb.com/)
    - The project uses **MongoDB** to store the database in the cloud. The information displayed in the front-end app is pulled and store in and from the database.
- [**Font Awesome**](https://fontawesome.com/)
    - The project uses **Font Awesome** for the various icons in my app.
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

### Testing User Stories
The testing of users stories consisted of:

1. Creating a new account - Register functionality
2. Log in - can the user log back in - Login functionality
3. Logging out - can the user log out - Logout functionality
4. Create - Add a recipe - can the user add a new recipe - Add recipe Functionality
5. Read - Can a user read/view their newly added recipe - Read functionality
6. Update - Edit a recipe - can a user edit a recipe - Edit recipe functionality
7. Delete a recipe - can a user delete a recipe - Delete recipe functionality
8. Feedback - does the user get the flashed messages to provide feedback
9. Read - Can a user read their account information - Read My Profile Functionality
10. Update - can a user update their account information - Edit My Profile functionality
11. Delete - Can a user delete their account - Delete My Profile functionality
12. Navigation Navbar - can a user navigate the site through full-screen and mobile view navigation at the navbar
13. Navigation Footer - can a user navigate the site through the footer
14. All recipes - user can see all recipes added by all users as a directory of recipes.


The testing of the site was extensive. As described above, I worked through all of those features to ensure all features are working well.

For the functionality just mentioned I didn’t encounter any bugs. I also got 1 more person to test the site using the above features and no bugs where found.


### Responsive and Functional Testing
- I tested my apps responsiveness on different devices; Mobile, Tablet and Desktop to ensure that the responsiveness worked and the site is functional at all sizes.
- Tested on Desktop (MacBook Pro)
- Tested on Tablet (Ipad using Chrome and Firefox)
- Tested on Mobile (iPhone using Chrome and Safari)


### Functionality

For testing of functionality, I have tested it myself trying each of the features on diferent devices.

#### Tesing included:
- Navbar Links
- Logo link
- Pages arrow click for reverse information
- All hyperlinks 
- All buttons on all elements
- Contact Form for sending an email
- Flashed messages for user feedback
- Footer navigation


### Additional Testing
- I used the developer tools with Chrome to check each of my styling, responsiveness and errors. This ensured that I identified and was able to modify errors and bugs quickly, and bring those edits back into VScode.

- I created several users and when through each of the available functionalities:
    - Registering
    - Login
    - Signing out
    - Editing account information
    - Deleting an account
    - Adding a recipe
    - Editing a recipe
    - Deleting a recipe
    - Creating a meeting
    - Navigation links
    - Buttons
    - Links
    - Sidenav for mobile screens
    - Flashed messages for user feedback
    - Footer Navigation


I asked a few friends to do the same along the way to capture any issues and debug them as well as providing feedback.


### Code Validation

- I used the [W3C HTML Validator tool](https://validator.w3.org/#validate_by_input) to validate my HTML code.
    - The validator doesn’t recognise the Jinja template. No other errors found.
- I used the [W3C CSS Validator tool](https://jigsaw.w3.org/css-validator/#validate_by_input) to validate my CSS code.
- I used the [Esprima Syntax Validator tool](http://esprima.org/demo/validate.html) to validate my JavaScript syntax.
- I used the [Pep8 Online tool](http://pep8online.com/) to validate my Python syntax.
    - Line too long, for now, this doesn’t affect functionality. One example is the second line in app.py importing the libraries from flask.

## Deployment

## <a name="deployment"></a> Deployment: 


#### <a name="deployment-to-heroku"></a> Deployment to Heroku
##### Database Setup

Create database on MongoDB

Get data in place first, on atlas mongo website:
* Database with four collections: categories, cooking_tools, recipes and user
* Create a sample record in category collection called category_name: "Lunch"
* Create sample record in the cooking_tools collection with tool_name, tool_image, tool_description, tool_url
* Create sample record in the recipes collection with recipe_name, category_name, recipe_description, image, serves, method, ingredients
* Create sample record in the user collection with username, email, password


##### Setup using VS Code on a Mac
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

##### Deploying to Heroku
###### Four steps to deploying in Heroku

I used GitHub for my version control and Heroku to host the live version of my project. To deploy my app to Heroku, I used the following steps:

1. Created the app in Heroku.
2. Run the `brew tap heroku/brew && brew install heroku` command in the terminal window if using Mac to install heroku in my local workspace.
3. Run `heroku login` command in the terminal window and entered my credentials to login to Heroku.
4. Added and committed the files to Git using the `git add .` and `git commit -m ""` commands in the terminal window.
5. Linked the Heroku app as the remote master branch using the following command in the terminal window:

    ```heroku git:remote -a <app-name>```

6. Created a requirements.txt file using the following command in the terminal window:

    ```pip3 freeze --local > requirements.txt```

7. Created a Procfile using the following command in the terminal window:

    ```echo web: python <fileName.py> > Procfile```

8. Run the `git push heroku master` command in the terminal window to push the app to Heroku.
9. Run the `heroku: ps:scale web=1` command in the terminal window to run the app in Heroku.
10. Entered the following Config Var in Heroku:

    ```MONGO_URI : <link to MongoDB>```

11. On Heroku web interface: Specify IP 0.0.0.0 and Port 5000


The app was successfully deployed to Heroku at this stage.



##### Connecting to MongoDB Atlas

    sudo pip3 install flask-pymongo
    
    
in new file env.py:
	import os
os.environ["MONGO_URI"] = "mongodb+srv://root:r00tUser@myfirstcluster-naitp.mongodb.net/recipes_manager?retryWrites=true&w=majority"


*NOTE* Formatting of connection string carefully. No <> around password, there are THREE places to insert the correct into in to the connection string.


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

1. Go to [my GitHub repository]
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
11. You should now be able to run the app locally using the `python3 run.py` command.

## Credits

- All of the code for my project was written by me.
- By reviewing the a few student projects and the task app made thrughout the data centric course, I developed my logic and understanding of how to implement main functionalities and write my own code.
- [Stack Overflow](https://stackoverflow.com/) The place to find answers of all kinds.
- [W3Schools](https://www.w3schools.com/) Another really good and complete source of information.
- I got a general idea of how to create a register and login system by watching this [Login Video](https://www.youtube.com/watch?list=PLXmMXHVSvS-Db9KK1LA7lifcyZm4c-rwj&v=vVx1737auSE&app=desktop) 
- [Flash Messages Article](https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/) This article help me is understand messages in the app.


### Content

The recipe content for the application was taken from (https://greenkitchenstories.com/) and other text created by me.

### Media

All the images for this app were taken from 

[**_Unsplash_**](https://unsplash.com/)

[**_Green Kitchen Stories_**](https://greenkitchenstories.com/)

The listing item images are added by users from the various sites or locations that the users find images for.

### Acknowledgements

Thank you to the tutoring team for their invaluable support in guiding me through issues I had.
Thank you to my mentor, Rohit, for his review of my project.

### Disclaimer

This project is for educational purposes only.
