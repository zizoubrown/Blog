import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm, CommentForm
from flaskblog.models import User, Post, Comment
from flask_login import login_user, current_user, logout_user, login_required
from flaskblog import request

@app.route("/")
@app.route("/home")
def home():
    #page = request.args.get('page', 1, type=int)
    quote = request.get_quote()
    posts = Post.query.order_by(Post.date_posted.desc()).paginate( per_page=5)
    return render_template('home.html', posts=posts, quote=quote)