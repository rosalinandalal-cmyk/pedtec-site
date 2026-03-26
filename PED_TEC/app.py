from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Criar banco automaticamente
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS mensagens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        email TEXT,
        mensagem TEXT
    )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contato", methods=["POST"])
def contato():
    nome = request.form["nome"]
    email = request.form["email"]
    mensagem = request.form["mensagem"]

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO mensagens (nome, email, mensagem) VALUES (?, ?, ?)",
                   (nome, email, mensagem))
    conn.commit()
    conn.close()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)