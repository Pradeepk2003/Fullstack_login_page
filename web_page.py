from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = '12345'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pass1234s5'
app.config['MYSQL_DB'] = 'web'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])

def login():
    if request.method=='POST':
        email = request.form['email']
        password = request.form['password']

        
        cursor = mysql.connection.cursor()
        cursor.execute(f"SELECT * FROM data WHERE email = '{email}' AND password = '{password}'")
        data = cursor.fetchone()
        cursor.close()

        if data:
            session['email'] = data[1]
            session['password'] = data[1]
            return render_template('LS.html')
        
    return render_template("NEWLOGINUI.html")    

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO data (username, password, email) VALUES (%s, %s, %s)",(username,password,email))
        mysql.connection.commit()
        cursor.close()

        return render_template('RS.html')
    return render_template('NEWLOGINUI.html')

if __name__ == '__main__':
    app.run(debug=True)

