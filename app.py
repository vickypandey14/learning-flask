from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from form import MyForm
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/')
def hello_world():
    return 'Hello, World! My name is vivek and i am learning flask!'

@app.route('/about')
def about():
    return 'This is the about page of the Flask application.'

# Dynamic route example

@app.route('/user/<username>/<age>')
def user_profile(username , age):
    return f'User profile page for {username} with age {age}.'

# GET method example

@app.route('/post/<int:post_id>', methods=['GET'])
def show_post(post_id):
    return f'Post: {post_id}'

# POST and GET method example

@app.route('/submit', methods=['GET','POST'])
def submit_form():
    if request.method == 'POST':
        return 'Your Form has been submitted!'
    else:
        return 'Please try to submit the form again!'

# Template rendering example

@app.route('/template')
def template_example():
    return render_template('index.html')

@app.route('/user-template/<username>/<age>')
def user_template(username, age):
    items = ['Laravel', 'Flask', 'Django', 'PHP', 'JavaScript', 'Python']
    return render_template('user.html', name=username, user_age=age, skills=items)

# Handle Form submission example

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)

@app.route('/submit-form', methods=['GET', 'POST'])
def submit_form_example():
    form = MyForm()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        new_user = User(name=name, email=email, phone=phone)
        db.session.add(new_user)
        db.session.commit()

        return f'Form submitted successfully!'
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)