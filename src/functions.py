from PySide6.QtWidgets import QTableWidgetItem

from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QDateEdit
from PySide6.QtWidgets import QWidget 
from PySide6.QtWidgets import QVBoxLayout 
from PySide6.QtWidgets import QLineEdit 
from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QDate
from PySide6 import QtCore 
from customized import PasswordEdit
from PySide6.QtGui import QIcon
from PySide6 import QtWidgets  
import random
import mysql.connector

def connect_to_database():
    """Connects to the MySQL database using the provided configuration."""
    config = {
        'host': 'db4free.net',
        'port': 3306,
        'user': 'thehaternoob',
        'password': 'palarga123',
        'database': 'thehaternoob'
    }
    try:
        connection = mysql.connector.connect(**config)
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to database: {err}")
        return None


def run_login_form(app):
    # Define la función de login
    def login():
        msg_box = QMessageBox()
        username = form.lineEdit.text()
        password = form.lineEdit_2.text()
        try:
            for data in form.usuario_data:
                if username == data[2] and password == data[5]:
                    user_role = data[3]
                    if user_role == "admin":
                        print("ES ADMIN")
                    else:
                        print("ES NORMAL")
                    return
            msg_box.setText(" Usuario o contraseña invalidos ")
            msg_box.exec_()
        except mysql.connector.Error as err:
            msg_box.setText(" ERROR ", err)
            msg_box.exec_()

    # Define la función de registro
    def register():
        username = form.lineEdit.text()
        password = form.lineEdit_2.text()
        mycursor = mydb.cursor()
        sql = "INSERT INTO usuarios (id_usuario,identidad, nombre, rol, telefono, password) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (form.list_size + 1, 12345678, username, "normal", 1234567890, password)
        mycursor.execute(sql, val)
        mydb.commit()
        msg_box = QMessageBox()
        msg_box.setText(" SE HA REGISTRADO")
        msg_box.exec_()
        mycursor.close()
        mydb.close()
        form.get_usuario_data()

    def on_toggle_password_Action():
        if not form.password_shown:
            form.setEchoMode(QLineEdit.Normal)
            form.password_shown = True
            form.togglepasswordAction.setIcon(self.hiddenIcon)
        else:
            form.setEchoMode(QLineEdit.Password)
            form.password_shown = False
            form.togglepasswordAction.setIcon(self.visibleIcon)
    # Crea la instancia del formulario

    form = QtWidgets.QWidget()
    form.resize(480, 825)
    form.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    form.setStyleSheet(
        """
        QPushButton {
            border-style: outset;
            border-radius: 0px;
            padding: 6px;
        }
        QPushButton:hover {
            background-color: #6da0f2;
            border-style: inset;
        }
        QPushButton:pressed {
            background-color: #146cfa;
            border-style: inset;
        }
        QLineEdit {
        border-radius: 0px;
        height: 30px;
        margin: 0px 0px 0px 0px;
        }
        """
    )

    verticalLayout = QtWidgets.QVBoxLayout(form)
    verticalLayout.setContentsMargins(0, 0, 0, 0)

    horizontalLayout_3 = QtWidgets.QHBoxLayout()

    widget = QtWidgets.QWidget(form)
    widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
    widget.setStyleSheet(".QWidget{background-color: rgb(2, 63, 82);}")

    verticalLayout_2 = QtWidgets.QVBoxLayout(widget)
    verticalLayout_2.setContentsMargins(9, 0, 0, 0)

    pushButton_3 = QtWidgets.QPushButton(widget)
    pushButton_3.setMinimumSize(QtCore.QSize(35, 25))
    pushButton_3.setMaximumSize(QtCore.QSize(35, 25))
    pushButton_3.setStyleSheet("color: white;\n"
                               "font: 13pt \"Verdana\";\n"
                               "border-radius: 1px;\n"
                               "opacity: 200;\n")
    pushButton_3.clicked.connect(form.close)
    verticalLayout_2.addWidget(pushButton_3, 0, QtCore.Qt.AlignRight)

    verticalLayout_3 = QtWidgets.QVBoxLayout()
    verticalLayout_3.setContentsMargins(-1, 15, -1, -1)

    label = QtWidgets.QLabel(widget)
    label.setMinimumSize(QtCore.QSize(100, 150))
    label.setMaximumSize(QtCore.QSize(150, 150))
    label.setStyleSheet("image: url(:icons/rocket_48x48.png);")
    verticalLayout_3.addWidget(label, 0, QtCore.Qt.AlignHCenter)

    formLayout_2 = QtWidgets.QFormLayout()
    formLayout_2.setContentsMargins(50, 35, 59, -1)

    label_2 = QtWidgets.QLabel(widget)
    label_2.setStyleSheet("color: rgb(231, 231, 231);\n"
                          "font: 15pt \"Verdana\";")
    formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, label_2)

    lineEdit = QtWidgets.QLineEdit(widget)
    lineEdit.setMinimumSize(QtCore.QSize(0, 40))
    lineEdit.setStyleSheet("QLineEdit {\n"
                           "color: rgb(231, 231, 231);\n"
                           "font: 15pt \"Verdana\";\n"
                           "border: None;\n"
                           "border-bottom-color: white;\n"
                           "border-radius: 10px;\n"
                           "padding: 0 8px;\n"
                           "background: rgb(20, 20, 40);\n"
                           "selection-background-color: darkgray;\n"
                           "}")
    lineEdit.setFocus()
    formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, lineEdit)

    label_4 = QtWidgets.QLabel(widget)
    formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, label_4)

    label_3 = QtWidgets.QLabel(widget)
    formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, label_3)

    """lineEdit_2 = PasswordEdit(widget)
    lineEdit_2.setMinimumSize(QtCore.QSize(0, 40))
    lineEdit_2.setStyleSheet("QLineEdit {\n"
                              "color: white;\n"
                              "font: 15pt \"Verdana\";\n"
                              "border: None;\n"
                              "border-bottom-color: white;\n"
                              "border-radius: 10px;\n"
                              "padding: 0 8px;\n"
                              "background: rgb(20, 20, 40);\n"
                              "selection-background-color: darkgray;\n"
                              "}")
    formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, lineEdit_2)
    lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
    """
    line = QtWidgets.QFrame(widget)
    line.setStyleSheet("border: 2px solid white;")
    line.setFrameShape(QtWidgets.QFrame.HLine)
    line.setFrameShadow(QtWidgets.QFrame.Sunken)
    formLayout_2.setWidget(1, QtWidgets.QFormLayout.SpanningRole, line)

    line_2 = QtWidgets.QFrame(widget)
    line_2.setStyleSheet("border: 2px solid white;")
    line_2.setFrameShape(QtWidgets.QFrame.HLine)
    line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
    formLayout_2.setWidget(5, QtWidgets.QFormLayout.SpanningRole, line_2)

    pushButton = QtWidgets.QPushButton(widget)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(pushButton.sizePolicy().hasHeightForWidth())
    pushButton.setSizePolicy(sizePolicy)
    pushButton.setMinimumSize(QtCore.QSize(0, 60))
    pushButton.setAutoFillBackground(False)
    pushButton.setStyleSheet("color: rgb(231, 231, 231);\n"
                              "font: 17pt \"Verdana\";\n"
                              "border: 2px solid white;\n"
                              "padding: 5px;\n"
                              "border-radius: 3px;\n"
                              "opacity: 200;\n")
    pushButton.setAutoDefault(True)
    formLayout_2.setWidget(7, QtWidgets.QFormLayout.SpanningRole, pushButton)

    pushButton_2 = QtWidgets.QPushButton(widget)
    pushButton_2.setMinimumSize(QtCore.QSize(0, 60))
    pushButton_2.setStyleSheet("color: rgb(231, 231, 231);\n"
                                "font: 17pt \"Verdana\";\n"
                                "border: 2px solid white;\n"
                                "padding: 5px;\n"
                                "border-radius: 3px;\n"
                                "opacity: 200;\n")
    pushButton_2.setDefault(False)
    pushButton_2.setFlat(False)
    formLayout_2.setWidget(8, QtWidgets.QFormLayout.SpanningRole, pushButton_2)

    spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
    formLayout_2.setItem(6, QtWidgets.QFormLayout.SpanningRole, spacerItem)
    verticalLayout_3.addLayout(formLayout_2)

    spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
    verticalLayout_3.addItem(spacerItem1)
    verticalLayout_2.addLayout(verticalLayout_3)

    horizontalLayout_3.addWidget(widget)
    horizontalLayout_3.setStretch(0, 1)
    verticalLayout.addLayout(horizontalLayout_3)

    # Conecta las señales de los botones a las funciones correspondientes
    pushButton.clicked.connect(login)
    pushButton_2.clicked.connect(register)

    form.show()
    app.exec_()







