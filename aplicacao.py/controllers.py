from app import app
from flask import render_template



@app.route('/home')
def index():
    
    return render_template('index.html')

@app.route('/')
def pagina_principal():
    return '<h1>Página Principal</h1> <p>Olá Prof!!!</p>'


app.run(debug=True)