# Cocktail API Project

Welcome to the Cocktail API project! This project is a Flask-based web application that allows users to explore and interact with cocktail information retrieved from [TheCocktailDB API](https://www.thecocktaildb.com/api.php?ref=apilist.fun). Users can search for cocktails by name, sign in or sign up, add drinks to their favorites, leave comments, and more.



## Features

- **Search Cocktails by Name:** Users can search for cocktails by their names.
- <img src = "https://github.com/serenkapanoglu/BeABaristaAtHome2/blob/main/images2/search.png" width="280" />
  
- **User Authentication:**
  - Sign up with first name, last name, username, and password.
  - Passwords are securely encrypted using Bcrypt.
  - Sign in with registered credentials.

- **Favorites:**
  - Users can add drinks to their favorites.
  - View all favorite drinks on the Favorites page.
  - Remove drinks from favorites.

- **Comments:**
  - Users can add comments to cocktails.
  - Delete their own comments.

- **Random Cocktail on Page Refresh:** Every time a user refreshes the page, a random cocktail is displayed.

## Tech Stack

- HTML, CSS, Bootstrap for front-end.
- Python with Flask for the back-end.
- PostgreSQL as the database.
- SQLAlchemy for database ORM.
- Jinja for templating.

## Deployment

The project is deployed and can be accessed at [be-a-barista-at-home.onrender.com](https://be-a-barista-at-home.onrender.com/).

## Database Schema

Include a brief description or a visual representation of your database schema. You can use tools like [draw.io](https://app.diagrams.net/) for creating a visual representation.

## Getting Started

1. Clone the repository.
   ```bash
   git clone https://github.com/your-username/cocktail-api-project.git
   cd cocktail-api-project
