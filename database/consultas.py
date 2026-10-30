import sqlite3

def guardar_formulario(nombre, curso, correo, fecha, motivo):

    conexion = sqlite3.connect("formularios.db")
    cursor = conexion.cursor()

    cursor.execute("""
    INSERT INTO formulario
    (nombre, curso, correo, fecha, motivo)
    VALUES (?, ?, ?, ?, ?)
    """, (nombre, curso, correo, fecha, motivo))

    conexion.commit()
    conexion.close()


def mostrar_formularios():

    conexion = sqlite3.connect("formularios.db")
    cursor = conexion.cursor()

    cursor.execute("""
    SELECT *
    FROM formulario
    ORDER BY fecha_registro DESC
    """)

    registros = cursor.fetchall()

    conexion.close()

    return registros