from flask import Flask, render_template, request, flash, redirect, session,url_for,abort
import requests
from models import Cocktail
import random


from models import db, connect_db, User, Comment, Favorite
from forms import UserAddForm, LoginForm,SearchForm, CommentForm




app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cocktails'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"
CURR_USER_KEY = "curr_user"




@app.route("/", methods=["GET", "POST"])
def home():
    """Home page"""
    search_form=SearchForm()
    
    if search_form.validate_on_submit():
        search_term=search_form.search.data
        return redirect(url_for("search_cocktails", term=search_term))
    
    response = requests.get("https://www.thecocktaildb.com/api/json/v1/1/random.php")
    data = response.json()
    cocktail = data["drinks"][0]

    processed_coctail = {}
    processed_coctail['id'] = cocktail['idDrink']
    processed_coctail['name'] = cocktail['strDrink']
    processed_coctail['instructions'] = cocktail['strInstructions']
    processed_coctail['image'] = cocktail['strDrinkThumb']
    processed_coctail['ingredients'] = []

    for i in range(1, 16):
        ingredient_key = f'strIngredient{i}'
        measure_key = f'strMeasure{i}'

        if cocktail[ingredient_key] and cocktail[measure_key]:
            ingredient = cocktail[ingredient_key]
            measure = cocktail[measure_key]
            processed_coctail['ingredients'].append((ingredient, measure))

    return render_template("home.html", search_form=search_form, cocktail=processed_coctail)

@app.route("/search/<term>")
def search_cocktails(term):
    response = requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={term}")
    data = response.json()
    cocktails = data["drinks"] if data["drinks"] else []
    processed_coctails=[]
    
    
    
    for cocktail in cocktails:
        processed_coctail = {}
        processed_coctail['id'] = cocktail['idDrink']
        processed_coctail['name'] = cocktail['strDrink']
        processed_coctail['instructions'] = cocktail['strInstructions']
        processed_coctail['image'] = cocktail['strDrinkThumb']
        processed_coctail['ingredients'] = []
        
        for i in range(1,16):
            ingredient_key = f'strIngredient{i}'
            measure_key = f'strMeasure{i}'
            
            if cocktail[ingredient_key] and cocktail[measure_key]:
                ingredient = cocktail[ingredient_key]
                measure = cocktail[measure_key]
                processed_coctail['ingredients'].append((ingredient, measure))
        
        processed_coctails.append(processed_coctail)
    
                
    return render_template("search.html", term=term, cocktails=processed_coctails)




@app.route("/cocktail/<id>", methods=["GET", "POST"])
def cocktail(id):
    response = requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={id}")
    data = response.json()
    cocktail = data["drinks"][0]

    processed_coctail = {}
    processed_coctail['id'] = cocktail['idDrink']
    processed_coctail['name'] = cocktail['strDrink']
    processed_coctail['instructions'] = cocktail['strInstructions']
    processed_coctail['image'] = cocktail['strDrinkThumb']
    processed_coctail['ingredients'] = []

    for i in range(1,16):
        ingredient_key = f'strIngredient{i}'
        measure_key = f'strMeasure{i}'

        if cocktail[ingredient_key] and cocktail[measure_key]:
            ingredient = cocktail[ingredient_key]
            measure = cocktail[measure_key]
            processed_coctail['ingredients'].append((ingredient, measure))
   

    form = CommentForm()

    if form.validate_on_submit():
        comment_text = form.comment.data
        
       # cocktail = Cocktail.query.get(id)
        #if cocktail is None:
         #   flash("Cocktail not found", "error")
          #  return redirect(url_for('cocktail', id=id))
        

        
        comment = Comment(text=comment_text, cocktail_id=id)

        
        db.session.add(comment)
        db.session.commit()
        

        flash("Comment added successfully", "success")
        return redirect(url_for('cocktail', id=id))

    
    comments = Comment.query.filter_by(cocktail_id=id).all()

    return render_template("cocktail.html", cocktail=processed_coctail, form=form, comments=comments)




@app.route("/delete/comment/<int:cocktail_id>/delete/comment/<int:id>")
def delete_comment(cocktail_id, id):
    comment = Comment.query.get_or_404(id)
    db.session.delete(comment)
    db.session.commit()
    flash("Comment deleted successfully", "success")
    return redirect(url_for('cocktail', id=cocktail_id))



#Fav

@app.route('/cocktail/<int:cocktail_id>/favorites', methods=['POST'])
def add_to_favorites(cocktail_id):
    if CURR_USER_KEY not in session:
        return redirect('login.html')
    
    user_id = int(session[CURR_USER_KEY])  
    cocktail_id = int(cocktail_id)  
    
    existing_favorite = Favorite.query.filter_by(user_id=user_id, cocktail_id=cocktail_id).first()

    if existing_favorite is None:
        fav_handle = Favorite(user_id=user_id, cocktail_id=cocktail_id)
        db.session.add(fav_handle)
        db.session.commit()

    return redirect(f'/{user_id}/favorites')



@app.route('/<int:user_id>/favorites')
def user_fav(user_id):
    if CURR_USER_KEY not in session:
        return redirect('login.html')
    
    favs= Favorite.query.filter_by(user_id=user_id).all()
    fav_list = []
    i = 0
    for result in favs:
        fav_details = Cocktail.query.filter_by(id=favs[i].cocktail_id)
        fav_list.append(fav_details) 
        i +=1
    return render_template('favorites.html', cocktail_list=fav_list)

@app.route('/<int:user_id>/favorites/delete/<int:drink_id>', methods=["POST"])
def delete_cocktail(user_id, drink_id):
    fav = Favorite.query.filter_by(cocktail_id=drink_id).first()
    db.session.delete(fav)
    db.session.commit()
    return redirect(f'/{user_id}/favorites')











@app.route("/login", methods=["GET", "POST"])
def login_user():
    """User login handling"""
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)
        if user:
            session[CURR_USER_KEY] = user.id
            return redirect("/")
        else:
            form.username.errors = ["Invalid Username/Passwords"]

    return render_template("login.html", form=form)


@app.route("/register", methods=["GET", "POST"])
def register_user():
  
    form = UserAddForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        user = User.register(username, password, first_name, last_name)
        db.session.add(user)
        db.session.commit()
        session[CURR_USER_KEY] = user.id
        flash("User Created", "success")
        return redirect("/")
    else:
        return render_template("register.html", form=form)




@app.route("/logout")
def logout():
    session.pop(CURR_USER_KEY)
    flash("You have logged out successfully", "success")
    return redirect("/")
