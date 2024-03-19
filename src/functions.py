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
