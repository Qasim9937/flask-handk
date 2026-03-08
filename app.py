from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

data = {}

# creating routes

@app.route('/')
def home():
    # return 'Welcome Home'
    return render_template('index.html')


@app.route('/login')
def login():
    # return 'Login Page'
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "GET":
        return render_template('signup.html')
    
    elif request.method == "POST":
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        password = request.form['password']

        print(fname, lname, email, password)
        return redirect(url_for('home'))





if __name__ == '__main__':
    app.run(debug=True)