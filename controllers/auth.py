import sqlite3
from database import create_connection

def register_user(username,password):
    # Registra novo usuario
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("Usuário cadastrado com sucesso")
    except sqlite3.IntegrityError:
        print("ERRO: Nome do usuario já existe!")
    finally:
        conn.close()

def login_user(username, password):
    # valida o login do Usuario
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user
