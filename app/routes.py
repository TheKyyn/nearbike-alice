from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from . import db, bcrypt
from .models import User, Favorite

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('main.index'))
        else:
            flash('Login failed. Check your credentials.')
    return render_template('login.html')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@main.route('/favorites', methods=['GET', 'POST'])
@login_required
def favorites():
    if request.method == 'POST':
        #logique pour ajouter/supprimer des favoris
        pass
    return render_template('favorites.html', favorites=current_user.favorites)

@main.route('/add_favorite', methods=['POST'])
@login_required
def add_favorite():
    station_code = request.form['station_code']
    if not Favorite.query.filter_by(user_id=current_user.id, station_code=station_code).first():
        new_favorite = Favorite(user_id=current_user.id, station_code=station_code)
        db.session.add(new_favorite)
        db.session.commit()
        flash('Station added to favorites.')
    else:
        flash('Station is already in favorites.')
    return redirect(url_for('main.favorites'))

@main.route('/edit_favorite/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_favorite(id):
    favorite = Favorite.query.get_or_404(id)
    if request.method == 'POST':
        if favorite.user_id != current_user.id:
            abort(403)
        new_station_code = request.form['station_code']
        favorite.station_code = new_station_code
        db.session.commit()
        flash('Favorite updated successfully.')
        return redirect(url_for('main.favorites'))
    return render_template('edit_favorite.html', favorite=favorite)


@main.route('/delete_favorite/<int:id>', methods=['POST'])
@login_required
def delete_favorite(id):
    favorite = Favorite.query.get_or_404(id)
    if favorite.user_id != current_user.id:
        abort(403)
    db.session.delete(favorite)
    db.session.commit()
    flash('Station favorite retirée.')
    return redirect(url_for('main.favorites'))

@main.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        existing_user = User.query.filter_by(username=username).first()
        if existing_user is None:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            new_user = User(username=username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('main.index'))
        flash('Username already exists.')
    return render_template('signup.html')

@main.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        current_user.username = request.form['username']
        if request.form['password']:
            current_user.password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        db.session.commit()
        flash('Your profile has been updated.')
        return redirect(url_for('main.profile'))
    return render_template('profile.html')
