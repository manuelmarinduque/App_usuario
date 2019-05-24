from tkinter import messagebox

import psycopg2


class Functions:

    @staticmethod
    def create_table():
        conexion = psycopg2.connect(host='localhost', dbname='register_user', user='Manuel', password='1234')

        cursor = conexion.cursor()

        try:
            cursor.execute('''
                CREATE TABLE usuario (
                ID INTEGER PRIMARY KEY,
                NOMBRE VARCHAR (50),
                APELLIDO VARCHAR (50),
                PASSWORD VARCHAR (50),
                DIRECCION VARCHAR (50),
                BIOGRAFIA VARCHAR (100))
                ''')

            conexion.commit()
            messagebox.showinfo("BBDD", "Base de datos creada correctamente")

        except psycopg2.errors.DuplicateTable:
            messagebox.showwarning("¡Atención!", "Base de datos ya existente")

        finally:
            cursor.close()
            conexion.close()

    @staticmethod
    def salir(raiz):
        valor = messagebox.askquestion("¡Aviso!", "¿Quiere salir del programa?")

        if valor == "yes":
            raiz.destroy()

    @staticmethod
    def limpiar(ident, nombre, apellido, passw, dire, bio):
        ident.set("")
        nombre.set("")
        apellido.set("")
        passw.set("")
        dire.set("")
        bio.delete(1.0, 150.0)

    @staticmethod
    def insertar(ident, nombre, apellido, passw, dire, bio):

        conexion = psycopg2.connect(host='localhost', dbname='register_user', user='Manuel', password='1234')

        cursor = conexion.cursor()

        try:
            cursor.execute('''
                INSERT INTO usuario
                VALUES (%s,%s,%s,%s,%s,%s);
                ''', (ident.get(), nombre.get(), apellido.get(), passw.get(), dire.get(), bio.get(1.0, 150.0)))

            conexion.commit()
            Functions.limpiar(ident, nombre, apellido, passw, dire, bio)
            messagebox.showinfo("BBDD", "Usuario creado correctamente")

        except psycopg2.errors.UniqueViolation:
            messagebox.showwarning("¡Atención!", "El id ya existe")

        except psycopg2.errors.InvalidTextRepresentation:
            messagebox.showwarning("¡Atención!", "Debe llenar todos los campos")

        except psycopg2.errors.StringDataRightTruncation:
            messagebox.showwarning("¡Atención!", "El valor es demasiado largo")

        finally:
            cursor.close()
            conexion.close()

    @staticmethod
    def __leer(ident):

        conexion = psycopg2.connect(host='localhost', dbname='register_user', user='Manuel', password='1234')

        cursor = conexion.cursor()

        usuario = []

        try:
            cursor.execute("SELECT * FROM usuario WHERE id = " + ident.get())
            usuario_f = cursor.fetchall()
            conexion.commit()
            return usuario_f

        except psycopg2.errors.SyntaxError:
            messagebox.showwarning("¡Atención!", "Ingrese id")
            return usuario

        finally:
            cursor.close()
            conexion.close()

    @staticmethod
    def seleccionar(ident, nombre, apellido, passw, dire, bio):

        contenido = Functions.__leer(ident)

        if len(contenido) == 0:
            messagebox.showerror("¡Error!", "No se ha encontrado el usuario")
        else:
            for i in contenido:
                ident.set(i[0])
                nombre.set(i[1])
                apellido.set(i[2])
                passw.set(i[3])
                dire.set(i[4])
                bio.insert(1.0, i[5])

    @staticmethod
    def actualizar(ident, nombre, apellido, passw, dire, bio):

        conexion = psycopg2.connect(host='localhost', dbname='register_user', user='Manuel', password='1234')

        cursor = conexion.cursor()

        contenido = Functions.__leer(ident)

        try:

            if len(contenido) == 0:
                messagebox.showerror("¡Error!", "No se ha encontrado el usuario")
            else:
                cursor.execute(
                    "UPDATE usuario SET nombre= %s, apellido= %s, password= %s, direccion= %s, biografia= %s WHERE id= "
                    + ident.get(), (nombre.get(), apellido.get(), passw.get(), dire.get(), bio.get(1.0, 150.0)))
                conexion.commit()
                messagebox.showinfo("BBDD", "Usuario actualizado correctamente")

        except psycopg2.errors.StringDataRightTruncation:
            messagebox.showwarning("¡Atención!", "El valor es demasiado largo")

        finally:
            cursor.close()
            conexion.close()

    @staticmethod
    def eliminar(ident, nombre, apellido, passw, dire, bio):

        conexion = psycopg2.connect(host='localhost', dbname='register_user', user='Manuel', password='1234')

        cursor = conexion.cursor()

        contenido = Functions.__leer(ident)

        try:

            if len(contenido) == 0:
                messagebox.showerror("¡Error!", "No se ha encontrado el usuario")
            else:
                cursor.execute(
                    "DELETE FROM usuario WHERE id= " + ident.get())

                Functions.limpiar(ident, nombre, apellido, passw, dire, bio)
                conexion.commit()
                messagebox.showinfo("BBDD", "Usuario eliminado correctamente")

        except psycopg2.errors.SyntaxError:
            messagebox.showwarning("¡Atención!", "Sólo se puede eliminar por id")

        finally:
            cursor.close()
            conexion.close()
