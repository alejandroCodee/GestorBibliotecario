########################################################################
## IMPORTS
########################################################################
import os
import sys
########################################################################
# IMPORT GUI FILE
from src.functions import Functions

########################################################################
########################################################################
# IMPORT Custom widgets
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from login import login 

from src.functions_user import FunctionsUser
from src.ui_interface import Ui_MainWindow
from src.ui_interface_user import Ui_UserMain

########################################################################

########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)


        self.ui_admin = Ui_MainWindow()
        self.ui_user = Ui_UserMain()



        # Para trabajar con la interfaz de administrador
        # Para trabajar con la interfaz de usuario
        self.login_window = login()
        self.login_window.show()
        self.login_window.session_closed.connect(self.show_main_window)

        
        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################


    def show_main_window(self):
        # Cierra la ventana de login y muestra la ventana principal
        self.login_window.close()
        rol = self.login_window.obtener_rol()
        if rol == "ADMIN":
            self.ui_admin.setupUi(self)
            loadJsonStyle(self, self.ui_admin, jsonFiles={"json-styles/style.json"}) 
            self.functions_admin = Functions(self.ui_admin)
            self.show()
        else:
            self.ui_user.setupUi(self)
            loadJsonStyle(self, self.ui_user, jsonFiles={"json-styles/style_user.json"}) 
            self.functions_user = FunctionsUser(self.ui_user)   
            self.show()
        

    
    #def update_app_settings(self):
     #   QAppSettings.updateAppSettings(self)

########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    #window.update_app_settings()  # Llama a la función para actualizar la configuración de la aplicación
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  