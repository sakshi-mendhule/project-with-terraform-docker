from flask import Flask, jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL
from config import Config
from models import get_movies
from routes.user_routes import user_bp, init_mysql

app = Flask(__name__)
CORS(app)

app.config.from_object(Config)

mysql = MySQL(app)
init_mysql(app)

app.register_blueprint(user_bp, url_prefix='/api/users')

@app.route('/')
def home():
    return "Hotstar Backend Running 🚀"

@app.route('/api/movies', methods=['GET'])
def movies():
    return jsonify(get_movies())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
