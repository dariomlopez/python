# Endpoints, GET y Post con flask
# Line 2 to line 9 a very basic flask app
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '¡Landing page!'

@app.route('/usuario/<username>')
def usuario(username):
    return f'Hola {username}, bienvenida/o a tu perfil'

if __name__ == '__main__':
    app.run(debug=True)