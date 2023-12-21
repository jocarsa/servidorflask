from flask import Flask, render_template

app = Flask(__name__)

miedad = 45

@app.route('/')
def home():
    return render_template('home.html',mi_edad = miedad)

@app.route('/clientes')
def clientes():
    return render_template('clientes.html')

@app.route('/productos')
def productos():
    return render_template('productos.html')

@app.route('/edad')
def edad():
    global miedad
    miedad += 1
    return "tu edad es de: "+str(miedad)+" años"
    

if __name__ == '__main__':
    app.run(port=8080)
