import sqlite3

def create_connection():
    # Cria conexão com o banco SQLite
    conn = sqlite3.connect("users.db")
    return conn

def initialize_database():
    # Inicia banco de dados com tabelae usuarios e dados
    conn = create_connection()
    cursor = conn.cursor()

    #tabela do usuario
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
            )
        ''')

    #Tabela de dados (crud)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS records(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_database()