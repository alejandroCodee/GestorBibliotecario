from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtCore import Qt

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
        self.connection = connect_to_database()  # Establish database connection

    def add_data_to_table(self):
        if not self.connection:  # Check if connection is established
            return

        codigo = self.ui.codigo_LE.text()
        fechaprestamo = self.ui.fechaprestamo_LE.text()
        fechadevolucion = self.ui.fechadevolucion_LE.text()
        libro = self.ui.libro_LE.text()
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

                # Clear the LineEdits after successful insertion
                self.ui.codigo_LE.clear()
                self.ui.fechaprestamo_LE.clear()
                self.ui.fechadevolucion_LE.clear()
                self.ui.libro_LE.clear()
                self.ui.usuario_LE.clear()

        except mysql.connector.Error as err:
            print(f"Error inserting data: {err}")

    def close_connection(self):
        if self.connection:
            self.connection.close()