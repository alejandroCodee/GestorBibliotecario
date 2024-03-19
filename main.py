########################################################################
## QT GUI BY SPINN TV(YOUTUBE)
########################################################################

########################################################################
## IMPORTS
########################################################################
import os
import sys
########################################################################
# IMPORT GUI FILE
from src.ui_interface import *
from src.functions import Functions

########################################################################
########################################################################
# IMPORT Custom widgets
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from login import login 
########################################################################

########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        loadJsonStyle(self, self.ui, jsonFiles={"json-styles/style.json"}) 

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
        self.show()

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
