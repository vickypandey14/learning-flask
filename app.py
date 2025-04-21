from flask import Flask, request

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)