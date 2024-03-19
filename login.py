# This Python file uses the following encoding: utf-8
import sys
import mysql.connector
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtCore import Signal  # Importa Signal
from cryptography.fernet import Fernet
from ui_form import Ui_login

key = Fernet.generate_key()
cipher_suite = Fernet(key)

class login(QWidget):
    # Define la señal
    session_closed = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_login()
        self.ui.setupUi(self)
        self.usuario = ""
        self.password = ""
        self.db_host = "db4free.net"
        self.db_user = "thehaternoob"
        self.db_password = "palarga123"
        self.db_name = "thehaternoob"

        self.usuario_data = []  
        self.get_usuario_data()

        self.ui.pushButton.clicked.connect(self.login)
        self.ui.pushButton_2.clicked.connect(self.register)

    def encrypt_password(self, password):
        encrypted_password = cipher_suite.encrypt(password.encode())
        return encrypted_password

    def decrypt_password(self, encrypted_password):
        decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
        return decrypted_password
    
    def get_usuario_data(self):
        msg_box = QMessageBox()
        try:
            self.connection = mysql.connector.connect(
                host=self.db_host,
                user=self.db_user,
                password=self.db_password,
                database=self.db_name
            )

            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM usuarios")

            self.usuario_data = cursor.fetchall()
            self.list_size = len(self.usuario_data)  

            cursor.close()
            self.connection.close()

        except mysql.connector.Error as err:
            msg_box.setText(" ERROR ", err)  
            msg_box.exec() 

    def login(self):
        msg_box = QMessageBox()
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        try:
            for data in self.usuario_data:
                if username == data[2] and password == self.decrypt_password(data[5]):
                    self.user_role = data[3]  
                    if self.user_role == "admin":
                        print("ES ADMIN") #borrable
                    else:
                        print("ES NORMAL") #borrable
                    # Emite la señal cuando el usuario inicia sesión exitosamente
                    self.session_closed.emit()
                    return  
            msg_box.setText(" Usuario o contraseña invalidos ")  
            msg_box.exec()  

        except mysql.connector.Error as err:
            msg_box.setText(" ERROR ", err)  
            msg_box.exec()  

    def register(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        encrypted_password = self.encrypt_password(password)
        mydb = mysql.connector.connect(
            host = "db4free.net",
            user = "thehaternoob",
            password = "palarga123",
            database = "thehaternoob"
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO usuarios (id_usuario,identidad, nombre, rol, telefono, password) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (self.list_size+1,12345678, username, "normal", 1234567890, encrypted_password)
        mycursor.execute(sql, val)  
        mydb.commit()
        msg_box = QMessageBox()
        msg_box.setText(" SE HA REGISTRADO")  
        msg_box.exec()      
        mycursor.close()
        mydb.close()
        self.get_usuario_data()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = login()
    widget.show()
    sys.exit(app.exec())
