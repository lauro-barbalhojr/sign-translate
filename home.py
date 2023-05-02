from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/teclado/<nome>', methods=['GET', 'POST'])
def teclado(nome):
    if request.method == 'POST':
        nome = request.form['nome']
        return render_template('teclado.html', nome=nome)
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