class Functions:
    def __init__(self, ui):
        self.ui = ui
        self.ui.Add.clicked.connect(self.add_data_to_table)
        self.ui.pushButton.clicked.connect(self.add_data_to_table_catalogo)
        self.ui.buscar_libro.clicked.connect(self.buscar_libro)
        self.connection = connect_to_database()  # Establish database connection

        self.ui.alquilar_btn.clicked.connect(self.handle_rent_button_click)
        self.ui.refresh.clicked.connect(self.refresh_table)
        self.ui.refresh_catalogo.clicked.connect(self.refresh_catalogo_table)  




        self.title = None 

        if self.connection:  # Check if connection is established
            self.load_data_to_home_table()
            self.load_data_to_table_catalogo()
            self.load_data_to_table()

    def handle_rent_button_click(self):
        # Get the selected row
        selected_row = self.ui.HomeTable.currentRow()

        if selected_row >= 0:
            # Get the title from the selected row
            title_item = self.ui.HomeTable.item(selected_row, 0)
            if title_item:
                self.title = title_item.text()

                # Update the "Copias" column for the selected book
                update_query = """
                    UPDATE Libros
                    SET Copias = Copias - 1
                    WHERE Titulo = %s
                """

                try:
                    with self.connection.cursor() as cursor:
                        cursor.execute(update_query, (self.title,))
                        self.connection.commit()

                        # Inform the user about the update (optional)
                        QMessageBox.information(self.ui.centralwidget, "Libro Alquilado", f"Se ha alquilado '{self.title}'.")

                        # Refresh the tables to reflect the update (optional)
                        self.refresh_table()  # Assuming you have a refresh_table function
                        self.load_data_to_table_catalogo()  # Assuming you have a function to load catalogo table

                except mysql.connector.Error as err:
                    print(f"Error updating 'Copias': {err}")
                    QMessageBox.critical(self.ui, "Error", "Ha ocurrido un error al alquilar el libro.")

            else:
                QMessageBox.warning(self.ui, "Advertencia", "No se pudo obtener el título de la fila seleccionada")
        else:
            QMessageBox.warning(self.ui, "Advertencia", "Por favor, seleccione una fila antes de hacer clic en el botón 'Alquilar'")


    

    def buscar_libro(self):
        titulo = self.ui.Buscar_Libro.text()

        select_query = "SELECT titulo, autor, resumen, Ano_de_publicacion, genero FROM Libros WHERE titulo LIKE %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(select_query, ('%' + titulo + '%',))
                data = cursor.fetchall()

                #se borran TODOS datos
                self.ui.HomeTable.clearContents()
                self.ui.HomeTable.setRowCount(0)
                for row in data:
                    # Añadre solo los que encontro
                    self.add_row_to_home_table(row)

                    
        except mysql.connector.Error as err:
            print(f"Error executing search query: {err}")


