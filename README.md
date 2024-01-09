# Cocktail API Project

Welcome to the Cocktail API project! This project is a Flask-based web application that allows users to explore and interact with cocktail information retrieved from [TheCocktailDB API](https://www.thecocktaildb.com/api.php?ref=apilist.fun). Users can search for cocktails by name, sign in or sign up, add drinks to their favorites, leave comments, and more.

  
## Tech Stack

- HTML, CSS, Bootstrap for front-end.
- Python with Flask for the back-end.
- PostgreSQL as the database.
- SQLAlchemy for database ORM.
- Jinja for templating.
<br></br>


## Features

- **Search Cocktails by Name:** Users can search for cocktails by their names. <br></br>
 <img src = "https://github.com/serenkapanoglu/BeABaristaAtHome2/blob/main/images2/search3.png" />
 <img src = "https://github.com/serenkapanoglu/BeABaristaAtHome2/blob/main/images2/searchvodka.png" />
  <br></br>
  
- ## **User Authentication:**
  - Sign up with first name, last name, username, and password.
  - Passwords are securely encrypted using Bcrypt.
  - Sign in with registered credentials.
  <br></br>
  <br></br>
  
    <img src="https://github.com/serenkapanoglu/BeABaristaAtHome2/blob/main/images2/login.png" />
    <img src ="https://github.com/serenkapanoglu/BeABaristaAtHome2/blob/main/images2/register.png?raw=true" />
    <br></br>
    

- ## **Favorites:**
  - Users can add drinks to their favorites.
  - View all favorite drinks on the Favorites page.
  - Remove drinks from favorites.
    <br></br>
  <br></br>
    <img src = "https://github.com/serenkapanoglu/BeABaristaAtHome2/blob/main/images2/fav.png" />
<br></br>


- ## **Comments:**
  - Users can add comments to cocktails.
  - Delete their own comments.
    <br></br>
  <br></br>
    <img src = "https://github.com/serenkapanoglu/BeABaristaAtHome2/blob/main/images2/addcomment.png" />
    <img src = "https://github.com/serenkapanoglu/BeABaristaAtHome2/blob/main/images2/deletecomment.png" />
<br></br>
<br></br>

- ## **Random Cocktail on Page Refresh:** Every time a user refreshes the page, a random cocktail is displayed.
<img src= "https://github.com/serenkapanoglu/BeABaristaAtHome2/blob/main/images2/search2.png" />
<img src = "https://github.com/serenkapanoglu/BeABaristaAtHome2/blob/main/images2/search4.png" />
<img src = "https://github.com/serenkapanoglu/BeABaristaAtHome2/blob/main/images2/search.png" />
   
<br></br>



## Deployment

 [be-a-barista-at-home.onrender.com](https://your-barista-at-home.onrender.com/).

## Database Schema

<img src = "https://github.com/serenkapanoglu/BeABaristaAtHome2/blob/main/schema.png" />


## Project Structure

- `/app`: This directory holds the core files for your Flask application.
  - `app.py`: Entry point for the Flask application.
  - `forms.py`: Includes forms for user input.
  - `models.py`: Contains database models.


- `/templates`: Holds HTML templates for your Flask app.
  - `base.html`: Base template with common structure.
  - `cocktails.html`: Template for displaying cocktail information.
  - `favorites.html`: Template for showing user's favorite drinks.
  - `home.html`: Template for the home page.
  - `login.html`: Template for user login.
  - `register.html`: Template for user registration.
  - `search.html`: Template for searching cocktails.

- `/images2`: Stores images used in the project.


- `.env`: Configuration file for environment variables, including sensitive data like API keys.

- `requirements.txt`: Lists all the dependencies required for your project.

- `README.md`: Documentation for your project.


## Getting Started

1. Clone the repository.
   ```bash
   git clone https://github.com/serenkapanoglu/BeABaristaAtHome2.git
   cd BeABaristaAtHome2
   flask run
