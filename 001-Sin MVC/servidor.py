from flask import Flask

app = Flask(__name__)

def cabecera():
    return "<!doctype><html><head></head><body><header><h1>La web de Jose Vicente</h1></header><main>"

def piedepagina():
    return "</main><footer>(c) 2023 Jose Vicente</footer></html>"

@app.route('/')
def home():
    return cabecera()+"<h1>Pagina principal</h1>"+piedepagina()

@app.route('/clientes')
def clientes():
    return cabecera()+"<h1>Pagina de clientes</h1>"+piedepagina()

@app.route('/productos')
def productos():
    return cabecera()+"<h1>Pagina de productos</h1>"+piedepagina()

if __name__ == '__main__':
    app.run(port=8080)
