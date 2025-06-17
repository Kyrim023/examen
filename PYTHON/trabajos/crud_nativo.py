import sqlite3

conn = sqlite3.connect("usuarios.db")
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    correo TEXT NOT NULL UNIQUE
)
''')
conn.commit()

def crear_usuario(nombre, correo):
    try:
        cursor.execute("INSERT INTO usuarios (nombre, correo) VALUES (?, ?)", (nombre, correo))
        conn.commit()
        print(" Usuario creado con éxito.")
    except sqlite3.IntegrityError:
        print(" El correo ya existe.")


def listar_usuarios():
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    print(" Lista de usuarios:")
    for u in usuarios:
        print(u)

def actualizar_usuario(id_usuario, nuevo_nombre, nuevo_correo):
    cursor.execute("UPDATE usuarios SET nombre = ?, correo = ? WHERE id = ?", (nuevo_nombre, nuevo_correo, id_usuario))
    conn.commit()
    print(" Usuario actualizado.")

def eliminar_usuario(id_usuario):
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
    conn.commit()
    print(" Usuario eliminado.")

def menu():
    while True:
        print("\n--- MENÚ CRUD ---")
        print("1. Crear usuario")
        print("2. Listar usuarios")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            crear_usuario(nombre, correo)
        elif opcion == "2":
            listar_usuarios()
        elif opcion == "3":
            id_usuario = int(input("ID del usuario a actualizar: "))
            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_correo = input("Nuevo correo: ")
            actualizar_usuario(id_usuario, nuevo_nombre, nuevo_correo)
        elif opcion == "4":
            id_usuario = int(input("ID del usuario a eliminar: "))
            eliminar_usuario(id_usuario)
        elif opcion == "5":
            print(" Saliendo del programa.")
            break
        else:
            print("Opción inválida, intenta de nuevo.")


menu()
conn.close()
