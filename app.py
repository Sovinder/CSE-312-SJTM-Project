from flask import Flask
from flask import render_template
from flask import make_response
from flask import request
from flask import redirect
from util import validate_password
from util import generate_auth_token
from flask import jsonify
import bcrypt
import mysql.connector


app = Flask(__name__,static_url_path='/static')

@app.after_request
def add_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    return response

@app.route("/")
def home():
    username="Guest"
    user_type_cookie = request.cookies.get('auth')
    if(user_type_cookie=="0" or user_type_cookie==0):
        user_type_cookie=None
    if user_type_cookie != None:
        try:
            conn = mysql.connector.connect(
                user = 'user',
                password = 'password',
                host = 'db',
                database = 'db'
            )
            cursor = conn.cursor()
        except mysql.connector.Error as e:
            print(f"Error: {e}")
        user_query = "SELECT * FROM user WHERE auth_token=%s"
        values = (user_type_cookie,)
        cursor.execute(user_query,values)
        result = cursor.fetchall()
        username = result[0][1]
        conn.commit()
        cursor.close()
        conn.close()
    response = make_response(render_template('index.html',user_type=user_type_cookie,name=username,team="None"))
    response.headers['Content-Type'] = 'text/html'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    return response

@app.route("/chat-update")
def update_chat():
    try:
        conn = mysql.connector.connect(
            user = 'user',
            password = 'password',
            host = 'db',
            database = 'db'
        )
        cursor = conn.cursor()
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    try:
        select_query = "SELECT * FROM messages"
        cursor.execute(select_query)
        result = cursor.fetchall()
    except:
        result = []
    conn.commit()
    cursor.close()
    conn.close()
    data  = {
        'messages':result
    }
    response = jsonify(data)
    return response

@app.route("/chat-message",methods=['POST'])
def chat_message():
    username="Guest"
    username = request.form.get('username')
    team = request.form.get('team')
    message = request.form.get('message')
    user_type_cookie = request.cookies.get('auth')
    if(user_type_cookie=="0" or user_type_cookie==0):
        user_type_cookie=None
    if user_type_cookie != None:
        try:
            conn = mysql.connector.connect(
                user = 'user',
                password = 'password',
                host = 'db',
                database = 'db'
            )
            cursor = conn.cursor()
        except mysql.connector.Error as e:
            print(f"Error: {e}")
        user_query = "SELECT * FROM user WHERE auth_token=%s"
        values = (user_type_cookie,)
        cursor.execute(user_query,values)
        result = cursor.fetchall()
        username = result[0][1]
        if(username!="Guest"):
            create_table = "CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY AUTO_INCREMENT,username TEXT NOT NULL,team TEXT NOT NULL,message TEXT NOT NULL);"
            cursor.execute(create_table)
            conn.commit()
            insert_query = "INSERT INTO messages (username, team,message) VALUES (%s,%s,%s);"
            values = (username, team, message)
            cursor.execute(insert_query, values)
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/chat')
    else:
        return "Error: Not logged in", 400

@app.route("/chat",methods=['POST','GET'])
def chat():
    if request.method == 'POST' or request.method == 'GET':
        if request.method == 'POST':
            username = request.form.get('name')
            team = request.form.get('team')
        else:
            user_type_cookie = request.cookies.get('auth')
            if(user_type_cookie=="0" or user_type_cookie==0):
                user_type_cookie=None
                return redirect("/")
            if user_type_cookie != None:
                try:
                    conn = mysql.connector.connect(
                        user = 'user',
                        password = 'password',
                        host = 'db',
                        database = 'db'
                    )
                    cursor = conn.cursor()
                except mysql.connector.Error as e:
                    print(f"Error: {e}")
            user_query = "SELECT * FROM user WHERE auth_token=%s"
            values = (user_type_cookie,)
            cursor.execute(user_query,values)
            result = cursor.fetchall()
            username = result[0][1]
            team = 'None'
        try:
            conn = mysql.connector.connect(
                user = 'user',
                password = 'password',
                host = 'db',
                database = 'db'
            )
            cursor = conn.cursor()
        except mysql.connector.Error as e:
            print(f"Error: {e}")
        try:
            select_query = "SELECT * FROM messages"
            cursor.execute(select_query)
            result = cursor.fetchall()
        except:
            result = []
        conn.commit()
        cursor.close()
        conn.close()
        response = make_response(render_template('chat.html',name=username,team=team,messages=result))
        response.headers['Content-ype'] = 'text/html'
        response.headers['X-Content-Type-Options'] = 'nosniff'
        return response
        
        
