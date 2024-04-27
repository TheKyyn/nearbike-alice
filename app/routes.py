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

