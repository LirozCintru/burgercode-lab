from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola():
    return "¡Bienvenido a BurgerCode! La mejor hamburguesa v1.0"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
