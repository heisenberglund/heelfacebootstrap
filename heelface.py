from flask import Flask, request, redirect, render_template, session, flash


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['POST','GET'])
def index():
    return render_template('heelface.html')

@app.route('/signup', methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        verify = request.form['verify']
        existing_user = User.query.filter_by(email=email).first()
        if not existing_user:
            new_user = User(email, password)
            db.session.add(new_user)
            db.session.commit()
            session['email'] = email
            return redirect('/')
        else:
            return "<h1>Duplicate user</h1>"

    return render_template('signup.html')

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.password == password:
            session['email'] = email
            flash("Logged in")
            return redirect('/')
        else:
            flash('User password incorrect, or user does not exist', 'error')

    return render_template('login.html')
@app.route('/contact', methods=['POST','GET'])
def contact():
    return render_template('contact.html')

app.run()