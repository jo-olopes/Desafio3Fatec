from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/starblack')
def starblack():
    return render_template('starblack.html')

@app.route('/starwhite')
def starwhite():
    return render_template('starwhite.html')

@app.route('/moletombranco')
def moletombranco():
    return render_template('moletombranco.html')

@app.route('/moletompreto')
def moletompreto():
    return render_template('moletompreto.html')


@app.route('/quemsomos')
def quemsomos():
    return render_template('quemsomos.html')


@app.route('/cart')
def cart():
    return render_template('cart.html')


if __name__=="__main__":
    app.run(debug=True)