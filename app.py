from flask import Flask, render_template, request,redirect,url_for,session
from database import create_connection, initialize_database
import os

app = Flask(__name__)
app.secret_key = 'secret_key' #chave para sessão

#inicializa o banco de dados
initialize_database()

#Rota inicial do Login
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]


        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            session[user] = username
            return redirect(url_for("dashboard"))
        else:
            return "Login falhou! Verifique suas credenciais."
    return render_template("loginhtml")

#rota de registro
@app.route("/register", method = ["GET","POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            return redirect(url_for("login"))
        except:
            return "Usuario já existe!"
        finally:
            conn.close()
    return render_template("register.html")

#Dashboard #crud
@app.route("/dashboard", methods = ["GET","POST"])
def dashboard():
    if "user" not in session:
        return redirect("login.html")
    
    conn = create_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        # Criação de um novo registro
        name = request.form["name"]
        description = request.form["description"]
        cursor.execute("INSERT INTO records (name, description) VALUES (?, ?)", (name, description))
        conn.commit()
    
    #Leitura do registro
    cursor.execute("SELECT * FROM records")
    records = cursor.fetchall()
    conn.close()
    return render_template("dashboard.html", records = records)


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
