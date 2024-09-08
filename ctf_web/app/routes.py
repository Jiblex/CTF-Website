import os
import secrets
import magic
from pathlib import Path
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort, jsonify
from flask_login import login_user, current_user, logout_user, login_required
from app import app, database, bcrypt, login_manager, Jinja2
from app.forms import Registration, Login, UpdateAccount, PostForm
from app.models import User, Post
from jinja2 import Environment

from sqlalchemy.sql import text


# index route
@app.route("/")
def index():
    return home()

# home page route
@app.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=4)
    return render_template("home.html", posts=posts)

# about page route
@app.route("/about")
def about():
    return render_template("about.html")

# register page route
@app.route("/register", methods=["POST", "GET"])
def register():
    # if user is authenticated, redirect them to the home page
    if current_user.is_authenticated:
        return redirect(url_for("home"))

    form = Registration()
    # if form validates successfully, create user in database, forward user to login page
    if form.validate_on_submit():
        # hashed password
        hashpass = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        # make user
        user = User(username=form.username.data, email=form.email.data, password=hashpass)
        # add and commit to database
        database.session.add(user)
        database.session.commit()
        flash(f'Account created for {form.username.data}! Please login.', 'success')
        # redirect to login page
        return redirect(url_for('login'))
    return render_template("register.html", title="Register", form=form)

# login page route
@app.route("/login", methods=["POST", "GET"])
def login():
    # if user is authenticated, redirect them to the home page
    if current_user.is_authenticated:
        return redirect(url_for("home"))

    form = Login()

    # if form validates successfully, forward user to home page
    if form.validate_on_submit():
        # check that email exists and password hash matches that in the database
        email = User.query.filter_by(email=form.email.data).first()
        if email and bcrypt.check_password_hash(email.password, form.password.data):
            login_user(email, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("home"))
        # if login incorrect
        else:
            flash('Either email or password is incorrect.', 'danger')
    # SQLi section, making the email input field vulnerable 
    if form.email.data:
        rawQueryString = form.email.data
        try:
            query = text(rawQueryString)
            # Execute the vulnerable query
            result = database.session.execute(query)
            # the result of the SQLi
            res = result.fetchall()
            if res:
                return render_template("login.html", title="Login", form=form, res=res)
        except:
            return render_template("login.html", title="Login", form=form)
        
    return render_template("login.html", title="Login", form=form)

# logout route (only for when user clicks logout) 
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


# function saves given picture
def save_pic(form_picture):
    rand_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = rand_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/images', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

# account page route; displays account info on logged in user
@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccount()
    # if form submits, make entered info the new user info
    if form.validate_on_submit():
        if form.pic.data:
            # save submitted picture and make it current user pic
            pic = save_pic(form.pic.data)
            current_user.image = pic
        current_user.username = form.username.data
        current_user.email = form.email.data
        database.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image = url_for('static', filename='images/' + current_user.image)
    return render_template('account.html', title='Account', image_file=image, form=form)


# robots page route, there is a flag here
@app.route("/robots.txt")
def robots():
    return render_template("robots.txt", title="robots.txt")


# create a post page route
@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    # make sure post has data in it
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        database.session.add(post)
        database.session.commit()
        flash('Post Created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post',
                           form=form, legend='New Post')


# find specific post route
@app.route("/post/<int:pid>")
# use post id to find the post
def post(pid):
    post = Post.query.get_or_404(pid)
    return render_template('post.html', title=post.title, post=post)


