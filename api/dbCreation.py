import sqlite3
#A simple sqlite db for this case :)
conexion = sqlite3.connect("mi_base.db")
cursor = conexion.cursor() #Too used for sql sentences
#The following is needed only to run one time, but it is no problem if its runed more (there is a previus validation)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        contrasenia TEXT NOT NULL,
        imagen TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS categorias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS tareas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        texto TEXT NOT NULL,
        fecha_creacion TEXT NOT NULL,
        fecha_tentativa TEXT,
        estado TEXT,
        id_usuario TEXT,
        id_categoria TEXT
    )
''')

cursor.execute("INSERT INTO categorias (nombre, descripcion) VALUES (?, ?)", ("Hogar", "Quehaceres de la casa"))
cursor.execute("INSERT INTO categorias (nombre, descripcion) VALUES (?, ?)", ("Estudio", "Tu puedes, no abandones la carrera"))
cursor.execute("INSERT INTO categorias (nombre, descripcion) VALUES (?, ?)", ("Trabajo", "Vida laboral"))
cursor.execute("INSERT INTO categorias (nombre, descripcion) VALUES (?, ?)", ("Social", "Reuniones con familia y amigos"))
cursor.execute("INSERT INTO categorias (nombre, descripcion) VALUES (?, ?)", ("Otros", "Categoria comodin"))


conexion.commit()
print("Si sirvió")
