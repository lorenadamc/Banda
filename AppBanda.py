from flask import Flask
from flask import render_template, session, request
from NuevaBanda import nuevabanda
app = Flask(__name__)
app.secret_key = 'esto-es-una-clave-muy-secreta'
banda = nuevabanda()
@app.route('/')
def index():
    session['BandaSesion'] = nuevabanda()
    b = session['BandaSesion']
    return render_template('index.html', banda = b)
@app.route('/banda')
def Banda():
    session['BandaSesion'] = nuevabanda()
    b = session['BandaSesion']
    return render_template('Instrumento.html', banda = b)
@app.route('/preparar')
def preparar():
    b = session['BandaSesion']
    return render_template('preparar.html', banda = b)
@app.route('/tocar')
def tocar():
    return render_template('tocando.html', banda = b)
if __name__ == '__main__':
      app.run(debug = True, port = 5000 )