#para que se carguen los datos de catalogo
    def load_data_to_table_catalogo(self):
        select_query = "SELECT * FROM Libros"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(select_query)
                data = cursor.fetchall()
                for row in data:
                    self.add_row_to_catalogo_table(row)
        except mysql.connector.Error as err:
            print(f"Error loading data to catalogo table: {err}")

    def add_row_to_catalogo_table(self, row_data):
        row_position = self.ui.tableWidget_2.rowCount()
        self.ui.tableWidget_2.insertRow(row_position)
        for column, value in enumerate(row_data):
            self.ui.tableWidget_2.setItem(row_position, column, QTableWidgetItem(str(value)))


#para que se carguen los datos de prestamos
    def load_data_to_table(self):
        select_query = "SELECT * FROM presto"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(select_query)
                data = cursor.fetchall()
                for row in data:
                    self.add_row_to_prestamos_table(row)
        except mysql.connector.Error as err:
            print(f"Error loading data to prestamos table: {err}")

    def add_row_to_prestamos_table(self, row_data):
        row_position = self.ui.prestamos_tabla.rowCount()
        self.ui.prestamos_tabla.insertRow(row_position)
        for column, value in enumerate(row_data):
            self.ui.prestamos_tabla.setItem(row_position, column, QTableWidgetItem(str(value)))



