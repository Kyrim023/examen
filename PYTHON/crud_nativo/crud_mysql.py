import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="usuarios"
)
cursor = conn.cursor()

def crear_usuario(nombre, correo):
    try:
        sql = "INSERT INTO usuarios (nombre, correo) VALUES (%s, %s)"
        cursor.execute(sql, (nombre, correo))
        conn.commit()
        print(" Usuario creado.")
    except mysql.connector.IntegrityError:
        print(" El correo ya existe.")

def listar_usuarios():
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    print(" Lista de usuarios:")
    for u in usuarios:
        print(u)

def actualizar_usuario(id_usuario, nuevo_nombre, nuevo_correo):
    sql = "UPDATE usuarios SET nombre = %s, correo = %s WHERE id = %s"
    cursor.execute(sql, (nuevo_nombre, nuevo_correo, id_usuario))
    conn.commit()
    print(" Usuario actualizado.")

def eliminar_usuario(id_usuario):
    cursor.execute("DELETE FROM usuarios WHERE id = %s", (id_usuario,))
    conn.commit()
    print(" Usuario eliminado.")

def menu():
    while True:
        print("\n--- MENÚ CRUD MySQL ---")
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
            id_usuario = input("ID del usuario a actualizar: ")
            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_correo = input("Nuevo correo: ")
            actualizar_usuario(id_usuario, nuevo_nombre, nuevo_correo)
        elif opcion == "4":
            id_usuario = input("ID del usuario a eliminar: ")
            eliminar_usuario(id_usuario)
        elif opcion == "5":
            print(" Saliendo del programa.")
            break
        else:
            print(" Opción inválida, intenta de nuevo.")


menu()

cursor.close()
conn.close()