@app.route("/register", methods=['POST'])
def register():
    username = request.form.get('reg-username')
    password = request.form.get('reg-password')
    confirm_password = request.form.get('reg-confirm')
    try:
        conn = mysql.connector.connect(
            user = 'user',
            password = 'password',
            host = 'db',
            database = 'db'
        )
        cursor = conn.cursor()
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    create_table_query = """CREATE TABLE IF NOT EXISTS user (
        id INT AUTO_INCREMENT PRIMARY KEY, 
        username VARCHAR(255) NOT NULL, 
        password VARCHAR(255) NOT NULL,
        auth_token VARCHAR(255) NOT NULL
        );"""
    cursor.execute(create_table_query)
    conn.commit()
    unique_username_query = "SELECT * FROM user WHERE username=%s"
    values = (username,)
    cursor.execute(unique_username_query,values)
    result = cursor.fetchall()
    if(len(result)!=0):
        print("Need a unique username")
        return "Error: Username must be unique", 400
    else:
        if(password == confirm_password and len(validate_password(password))==0):
            auth_token = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())
            hash = auth_token.decode()
            safe_username = username.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
            register_query = "INSERT INTO user (username, password, auth_token) VALUES(%s,%s,%s)"
            values = (safe_username,hash,"0")
            cursor.execute(register_query,values)
            conn.commit()
            cursor.close()
            conn.close()
            response = make_response(render_template('index.html'))
            response.headers['Content-Type'] = 'text/html'
            response.headers['X-Content-Type-Options'] = 'nosniff'
            response.headers['Location'] = '/'
            response.status_code = 302
            return response
        else:
            return "Error: Passwords do not match or dont meet criteria" + password + username, 400


@app.route("/login",methods=['POST'])          
def login():
    username = request.form.get('log-username')
    password = request.form.get('log-password')
    try:
        conn = mysql.connector.connect(
            user = 'user',
            password = 'password',
            host = 'db',
            database = 'db'
        )
        cursor = conn.cursor()
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    check_account_query = "SELECT * FROM user WHERE username=%s"
    values = (username,)
    cursor.execute(check_account_query,values)
    result = cursor.fetchall()
    hashed_password = result[0][2]
    if(bcrypt.checkpw(password.encode("utf-8"),hashed_password.encode("utf-8"))):
        auth_token = generate_auth_token(64)
        insert_auth_query = "UPDATE user SET auth_token=%s WHERE username=%s"
        values = (auth_token,username)
        cursor.execute(insert_auth_query,values)
        conn.commit()
        cursor.close()
        conn.close()
        response = make_response(render_template('index.html'))
        response.headers['Content-Type'] = 'text/html'
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['Location'] = '/'
        response.set_cookie('auth',auth_token,max_age=3600,httponly=True)
        response.status_code = 302
        return response
    else:
        return "Error: Invalid login", 400

@app.route("/logout",methods=['POST'])
def logout():
    user_type_cookie = request.cookies.get('auth')
    if user_type_cookie != None:
        try:
            conn = mysql.connector.connect(
                user = 'user',
                password = 'password',
                host = 'db',
                database = 'db'
            )
            cursor = conn.cursor()
        except mysql.connector.Error as e:
            print(f"Error: {e}")
        logout_query = "UPDATE user SET auth_token=%s WHERE auth_token=%s"
        values = (user_type_cookie,user_type_cookie)
        cursor.execute(logout_query,values)
        conn.commit()
        cursor.close()
        conn.close()
        response = make_response(redirect('/'))
        response.set_cookie('auth',"0",max_age=0,httponly=True)
        return response

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080,debug=False)