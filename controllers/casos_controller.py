import sqlite3

def guardar_caso(caso):
    conn = sqlite3.connect("ligaclinica.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO casos_clinicos (idade, sexo, diagnostico, caracteristica, descricao)
        VALUES (?, ?, ?, ?, ?)
    """, (
        45,  
        "F",
        caso.titulo,
        "mutação X",
        caso.descricao
    ))

    conn.commit()
    conn.close()
