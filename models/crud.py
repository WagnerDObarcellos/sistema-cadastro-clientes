import sqlite3
from database import create_connection

def create_record(name, description):
    # Criar um novo registro
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO records (name, description) VALUES (?, ?)", (name, description))
    conn.commit()
    print("Registro criado com sucesso!")
    conn.close()

def read_record():
    # Lê todos os registros
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM records")
    records = cursor.fetchall()
    conn.close()
    return records

def update_record(record_id, name, description):
    # Atualiza um registro existente
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE records SET name = ?, description = ? WHERE id = ?", (name, description, record_id))
    conn.commit()
    print("Registro atualizado com sucesso")
    conn.close()

def delete_record(record_id):
    # Deleta o registro
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM records WHERE id = ?", (record_id,))
    conn.commit()
    print("Registro deletado com sucesso!")
    conn.close()