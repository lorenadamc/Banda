from flask import Flask
from flask import render_template, session, request
from NuevaBanda import nuevabanda
app = Flask(__name__)
app.secret_key = 'esto-es-una-clave-muy-secreta'
banda = nuevabanda()
@app.route('/')
def index():
    session['BandaSesion'] = nuevabanda()
    banda = session['BandaSesion']
    return render_template('index.html', banda = banda)
@app.route('/banda')
def Banda():
    session['BandaSesion'] = nuevabanda()
    banda= session['BandaSesion']
    return render_template('Instrumento.html', banda = banda)
@app.route('/preparar')
def preparar():
    banda = session['BandaSesion']
    return render_template('preparar.html', banda = banda)
@app.route('/tocar')
def tocar():
    banda = session['BandaSesion']
    return render_template('tocando.html', banda = banda)
if __name__ == '__main__':
      app.run(debug = True, port = 5000 )