# update post route 
@app.route("/post/<int:pid>/update", methods=['GET', 'POST'])
@login_required
def update_post(pid):
    post = Post.query.get_or_404(pid)
    # check that user trying to modify post if the post author
    if post.author != current_user:
        abort(403)
    form = PostForm()
    # check that data is present, commit to database
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        database.session.commit()
        flash('Post Updated!', 'success')
        return redirect(url_for('post', pid=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')


# delete post route
@app.route("/post/<int:pid>/delete", methods=['POST'])
@login_required
def delete_post(pid):
    post = Post.query.get_or_404(pid)
    # check that user trying to modify post if the post author
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Post Deleted!', 'success')
    return redirect(url_for('home'))





# ------------------------- route for H0tD0g challenge -------------------------
@app.route("/other_one", methods=['GET'])
def other_one():
    return render_template("other_one.html")
# -------------------------------------------------------------------------------------------





# ------------------------- route for URLpass challenge -------------------------
# route for navigation to challenge page, provides example of what the correct URL should look like
@app.route("/URLpass/param=wKD7yf0", methods=['GET'])
def example_param():
    return render_template('example_param.html')

# flag route with the correct parameter "rockyou"
@app.route("/URLpass/param=rockyou", methods=['GET'])
def correct_param():
    return render_template('correct_param.html')
# -------------------------------------------------------------------------------------------










# ------------------------- route for Phantom Pathfield challenge -------------------------
@app.route("/phantom", methods=['GET'])
def phantom():
    return render_template('phantom.html')
# -------------------------------------------------------------------------------------------











# ------------------------- routes for Access Abyss challenge -------------------------

# route for the abyss page pertaining to Access Abyss challenge
@app.route("/abyss", methods=['GET', 'POST'])
def access_abyss():
    # Using the login form
    form = Login()
    # wait for request, then check the request username and password, on success give back the flag page
    try:
        data = request.form
        if data['username'] == "FatherChristmas" and data['password'] == "d1dUctrlF":
            return "<p> CTF{the4Byss_sT4r3es_RIGhtB4ck} </p>"
    except:
        data = request.form
        if request.method == "GET":
            return render_template('access_abyss.html', title='Access Abyss', form=form)
        if not(data['username'] != "FatherChristmas") and request.method == "POST":
            return "<p> You failed to enter the abyss. </p>"
    return render_template('access_abyss.html', title='Access Abyss', form=form)
# -------------------------------------------------------------------------------------------










# ------------------------- routes for Phantom Pathfield challenge -------------------------
@app.route("/babygirl")
def babygirl():
    return "<h1> You found a secret page bbg. </h1>"
@app.route("/basketball")
def basketball():
    return "<h1> Ball </h1>"
@app.route("/genesis")
def genesis():
    return "<h1> The beginning. </h1>"
@app.route("/snickers")
def snickers():
    return "<h1> You're not you when you're hungry. </h1>"
@app.route("/popcorn")
def popcorn():
    return "<h1> I bet you like popcorn. </h1>"
# route for flag
@app.route("/rockyou")
def rockyou():
    return "<h1> CTF{r0UT3_bU5T3r5} </h1>"
# -------------------------------------------------------------------------------------------










# ------------------------- routes for Agent 007: User Agent Undercover challenge -------------------------
@app.route("/user_agent", methods=['POST', 'GET'])
def user_agent():
     # wait for request, then check the request username and password, on success give back the flag page
    try:
        data = request.form
        user_agent = request.headers
        # if player tries POST tell them they need the secret user agent
        if request.method =="POST":
            return "<p> Your user agent is incorrect.\
            Find the secret 'User-Agent' to get the flag. Go to /user_agent/help to find it.</p>"
        # if player uses secret user-agent they get the flag
        if user_agent["User-Agent"] == "agH8dGG7":
            return "<p> CTF{B3rRy_5TR4Wberry} </p>"
    
    except:
        print("Wrong user agent.")
    return render_template("user_agent_undercover.html")

# route for Jenja2 injection 
@app.route("/user_agent/help", methods=['POST', 'GET'])
def user_agent_help(user=None):
    form = Login()

    # Jinja2 injection via URL
    try:
        injection = request.values.get('injection')
        if injection == "{{secret_ua}}":
            return "<h4> Now go use the secret user agent! SECRET=agH8dGG7 </h4>"
        if injection == "{{ secret_ua }}":
            return "<h4> Now go use the secret user agent! SECRET=agH8dGG7 </h4>"
        if injection:
            return Jinja2.from_string(injection).render()

    except:
        return render_template("user_agent_help.html", form=form)
    return render_template("user_agent_help.html", form=form)
# -------------------------------------------------------------------------------------------










# ------------------------- routes for Cut it 0FF challenge -------------------------
ALLOWED_EXTENSIONS = {'pdf'}
TXT = {'.txt'}

# checks that file is a pdf
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# checks that file has null byte with .txt after it
def null_byte(filename):
    return '.' in filename and filename.rsplit('%00', 1)[1].lower() in TXT

# route for pdf submits
@app.route("/uploaded_pdf")
def up_pdf():
    return render_template('uploaded_pdf.html')

# route for txt submits with null byte
@app.route("/uploaded_nullbyte_withTXT")
def up_nullbyte():
    return render_template('nb_txt.html')


# route for Cut it 0FF
@app.route("/submit_me", methods=['POST', 'GET'])
def submit_me():
    # check file type and validate
    try:
        file = request.files['file']
        # check if pdf
        if allowed_file(file.filename):
            return redirect(url_for('up_pdf'))
        # check if null byte is being used and .txt 
        elif null_byte(file.filename):
            return redirect(url_for('up_nullbyte'))
        else:
            print("This file format is not supported!")
    except:
        print("This file format is not supported!")
    return render_template("submit_me.html")
# -------------------------------------------------------------------------------------------
