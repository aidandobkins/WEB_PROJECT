from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from __init__ import create_app

main = Blueprint('main', __name__)


@main.route('/')
def index(): 
    return render_template('index.html')

@main.route('/profile')
def profile(): 
    return render_template('profile')

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)