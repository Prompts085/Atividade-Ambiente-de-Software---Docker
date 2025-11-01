from flask import Flask
import pymysql
import os, time

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "senha123")
DB_NAME = os.getenv("DB_NAME", "meu_banco")

@app.route("/")
def index():
    try:
        conn = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        conn.close()
        return "<h1> Conexão OK!</h1>"
    except Exception as e:
        return f"<h1> Erro ao conectar </h1><p>{e}</p>"

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)
