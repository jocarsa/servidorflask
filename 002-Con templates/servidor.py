from flask import Flask, render_template

app = Flask(__name__)

edad = 45

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/clientes')
def clientes():
    return render_template('clientes.html')

@app.route('/productos')
def productos():
    return render_template('productos.html')


if __name__ == '__main__':
    app.run(port=8080)