from aplicacao2 import app
from flask import render_template



@app.route('/home')
def index():

    print('Acessei a página')

    retorno = render_template('index.html', 
        title='Página Flask',
        outra= 'novo texto',
        #lista=['a','b','c'])
        lista=[])
    return retorno

@app.route('/')
def pagina_principal():
    return '<h1>Página Principal</h1> <p>Olá Prof!!!</p>'


app.run(debug=True)