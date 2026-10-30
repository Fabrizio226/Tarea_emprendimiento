from flask import Flask, render_template, request
from database.consultas import guardar_formulario, mostrar_formularios

app = Flask(__name__)

# --- PÁGINAS DE LA BARRA DE NAVEGACIÓN ---

# Página de Inicio (index.html)
@app.route("/")
def inicio():
    return render_template("index.html")

# Agendar Hora (Tu formulario original)
@app.route("/agendar-hora")
def agendar():
    return render_template("solicitud_hora.html")

# Cancelar Hora
@app.route("/cancelar-hora")
def cancelar():
    return render_template("cancelar_hora.html")

# Horarios disponibles
@app.route("/horarios")
def horarios():
    return render_template("horarios.html")

# Ayuda
@app.route("/ayuda")
def ayuda():
    return render_template("ayuda.html")

# Preguntas
@app.route("/preguntas")
def preguntas():
    return render_template("preguntas.html")


# --- PROCESAMIENTO DE DATOS ---

# Guardar formulario (Modificado para que redireccione bien)
@app.route("/guardar", methods=["POST"])
def guardar():
    nombre = request.form["nombre"]
    curso = request.form["curso"]
    correo = request.form["correo"]
    fecha = request.form["fecha"]
    motivo = request.form["motivo"]

    guardar_formulario(
        nombre,
        curso,
        correo,
        fecha,
        motivo
    )

    # He actualizado los enlaces de este texto para que coincidan con las nuevas rutas de Flask
    return """
    <h1>Solicitud enviada correctamente</h1>
    <a href="/agendar-hora">Volver al formulario</a>
    <br><br>
    <a href="/registros">Ver solicitudes registradas</a>
    """

# Mostrar registros guardados
@app.route("/registros")
def registros():
    datos = mostrar_formularios()
    return render_template(
        "registros.html",
        registros=datos
    )

#calendario


# Iniciar servidor
if __name__ == '__main__':
    app.run(debug=True)