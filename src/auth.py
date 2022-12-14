from flask import Blueprint, render_template, request


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        signup_name = request.form.get('signup_name')
        signup_surname = request.form.get('signup_surname')
        signup_country = request.form.get('signup_country')
        signup_password1 = request.form.get('signup_password1')
        signup_password2 = request.form.get('signup_password2')
        signup_email1 = request.form.get('signup_email1')
        signup_email2 = request.form.get('signup_email2')
    return render_template("sign_up.html")
