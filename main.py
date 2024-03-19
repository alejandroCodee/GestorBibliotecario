
########################################################################
## IMPORTS
########################################################################
import os
import sys
########################################################################
# IMPORT GUI FILE
from src.ui_interface import *
from src.functions import Functions
from src.ui_interface_user import *

########################################################################
########################################################################
# IMPORT Custom widgets
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from login import login 
from src.functions_user import FunctionsUser
########################################################################

########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui_admin = Ui_MainWindow()
        self.ui_user = Ui_UserMain()
        
        self.ui_admin.setupUi(self)
        self.ui_user.setupUi(self)
        
        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        loadJsonStyle(self, self.ui_admin, jsonFiles={"json-styles/style.json"}) 
        loadJsonStyle(self, self.ui_user, jsonFiles={"json-styles/style.json"}) 
        
        self.functions = Functions(self.ui)
        

        self.login_window = login()
        self.login_window.show()

        
        self.login_window.session_closed.connect(self.show_main_window)

        #######################################################################

    #######################################################################
    # SHOW WINDOW
    #######################################################################
    def show_main_window(self):
        # Cierra la ventana de login y muestra la ventana principal
        self.login_window.close()
        
        user = FunctionsUser(self.ui)
        rol = user.obtener_rol()
        if (rol == "ADMIN"):
            self.ui_admin.show()
        else:
            self.ui_user.show()
            
        
        

    ########################################################################
    # UPDATE APP SETTINGS LOADED FROM JSON STYLESHEET 
    # IT'S IMPORTANT TO RUN THIS AFTER SHOWING THE WINDOW
    # THIS PROCESS WILL RUN ON A SEPARATE THREAD WHEN GENERATING NEW ICONS
    # TO PREVENT THE WINDOW FROM BEING UNRESPONSIVE
    ########################################################################
    def update_app_settings(self):
        QAppSettings.updateAppSettings(self)

########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.update_app_settings()  # Llama a la función para actualizar la configuración de la aplicación
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  