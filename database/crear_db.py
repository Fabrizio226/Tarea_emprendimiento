import sqlite3

conexion = sqlite3.connect("formularios.db")
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE formulario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    curso TEXT NOT NULL,
    correo TEXT NOT NULL,
    fecha TEXT NOT NULL,
    motivo TEXT NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conexion.commit()
conexion.close()

print("Tabla creada correctamente")