#FUNCIONES DE PRUEBA
    def load_data_to_home_table(self):
        select_query = "SELECT titulo, autor, resumen, Ano_de_publicacion, genero  FROM Libros"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(select_query)
                data = cursor.fetchall()
                for row in data:
                    self.add_row_to_home_table(row)
        except mysql.connector.Error as err:
            print(f"Error loading data to HomeTable: {err}")

    def add_row_to_home_table(self, row_data):
        row_position = self.ui.HomeTable.rowCount()
        self.ui.HomeTable.insertRow(row_position)
        for column, value in enumerate(row_data):
            self.ui.HomeTable.setItem(row_position, column, QTableWidgetItem(str(value)))    

      
#añadir los Lines a catalogo
    def add_data_to_table_catalogo(self):
        if not self.connection:  # Check if connection is established
            return

        año = self.ui.ANOP_LE.text()
        autor = self.ui.AUTOR_LE.text()
        cantidad = self.ui.CANTIDAD_LE.text()
        disponible = self.ui.DISPONIBLE_LE.text()
        formato = self.ui.FORMATO_LE.text()
        idioma = self.ui.IDIOMA_LE.text()
        estado = self.ui.ESTADO_LE.text()
        genero = self.ui.GENERO_LE.text()
        isbn = self.ui.ISBN_LE.text()
        pasillo = self.ui.PASILLO_LE.text()
        resumen = self.ui.RESUMEN_LE.text()
        titulo = self.ui.TITULO_LE.text()

        insert_query = """
            INSERT INTO Libros (ISBN, Titulo, Genero, Autor, Ano_de_publicacion, Disponible, Formato, Copias, Idioma, Resumen, Pasillo, Estado)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(insert_query, (isbn, titulo, genero, autor, año, disponible, formato, cantidad, idioma, resumen, pasillo, estado))
                self.connection.commit()  # Commit changes to the database

                # Add data to the table (assuming table name is 'prestamos_tabla')
                row_position = self.ui.tableWidget_2.rowCount()
                self.ui.tableWidget_2.insertRow(row_position)

                self.ui.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(isbn))
                self.ui.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(titulo))
                self.ui.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(genero))
                self.ui.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(autor))
                self.ui.tableWidget_2.setItem(row_position, 4, QTableWidgetItem(año))
                self.ui.tableWidget_2.setItem(row_position, 5, QTableWidgetItem(disponible))
                self.ui.tableWidget_2.setItem(row_position, 6, QTableWidgetItem(formato))
                self.ui.tableWidget_2.setItem(row_position, 7, QTableWidgetItem(cantidad))
                self.ui.tableWidget_2.setItem(row_position, 8, QTableWidgetItem(idioma))
                self.ui.tableWidget_2.setItem(row_position, 9, QTableWidgetItem(resumen))
                self.ui.tableWidget_2.setItem(row_position, 10, QTableWidgetItem(pasillo))
                self.ui.tableWidget_2.setItem(row_position, 11, QTableWidgetItem(estado))

                # Clear the LineEdits after successful insertion
                self.ui.ANOP_LE.clear()
                self.ui.AUTOR_LE.clear()
                self.ui.CANTIDAD_LE.clear()
                self.ui.DISPONIBLE_LE.clear()
                self.ui.FORMATO_LE.clear()
                self.ui.IDIOMA_LE.clear()
                self.ui.ESTADO_LE.clear()
                self.ui.GENERO_LE.clear()
                self.ui.ISBN_LE.clear()
                self.ui.PASILLO_LE.clear()
                self.ui.RESUMEN_LE.clear()
                self.ui.TITULO_LE.clear()

        except mysql.connector.Error as err:
            print(f"Error inserting data: {err}")

    def refresh_table(self):
        # Borra los datos actuales en HomeTable
        self.ui.HomeTable.clearContents()
        self.ui.HomeTable.setRowCount(0)

        # Carga los datos actualizados de la tabla 'Libro'
        select_query = "SELECT titulo, autor, resumen, Ano_de_publicacion, genero FROM Libros"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(select_query)
                data = cursor.fetchall()
                for row in data:
                    # Añade los datos a HomeTable
                    self.add_row_to_home_table(row)
        except mysql.connector.Error as err:
            print(f"Error loading data to HomeTable: {err}")

    def refresh_catalogo_table(self):
        # Borra los datos actuales en la tabla "Libros" (tableWidget_2)
        self.ui.tableWidget_2.clearContents()
        self.ui.tableWidget_2.setRowCount(0)

        # Carga los datos actualizados de la tabla 'Libros'
        select_query = "SELECT * FROM Libros"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(select_query)
                data = cursor.fetchall()
                for row in data:
                    # Añade los datos a la tabla "Libros" (tableWidget_2)
                    self.add_row_to_catalogo_table(row)
        except mysql.connector.Error as err:
            print(f"Error loading data to catalogo table: {err}")


  


    def add_data_to_table(self):
        if not self.connection:  # Check if connection is established
            return
        #agarra el dia de hoy
        fecha_actual = QDate.currentDate()


        codigo = random.randint(1000, 9999)
        #codigo = self.ui.codigo_LE.text()
        fechaprestamo = fecha_actual.toString("yyyy-MM-dd")
        fechadevolucion = self.ui.fecha_devolucion.date().toString("yyyy-MM-dd")

        #EN VEZ DE AGARRAR ESTE .TEXT, QUE AGARRE, LO DE LA FILA.
        #libro = self.ui.libro_LE.text()
        libro = self.title 
        usuario = self.ui.usuario_LE.text()

        # Prepare SQL query to insert data
        insert_query = """
            INSERT INTO presto (id_prestamo, fecha_prestamo, fecha_devolucion, Libro, usuario)
            VALUES (%s, %s, %s, %s, %s)
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(insert_query, (codigo, fechaprestamo, fechadevolucion, libro, usuario))
                self.connection.commit()  # Commit changes to the database
                # Get the newly inserted row ID (optional)
                cursor.execute("SELECT LAST_INSERT_ID()")
                inserted_row_id = cursor.fetchone()[0]

                # Add data to the table (assuming table name is 'prestamos_tabla')
                row_position = self.ui.prestamos_tabla.rowCount()
                self.ui.prestamos_tabla.insertRow(row_position)

                self.ui.prestamos_tabla.setItem(row_position, 0, QTableWidgetItem(codigo))
                self.ui.prestamos_tabla.setItem(row_position, 1, QTableWidgetItem(fechaprestamo))
                self.ui.prestamos_tabla.setItem(row_position, 2, QTableWidgetItem(fechadevolucion))
                self.ui.prestamos_tabla.setItem(row_position, 3, QTableWidgetItem(libro))
                self.ui.prestamos_tabla.setItem(row_position, 4, QTableWidgetItem(usuario))

                self.ui.usuario_LE.clear()

        except mysql.connector.Error as err:
            print(f"Error inserting data: {err}")






    def close_connection(self):
        if self.connection:
            self.connection.close()
