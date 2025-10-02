# app/my_project/auth/app.py
import os
from flask import Flask
from flask_mysqldb import MySQL
from route import api_bp

app = Flask(__name__)

# ---- MySQL config: беремо з env (див. /etc/flaskapp.env) ----
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER', 'appuser')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD', '')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB', 'appdb')
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST', '127.0.0.1')
app.config['MYSQL_PORT'] = int(os.getenv('MYSQL_PORT', '3306'))

# створюємо клієнт ПІСЛЯ конфігурації
mysql = MySQL(app)
app.mysql = mysql

def init_db_mysql():
    """Одноразова ініціалізація БД із data.sql."""
    cursor = mysql.connection.cursor()
    sql_file_path = os.path.join(os.path.dirname(__file__), 'data.sql')
    if os.path.exists(sql_file_path):
        with open(sql_file_path, 'r') as f:
            for command in (c.strip() for c in f.read().split(';')):
                if command:
                    cursor.execute(command)
        mysql.connection.commit()
    cursor.close()

# health-check БД (зручно для перевірки п.2)
@app.route("/health/db")
def health_db():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT 1")
        cur.fetchone()
        cur.close()
        return {"ok": True}, 200
    except Exception as e:
        return {"ok": False, "error": str(e)}, 500

@app.route("/debug/env")
def debug_env():
    return {
        "MYSQL_HOST": app.config.get("MYSQL_HOST"),
        "MYSQL_DB": app.config.get("MYSQL_DB"),
        "MYSQL_USER": app.config.get("MYSQL_USER"),
        "MYSQL_PORT": app.config.get("MYSQL_PORT"),
    }, 200

# реєстрація API
app.register_blueprint(api_bp, url_prefix='/api')

# dev-запуск: у проді запускає Gunicorn, тому без app.run() і без init тут
if __name__ == "__main__":
    app.run(debug=True)
