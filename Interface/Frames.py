from tkinter import Frame, Label, Entry, Button, Text, StringVar, Menu

from Functions.Funciones import Functions


class LienzoFrame:

    def __init__(self, raiz):
        self.__raiz = raiz
        self.mi_id = StringVar()
        self.mi_nombre = StringVar()
        self.mi_apellido = StringVar()
        self.mi_pass = StringVar()
        self.mi_dir = StringVar()
        self.entry_bio = Text()

    def construir_menu(self):

        barra_menu = Menu(self.__raiz)
        self.__raiz.config(menu=barra_menu)

        bbdd_menu = Menu(barra_menu, tearoff=0)

        bbdd_menu.add_command(label="Conectar", command=Functions.create_table)  # Funcion sin los paréntesis

        bbdd_menu.add_command(label="Salir", command=lambda: Functions.salir(self.__raiz))
        # Función con paso de parámetros, usar lambda

        borrar_menu = Menu(barra_menu, tearoff=0)
        borrar_menu.add_command(label="Borrar campos", command=lambda: Functions.limpiar(self.mi_id,
                                                                                         self.mi_nombre,
                                                                                         self.mi_apellido,
                                                                                         self.mi_pass,
                                                                                         self.mi_dir,
                                                                                         self.entry_bio))

        ayuda_menu = Menu(barra_menu, tearoff=0)
        ayuda_menu.add_command(label="Licencia")
        ayuda_menu.add_command(label="Acerca de")

        barra_menu.add_cascade(label="BBDD", menu=bbdd_menu)
        barra_menu.add_cascade(label="Borrar", menu=borrar_menu)
        barra_menu.add_cascade(label="Ayuda", menu=ayuda_menu)

    def construir_frame(self):
        frame = Frame(self.__raiz)
        frame.pack()

        label_id = Label(frame, text="ID")
        label_id.grid(row=0, column=0, padx=10, pady=10)

        label_nombre = Label(frame, text="Nombre")
        label_nombre.grid(row=1, column=0, padx=10, pady=10)

        label_apellido = Label(frame, text="Apellido")
        label_apellido.grid(row=2, column=0, padx=10, pady=10)

        label_pass = Label(frame, text="Password")
        label_pass.grid(row=3, column=0, padx=10, pady=10)

        label_dir = Label(frame, text="Direccion")
        label_dir.grid(row=4, column=0, padx=10, pady=10)

        label_bio = Label(frame, text="Biografia")
        label_bio.grid(row=5, column=0, padx=10, pady=10)

        entry_id = Entry(frame, textvariable=self.mi_id)
        entry_id.grid(row=0, column=1, padx=10, pady=10)

        entry_nombre = Entry(frame, textvariable=self.mi_nombre)
        entry_nombre.grid(row=1, column=1, padx=10, pady=10)

        entry_apellido = Entry(frame, textvariable=self.mi_apellido)
        entry_apellido.grid(row=2, column=1, padx=10, pady=10)

        entry_pass = Entry(frame, textvariable=self.mi_pass)
        entry_pass.grid(row=3, column=1, padx=10, pady=10)

        entry_dir = Entry(frame, textvariable=self.mi_dir)
        entry_dir.grid(row=4, column=1, padx=10, pady=10)

        self.entry_bio = Text(frame, width=15, height=10)
        self.entry_bio.grid(row=5, column=1, padx=10, pady=10)

    def construir_botones(self):

        frame2 = Frame(self.__raiz)
        frame2.pack()

        boton_c = Button(frame2, text="Insertar", command=lambda: Functions.insertar(self.mi_id,
                                                                                     self.mi_nombre,
                                                                                     self.mi_apellido,
                                                                                     self.mi_pass,
                                                                                     self.mi_dir,
                                                                                     self.entry_bio))
        boton_c.grid(row=0, column=0, padx=5, pady=10)

        boton_r = Button(frame2, text="Buscar", command=lambda: Functions.seleccionar(self.mi_id,
                                                                                      self.mi_nombre,
                                                                                      self.mi_apellido,
                                                                                      self.mi_pass,
                                                                                      self.mi_dir,
                                                                                      self.entry_bio))
        boton_r.grid(row=0, column=1, padx=5, pady=10)

        boton_u = Button(frame2, text="Actualizar", command=lambda: Functions.actualizar(self.mi_id,
                                                                                         self.mi_nombre,
                                                                                         self.mi_apellido,
                                                                                         self.mi_pass,
                                                                                         self.mi_dir,
                                                                                         self.entry_bio))
        boton_u.grid(row=0, column=2, padx=5, pady=10)

        boton_d = Button(frame2, text="Eliminar", command=lambda: Functions.eliminar(self.mi_id,
                                                                                     self.mi_nombre,
                                                                                     self.mi_apellido,
                                                                                     self.mi_pass,
                                                                                     self.mi_dir,
                                                                                     self.entry_bio))
        boton_d.grid(row=0, column=3, padx=5, pady=10)
