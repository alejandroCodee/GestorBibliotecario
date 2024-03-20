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
        self.ui.alquilar_btn.clicked.connect(self.handle_rent_button_click)
        self.ui.Add.clicked.connect(self.add_data_to_table)
        self.ui.buscar_libro.clicked.connect(self.buscar_libro)
        self.connection = connect_to_database()  # Establish database connection
        self.ui.refresh.clicked.connect(self.refresh_table)

        self.title = None 

        if self.connection:  # Check if connection is established
            self.load_data_to_home_table()

    def handle_rent_button_click(self):
        selected_row = self.ui.HomeTable.currentRow()

        if selected_row >= 0:
            title_item = self.ui.HomeTable.item(selected_row, 0)
            if title_item:
                self.title = title_item.text()

                update_query = """
                    UPDATE Libros
                    SET Copias = Copias - 1
                    WHERE Titulo = %s
                """

                try:
                    with self.connection.cursor() as cursor:
                        cursor.execute(update_query, (self.title,))
                        self.connection.commit()

                        QMessageBox.information(self.ui.centralwidget, "Libro Alquilado", f"Se ha alquilado '{self.title}'.")
                        self.refresh_table()

                except mysql.connector.Error as err:
                    print(f"Error updating 'Copias': {err}")
                    QMessageBox.critical(self.ui, "Error", "Ha ocurrido un error al alquilar el libro.")

            else:
                QMessageBox.warning(self.ui, "Advertencia", "No se pudo obtener el título de la fila seleccionada")
        else:
            QMessageBox.warning(self.ui, "Advertencia", "Por favor, seleccione una fila antes de hacer clic en el botón 'Alquilar'")

    def buscar_libro(self):
        titulo = self.ui.Buscar_Libro.text()

        select_query = "SELECT titulo, autor, resumen, Ano_de_publicacion, genero, Copias FROM Libros WHERE titulo LIKE %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(select_query, ('%' + titulo + '%',))
                data = cursor.fetchall()

                self.ui.HomeTable.clearContents()
                self.ui.HomeTable.setRowCount(0)
                for row in data:
                    if row[5] > 0:  # Check if 'Copias' > 0
                        self.add_row_to_home_table(row)

        except mysql.connector.Error as err:
            print(f"Error executing search query: {err}")

    def load_data_to_home_table(self):
        select_query = "SELECT titulo, autor, resumen, Ano_de_publicacion, genero, Copias FROM Libros"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(select_query)
                data = cursor.fetchall()
                for row in data:
                    if row[5] > 0:  # Check if 'Copias' > 0
                        self.add_row_to_home_table(row)
        except mysql.connector.Error as err:
            print(f"Error loading data to HomeTable: {err}")

    def add_row_to_home_table(self, row_data):
        row_position = self.ui.HomeTable.rowCount()
        self.ui.HomeTable.insertRow(row_position)
        for column, value in enumerate(row_data):
            self.ui.HomeTable.setItem(row_position, column, QTableWidgetItem(str(value)))    

    def refresh_table(self):
        self.ui.HomeTable.clearContents()
        self.ui.HomeTable.setRowCount(0)

        select_query = "SELECT titulo, autor, resumen, Ano_de_publicacion, genero, Copias FROM Libros WHERE Copias > 0"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(select_query)
                data = cursor.fetchall()
                for row in data:
                    self.add_row_to_home_table(row)
        except mysql.connector.Error as err:
            print(f"Error loading data to HomeTable: {err}")

    def add_data_to_table(self):
        if not self.connection:  # Check if connection is established
            return

        fecha_actual = QDate.currentDate()
        codigo = random.randint(1000, 9999)
        fechaprestamo = fecha_actual.toString("yyyy-MM-dd")
        fechadevolucion = self.ui.fecha_devolucion.date().toString("yyyy-MM-dd")
        libro = self.title 
        usuario = "hola"

        insert_query = """
            INSERT INTO presto (id_prestamo, fecha_prestamo, fecha_devolucion, Libro, usuario)
            VALUES (%s, %s, %s, %s, %s)
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(insert_query, (codigo, fechaprestamo, fechadevolucion, libro, usuario))
                self.connection.commit() 

                print("Data inserted successfully into presto table")

        except mysql.connector.Error as err:
            print(f"Error inserting data: {err}")

    def close_connection(self):
        if self.connection:
            self.connection.close()