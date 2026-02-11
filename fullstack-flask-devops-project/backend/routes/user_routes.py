from flask import Blueprint, request, jsonify
from flask_mysqldb import MySQL

user_bp = Blueprint('user_bp', __name__)
mysql = MySQL()

def init_mysql(app):
    mysql.init_app(app)

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    name = data['name']
    email = data['email']
    password = data['password']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users(name, email, password) VALUES(%s,%s,%s)",
                (name, email, password))
    mysql.connection.commit()
    cur.close()

    return jsonify({"message": "User Registered Successfully"})

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data['email']
    password = data['password']

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE email=%s AND password=%s",
                (email, password))
    user = cur.fetchone()
    cur.close()

    if user:
        return jsonify({"message": "Login Successful"})
    else:
        return jsonify({"message": "Invalid Credentials"}), 401
