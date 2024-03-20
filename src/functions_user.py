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

from src.ui_interface_user import Ui_UserMain


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


class FunctionsUser:
    def __init__(self, ui):
        self.ui = ui
        #self.ui.Add.clicked.connect(self.add_data_to_table)
        #self.ui.pushButton.clicked.connect(self.add_data_to_table_catalogo)
        self.ui.alquilar_btn.clicked.connect(self.handle_rent_button_click)
        self.ui.buscar_libro.clicked.connect(self.buscar_libro)
        self.connection = connect_to_database()  # Establish database connection

        
        self.ui.refresh.clicked.connect(self.refresh_table)
        #self.ui.refresh_catalogo.clicked.connect(self.refresh_catalogo_table)  

       

        self.title = None 

        if self.connection:  # Check if connection is established
            self.load_data_to_home_table()
            #self.load_data_to_table_catalogo()
            #self.load_data_to_table()

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
    """def load_data_to_table_catalogo(self):
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

"""

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

    def close_connection(self):
        if self.connection:
            self.connection.close()
