from flask import Flask
from flask import render_template
from NuevaBanda import nuevabanda
app = Flask(__name__)
banda = nuevabanda()
@app.route('/')
def index():
    banda = nuevabanda()
    return render_template('index.html', banda=banda)
@app.route('/preparar')
def preparar():
    return render_template('preparar.html', banda=banda)
@app.route('/tocar')
def tocar():
    return render_template('tocar.html', banda=banda)
if __name__ == '__main__':
      app.run(debug = True, port = 5000 )
