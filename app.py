from flask import Flask, render_template, request, redirect, url_for 
from flask_mysqldb import MySQL 

app = Flask(__name__)
app.config['MYSQL_HOST'] = '127.0.0.1'  # ou o endereço do seu banco de dados MySQL
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '32001josue@A'
app.config['MYSQL_DB'] = 'teste'
mysql = MySQL(app)

@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT email, senha FROM users")
    data = cur.fetchall()
    cur.close()
    return render_template('users.html', users=data)

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

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def add_login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (email, senha) VALUES (%s, %s)", (email, senha))
        mysql.connection.commit()
        cur.close()
        return redirect('/')

if __name__=="__main__":
    app.run(debug=True)