from flask import Blueprint, render_template, redirect, request, url_for

routes_blueprint = Blueprint('routes', __name__)


# creating routes
@routes_blueprint.route('/')
def home():
    # return 'Welcome Home'

    return render_template('index.html')

@routes_blueprint.route('/login')
def login():
    # return 'Login Page'
    return render_template('login.html')

@routes_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "GET":
        return render_template('signup.html')
    
    elif request.method == "POST":
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        password = request.form['password']
        return redirect(url_for('home'))

@routes_blueprint.route('/about')
def about():
    return render_template('about.html')

@routes_blueprint.route('/skills')
def skills():
    return render_template('skills.html')

@routes_blueprint.route('/project')
def project():
    return render_template('project.html')

@routes_blueprint.route('/contact')
def contact():
    return render_template('contact.html')

@routes_blueprint.app_errorhandler(404)
def page_404(error):
    return render_template('404.html'), 404