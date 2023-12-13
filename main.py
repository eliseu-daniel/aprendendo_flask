from flask import Flask, render_template, request

app = Flask (__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['email'],
                       request.form['password']):
            return log_the_user_in(request.form['email'])
        else:
            error = 'Invalid username/password'

            
    return render_template('login.html', error=error)


def valid_login(email, password):
    print(email)
    print(password)
    return True

def log_the_user_in(email):
    return render_template('hello.html',email=email)
