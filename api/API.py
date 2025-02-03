from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime, timedelta
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
CORS(app)

# Configuración de JWT
app.config["JWT_SECRET_KEY"] = "tu_clave_secreta_super_segura"
jwt = JWTManager(app)

def get_db_connection():
    conn = sqlite3.connect("mi_base.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/usuarios", methods=["POST"])
def crear_usuario():
    data = request.get_json()
    nombre = data.get("nombre")
    contrasenia = data.get("contrasenia")
    imagen = data.get("imagen", "")
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, contrasenia, imagen) VALUES (?, ?, ?)",
                   (nombre, contrasenia, imagen))
    conn.commit()
    conn.close()
    
    return jsonify({"mensaje": "Usuario creado exitosamente"}), 201

@app.route("/usuarios/iniciar-sesion", methods=["POST"])
def iniciar_sesion():
    data = request.get_json()
    nombre = data.get("nombre")
    contrasenia = data.get("contrasenia")
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE nombre = ? AND contrasenia = ?", (nombre, contrasenia))
    usuario = cursor.fetchone()
    conn.close()
    
    if usuario:
        access_token = create_access_token(identity=usuario["id"])
        return jsonify({"mensaje": "Inicio de sesión exitoso", "usuario": dict(usuario), "token": access_token})
    return jsonify({"error": "Credenciales incorrectas"}), 401

@app.route("/usuarios/<int:id>/tareass", methods=["GET"])
@jwt_required()
def obtener_Tareas(id): #tareas d eun usuario particular
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT t.*, c.nombre, c.descripcion
    FROM tareas t
    JOIN categorias c ON t.id_categoria = c.id
    WHERE t.id_usuario = ?
    """, (id,))
    tareas = cursor.fetchall()
    conn.close()
    
    return jsonify([dict(tarea) for tarea in tareas])

@app.route("/usuarios/<int:id>/tareas", methods=["GET"])
def obtener_tareas(id): 
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT t.*, c.nombre, c.descripcion
    FROM tareas t
    JOIN categorias c ON t.id_categoria = c.id
    WHERE t.id_usuario = ?
    """, (id,))
    tareas = cursor.fetchall()
    conn.close()
    
    return jsonify([dict(tarea) for tarea in tareas])

@app.route("/tareas", methods=["POST"])
def crear_tarea():
    data = request.get_json()
    texto = data.get("texto")
    fecha_tentativa = data.get("fecha_tentativa")
    estado = data.get("estado", "Pendiente")
    id_usuario = data.get("id_usuario")
    id_categoria = data.get("id_categoria")
    
    if fecha_tentativa:
        fecha_tentativa_dt = datetime.strptime(fecha_tentativa, "%Y-%m-%d")
        if fecha_tentativa_dt < datetime.now():
            return jsonify({"mensaje": "La fecha tentativa no puede ser anterior a hoy"}), 400
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tareas (texto, fecha_creacion, fecha_tentativa, estado, id_usuario, id_categoria) VALUES (?, ?, ?, ?, ?, ?)",
                   (texto, datetime.now().strftime("%Y-%m-%d"), fecha_tentativa, estado, id_usuario, id_categoria))
    conn.commit()
    conn.close()
    
    return jsonify({"mensaje": "Tarea creada exitosamente, refresca para ver cambios"}), 201

@app.route("/tareas/<int:id>", methods=["PUT"])
def actualizar_tarea(id):
    data = request.get_json()
    texto = data.get("texto")
    estado = data.get("estado")
    fecha_tentativa = data.get("fecha_tentativa")
    id_categoria = data.get("id_categoria")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tareas SET texto = ?, estado = ?, fecha_tentativa = ?,  id_categoria = ?  WHERE id = ?", (texto, estado, fecha_tentativa, id_categoria, id))
    conn.commit()
    conn.close()
    
    return jsonify({"mensaje": "Tarea actualizada exitosamente"})

@app.route("/tareas/<int:id>", methods=["DELETE"])
def eliminar_tarea(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tareas WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    
    return jsonify({"mensaje": "Tarea eliminada exitosamente"})

@app.route("/tareas/<int:id>", methods=["GET"])
def obtener_tarea(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tareas WHERE id = ?", (id,))
    tarea = cursor.fetchone()
    conn.close()
    
    if tarea:
        return jsonify(dict(tarea))
    return jsonify({"error": "Tarea no encontrada"}), 404

@app.route("/usuarios/<int:id>", methods=["GET"])
def obtener_usuario(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id,))
    usuario = cursor.fetchone()
    conn.close()
    
    if usuario:
        return jsonify(dict(usuario))
    return jsonify({"error": "usuario no encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=True)
