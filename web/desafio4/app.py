from flask import Flask , render_template, request
from flask_mysqldb import MySQL
import mysql.connector


app = Flask(__name__)

db = mysql.connector.connect(
host = "localhost",
user = "root",
password = "markos",
database = "unes"
)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/quemsomos')
def quemsomos():
    return render_template('quemsomos.html')

@app.route('/contato', methods = ["POST","GET"])
def contato():

    if request.method == "POST" :
        try:

            email = request.form['email']


            assunto = request.form['subject']


            descricao = request.form['description']


            if email == '' or assunto  == '' or descricao == '':

                 return render_template('contato.html', status = 'Erro algum dos campos está vazio')

            cursor =  db.cursor(buffered=True)
            

            cursor.execute(f"insert into  contatos (email, assunto, descricao) values ('{email}', '{assunto}', '{descricao}')")
            
            db.commit() 

            cursor.close()
            
            return render_template('contato.html', status = 'Sucesso')
        except ValueError:
            return render_template('contato.html', status = 'Erro')
    else:
        return render_template('contato.html')


@app.route('/users')
def user():
        cursor = db.cursor(buffered=True)
        cursor.execute("select * from contatos")
        userInfo = cursor.fetchall()
        return render_template('users.html', userInfo = userInfo)
    