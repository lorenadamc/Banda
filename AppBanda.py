from flask import Flask
from flask import render_template
from NuevaBanda import nuevabanda
app = Flask(__name__)
banda = nuevabanda()
can = len(banda)
@app.route('/')
def index():
    return render_template('index.html', banda=banda, can = can)
@app.route('/preparar')
def preparar():
    return render_template('preparar.html', banda=banda)
@app.route('/tocar')
def tocar():
    return render_template('tocando.html', banda=banda)
if __name__ == '__main__':
      app.run(debug = True, port = 5000 )
