from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/teclado/', methods=['GET', 'POST'])
def teclado():
    nome = request.form.get('nome')
    return render_template('teclado.html', nome=nome)

if __name__ == '__main__':
    app.run(debug=True)
