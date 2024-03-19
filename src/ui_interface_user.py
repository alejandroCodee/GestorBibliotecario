# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

from Custom_Widgets.Theme import (QLabelThemed, QPushButtonThemed)
from Custom_Widgets.Widgets import (QCustomSlideMenu, QCustomStackedWidget)

class Ui_UserMain(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(990, 597)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(2, 63, 82);\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setStyleSheet(u"	background-color: rgb(0, 133, 175);")
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frameIzq = QFrame(self.header)
        self.frameIzq.setObjectName(u"frameIzq")
        self.frameIzq.setFrameShape(QFrame.StyledPanel)
        self.frameIzq.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frameIzq)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.menubtn = QPushButtonThemed(self.frameIzq)
        self.menubtn.setObjectName(u"menubtn")
        self.menubtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"../../Qss/icons/Icons/feather/align-justify.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menubtn.setIcon(icon)
        self.menubtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_4.addWidget(self.menubtn, 0, Qt.AlignLeft)

        self.label = QLabelThemed(self.frameIzq)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setPointSize(40)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.label)


        self.horizontalLayout.addWidget(self.frameIzq, 0, Qt.AlignLeft)

        self.frameDer = QFrame(self.header)
        self.frameDer.setObjectName(u"frameDer")
        self.frameDer.setFrameShape(QFrame.StyledPanel)
        self.frameDer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frameDer)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Settings = QPushButtonThemed(self.frameDer)
        self.Settings.setObjectName(u"Settings")
        self.Settings.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"../../Qss/icons/Icons/feather/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Settings.setIcon(icon1)
        self.Settings.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.Settings)

        self.User = QPushButtonThemed(self.frameDer)
        self.User.setObjectName(u"User")
        self.User.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"../../Qss/icons/Icons/feather/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.User.setIcon(icon2)
        self.User.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.User)


        self.horizontalLayout.addWidget(self.frameDer, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignTop)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy)
        self.mainBody.setMinimumSize(QSize(990, 504))
        self.mainBody.setStyleSheet(u"	background-color: rgb(0, 133, 175);")
        self.horizontalLayout_2 = QHBoxLayout(self.mainBody)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.MenuIzq = QCustomSlideMenu(self.mainBody)
        self.MenuIzq.setObjectName(u"MenuIzq")
        self.MenuIzq.setMinimumSize(QSize(200, 0))
        self.MenuIzq.setMaximumSize(QSize(0, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.MenuIzq)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 0, 0, 9)
        self.widget = QWidget(self.MenuIzq)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(195, 486))
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(40, 40))
        font1 = QFont()
        font1.setFamilies([u"Century Gothic"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"text-align: left;\n"
"background-color: rgb(2, 63, 82);\n"
"color: rgb(255, 255, 255);\n"
"border-left-color: rgb(255, 255, 255);")
        icon3 = QIcon()
        icon3.addFile(u"../Qss/icons/Icons/feather/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setIconSize(QSize(40, 40))

        self.verticalLayout_5.addWidget(self.pushButton_2)


        self.verticalLayout_4.addWidget(self.frame)

        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Ayuda = QPushButtonThemed(self.frame_2)
        self.Ayuda.setObjectName(u"Ayuda")
        font2 = QFont()
        font2.setFamilies([u"Century Gothic"])
        font2.setPointSize(10)
        self.Ayuda.setFont(font2)
        self.Ayuda.setCursor(QCursor(Qt.PointingHandCursor))
        self.Ayuda.setStyleSheet(u"text-align: left;\n"
"color: rgb(255, 255, 255);")
        icon4 = QIcon()
        icon4.addFile(u"../../Qss/icons/Icons/material_design/help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Ayuda.setIcon(icon4)
        self.Ayuda.setIconSize(QSize(30, 30))

        self.verticalLayout_6.addWidget(self.Ayuda)

        self.Informacion = QPushButtonThemed(self.frame_2)
        self.Informacion.setObjectName(u"Informacion")
        self.Informacion.setFont(font2)
        self.Informacion.setCursor(QCursor(Qt.PointingHandCursor))
        self.Informacion.setStyleSheet(u"text-align: left;\n"
"color: rgb(255, 255, 255);")
        icon5 = QIcon()
        icon5.addFile(u"../../Qss/icons/Icons/material_design/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Informacion.setIcon(icon5)
        self.Informacion.setIconSize(QSize(30, 30))

        self.verticalLayout_6.addWidget(self.Informacion)


        self.verticalLayout_4.addWidget(self.frame_2)


        self.verticalLayout_3.addWidget(self.widget)


        self.horizontalLayout_2.addWidget(self.MenuIzq)

        self.Body = QWidget(self.mainBody)
        self.Body.setObjectName(u"Body")
        self.Body.setStyleSheet(u"background-color: rgb(2, 63, 82);")
        self.verticalLayout_2 = QVBoxLayout(self.Body)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 10, -1)
        self.mainPages = QCustomStackedWidget(self.Body)
        self.mainPages.setObjectName(u"mainPages")
        self.HomeP = QWidget()
        self.HomeP.setObjectName(u"HomeP")
        self.verticalLayout_20 = QVBoxLayout(self.HomeP)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.widget_6 = QWidget(self.HomeP)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_19 = QVBoxLayout(self.widget_6)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame_7 = QFrame(self.widget_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")
        font3 = QFont()
        font3.setFamilies([u"Century Gothic"])
        font3.setPointSize(26)
        font3.setBold(True)
        self.label_8.setFont(font3)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.label_8)

        self.Buscar_Libro = QLineEdit(self.frame_7)
        self.Buscar_Libro.setObjectName(u"Buscar_Libro")
        self.Buscar_Libro.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 8pt \"Century Gothic\";\n"
"border-color: rgb(255, 255, 255);\n"
"padding: 4px 10px;")

        self.horizontalLayout_7.addWidget(self.Buscar_Libro)

        self.buscar_libro = QPushButton(self.frame_7)
        self.buscar_libro.setObjectName(u"buscar_libro")
        font4 = QFont()
        font4.setFamilies([u"Century Gothic"])
        self.buscar_libro.setFont(font4)
        self.buscar_libro.setStyleSheet(u"background-color: rgb(0, 133, 175);\n"
"color: rgb(255, 255, 255);")
        icon6 = QIcon()
        icon6.addFile(u"../Qss/icons/Icons/feather/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buscar_libro.setIcon(icon6)
        self.buscar_libro.setIconSize(QSize(20, 20))

        self.horizontalLayout_7.addWidget(self.buscar_libro)


        self.verticalLayout_19.addWidget(self.frame_7)

        self.refresh = QPushButton(self.widget_6)
        self.refresh.setObjectName(u"refresh")

        self.verticalLayout_19.addWidget(self.refresh, 0, Qt.AlignLeft)

        self.HomeTable = QTableWidget(self.widget_6)
        if (self.HomeTable.columnCount() < 5):
            self.HomeTable.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.HomeTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.HomeTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.HomeTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.HomeTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.HomeTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.HomeTable.setObjectName(u"HomeTable")

        self.verticalLayout_19.addWidget(self.HomeTable)

        self.alquilar_btn = QPushButton(self.widget_6)
        self.alquilar_btn.setObjectName(u"alquilar_btn")
        font5 = QFont()
        font5.setFamilies([u"Century Gothic"])
        font5.setPointSize(10)
        font5.setBold(True)
        self.alquilar_btn.setFont(font5)
        self.alquilar_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.alquilar_btn.setStyleSheet(u"\n"
"background-color: rgb(0, 133, 175);\n"
"padding: 5px 10px;\n"
"border-radius: 5px;\n"
"\n"
"color: rgb(255, 255, 255);")
        icon7 = QIcon()
        icon7.addFile(u"../Qss/icons/Icons/feather/shopping-cart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.alquilar_btn.setIcon(icon7)
        self.alquilar_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_19.addWidget(self.alquilar_btn, 0, Qt.AlignRight)


        self.verticalLayout_20.addWidget(self.widget_6)

        self.mainPages.addWidget(self.HomeP)
        self.prestamosP = QWidget()
        self.prestamosP.setObjectName(u"prestamosP")
        self.verticalLayout_10 = QVBoxLayout(self.prestamosP)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_3 = QWidget(self.prestamosP)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_11 = QVBoxLayout(self.widget_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_4 = QFrame(self.widget_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabelThemed(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        font6 = QFont()
        font6.setFamilies([u"Century Gothic"])
        font6.setPointSize(28)
        font6.setBold(True)
        self.label_3.setFont(font6)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_3, 0, Qt.AlignLeft)

        self.showForm = QPushButtonThemed(self.frame_4)
        self.showForm.setObjectName(u"showForm")
        font7 = QFont()
        font7.setFamilies([u"Century Gothic"])
        font7.setPointSize(11)
        font7.setBold(True)
        self.showForm.setFont(font7)
        self.showForm.setCursor(QCursor(Qt.PointingHandCursor))
        self.showForm.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(2, 63, 82);")
        icon8 = QIcon()
        icon8.addFile(u"../../../../Qss/icons/Icons/feather/log-in.png", QSize(), QIcon.Normal, QIcon.Off)
        self.showForm.setIcon(icon8)
        self.showForm.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.showForm, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.frame_4)

        self.refresh_prestamos = QPushButton(self.widget_3)
        self.refresh_prestamos.setObjectName(u"refresh_prestamos")

        self.verticalLayout_11.addWidget(self.refresh_prestamos, 0, Qt.AlignLeft)

        self.prestamos_tabla = QTableWidget(self.widget_3)
        if (self.prestamos_tabla.columnCount() < 5):
            self.prestamos_tabla.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.prestamos_tabla.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.prestamos_tabla.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.prestamos_tabla.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.prestamos_tabla.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.prestamos_tabla.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        self.prestamos_tabla.setObjectName(u"prestamos_tabla")

        self.verticalLayout_11.addWidget(self.prestamos_tabla)


        self.verticalLayout_10.addWidget(self.widget_3)

        self.mainPages.addWidget(self.prestamosP)
        self.catalogoP = QWidget()
        self.catalogoP.setObjectName(u"catalogoP")
        self.verticalLayout_13 = QVBoxLayout(self.catalogoP)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.widget_4 = QWidget(self.catalogoP)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_14 = QVBoxLayout(self.widget_4)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_5 = QFrame(self.widget_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabelThemed(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font6)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_5)

        self.showFormC = QPushButtonThemed(self.frame_5)
        self.showFormC.setObjectName(u"showFormC")

        self.horizontalLayout_6.addWidget(self.showFormC, 0, Qt.AlignRight)


        self.verticalLayout_14.addWidget(self.frame_5)

        self.Buscar_Catalogo = QLineEdit(self.widget_4)
        self.Buscar_Catalogo.setObjectName(u"Buscar_Catalogo")

        self.verticalLayout_14.addWidget(self.Buscar_Catalogo)

        self.refresh_catalogo = QPushButton(self.widget_4)
        self.refresh_catalogo.setObjectName(u"refresh_catalogo")

        self.verticalLayout_14.addWidget(self.refresh_catalogo, 0, Qt.AlignLeft)

        self.tableWidget_2 = QTableWidget(self.widget_4)
        if (self.tableWidget_2.columnCount() < 12):
            self.tableWidget_2.setColumnCount(12)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(9, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(10, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(11, __qtablewidgetitem21)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.verticalLayout_14.addWidget(self.tableWidget_2)


        self.verticalLayout_13.addWidget(self.widget_4)

        self.mainPages.addWidget(self.catalogoP)
        self.reportesP = QWidget()
        self.reportesP.setObjectName(u"reportesP")
        self.label_2 = QLabelThemed(self.reportesP)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 30, 231, 71))
        self.label_2.setFont(font6)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.mainPages.addWidget(self.reportesP)
        self.ayudaP = QWidget()
        self.ayudaP.setObjectName(u"ayudaP")
        self.verticalLayout_12 = QVBoxLayout(self.ayudaP)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_6 = QLabelThemed(self.ayudaP)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font6)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_6)

        self.mainPages.addWidget(self.ayudaP)
        self.infoP = QWidget()
        self.infoP.setObjectName(u"infoP")
        self.gridLayout = QGridLayout(self.infoP)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_7 = QWidget(self.infoP)
        self.widget_7.setObjectName(u"widget_7")
        self.label_4 = QLabelThemed(self.widget_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 30, 264, 45))
        self.label_4.setFont(font6)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.widget_7, 0, 0, 1, 1)

        self.mainPages.addWidget(self.infoP)

        self.verticalLayout_2.addWidget(self.mainPages)


        self.horizontalLayout_2.addWidget(self.Body)

        self.MenuDer = QCustomSlideMenu(self.mainBody)
        self.MenuDer.setObjectName(u"MenuDer")
        self.MenuDer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_7 = QVBoxLayout(self.MenuDer)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.Menu_Der = QTabWidget(self.MenuDer)
        self.Menu_Der.setObjectName(u"Menu_Der")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_15 = QVBoxLayout(self.tab)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.widget_2 = QWidget(self.tab)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_8 = QVBoxLayout(self.widget_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.title = QLabelThemed(self.widget_2)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(70, 70))
        self.title.setMaximumSize(QSize(90, 90))
        self.title.setPixmap(QPixmap(u"../../../../Qss/icons/Icons/feather/file-plus.png"))

        self.verticalLayout_8.addWidget(self.title, 0, Qt.AlignHCenter)

        self.frame_3 = QFrame(self.widget_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.fecha_devolucion = QDateEdit(self.frame_3)
        self.fecha_devolucion.setObjectName(u"fecha_devolucion")
        self.fecha_devolucion.setStyleSheet(u"background-color: rgb(2, 63, 82);\n"
"padding: 5px 10px;\n"
"border-radius: 5px;\n"
"\n"
"color: rgb(255, 255, 255);")
        self.fecha_devolucion.setCalendarPopup(True)

        self.verticalLayout_9.addWidget(self.fecha_devolucion)

        self.usuario_LE = QLineEdit(self.frame_3)
        self.usuario_LE.setObjectName(u"usuario_LE")
        self.usuario_LE.setStyleSheet(u"background-color: rgb(2, 63, 82);\n"
"padding: 5px 10px;\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_9.addWidget(self.usuario_LE)


        self.verticalLayout_8.addWidget(self.frame_3)

        self.Add = QPushButtonThemed(self.widget_2)
        self.Add.setObjectName(u"Add")
        self.Add.setFont(font7)
        self.Add.setCursor(QCursor(Qt.PointingHandCursor))
        self.Add.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(2, 63, 82);\n"
"")
        icon9 = QIcon()
        icon9.addFile(u"../../../../Qss/icons/Icons/feather/check-square.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Add.setIcon(icon9)
        self.Add.setIconSize(QSize(25, 25))

        self.verticalLayout_8.addWidget(self.Add, 0, Qt.AlignHCenter)


        self.verticalLayout_15.addWidget(self.widget_2)

        self.Menu_Der.addTab(self.tab, "")

        self.verticalLayout_7.addWidget(self.Menu_Der)


        self.horizontalLayout_2.addWidget(self.MenuDer)


        self.verticalLayout.addWidget(self.mainBody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainPages.setCurrentIndex(0)
        self.Menu_Der.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menubtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"SISTEBIB", None))
        self.Settings.setText("")
        self.User.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.Ayuda.setText(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.Informacion.setText(QCoreApplication.translate("MainWindow", u"Informaci\u00f3n", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"LIBROS", None))
        self.Buscar_Libro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u00a1Busca tu libro favorito!", None))
        self.buscar_libro.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        self.refresh.setText(QCoreApplication.translate("MainWindow", u"R", None))
        ___qtablewidgetitem = self.HomeTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Titulo", None));
        ___qtablewidgetitem1 = self.HomeTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Autor", None));
        ___qtablewidgetitem2 = self.HomeTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Sinopsis", None));
        ___qtablewidgetitem3 = self.HomeTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"A\u00f1o", None));
        ___qtablewidgetitem4 = self.HomeTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Genero", None));
        self.alquilar_btn.setText(QCoreApplication.translate("MainWindow", u"ALQUILAR", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"PRESTAMOS", None))
        self.showForm.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir Prestamo", None))
        self.refresh_prestamos.setText(QCoreApplication.translate("MainWindow", u"R", None))
        ___qtablewidgetitem5 = self.prestamos_tabla.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"CODIGO", None));
        ___qtablewidgetitem6 = self.prestamos_tabla.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"FECHA PRESTAMO", None));
        ___qtablewidgetitem7 = self.prestamos_tabla.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"FECHA DEVOLUCION", None));
        ___qtablewidgetitem8 = self.prestamos_tabla.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"LIBRO", None));
        ___qtablewidgetitem9 = self.prestamos_tabla.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"USUARIO", None));
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"CATALOGO", None))
        self.showFormC.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir Libro", None))
        self.refresh_catalogo.setText(QCoreApplication.translate("MainWindow", u"R", None))
        ___qtablewidgetitem10 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"ISBN", None));
        ___qtablewidgetitem11 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"TITULO", None));
        ___qtablewidgetitem12 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"GENERO", None));
        ___qtablewidgetitem13 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"AUTOR", None));
        ___qtablewidgetitem14 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"A\u00d1O DE PUBLICACI\u00d3N", None));
        ___qtablewidgetitem15 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"DISPONIBLE", None));
        ___qtablewidgetitem16 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"FORMATO", None));
        ___qtablewidgetitem17 = self.tableWidget_2.horizontalHeaderItem(7)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"COPIAS", None));
        ___qtablewidgetitem18 = self.tableWidget_2.horizontalHeaderItem(8)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"IDIOMA", None));
        ___qtablewidgetitem19 = self.tableWidget_2.horizontalHeaderItem(9)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"RESUMEN", None));
        ___qtablewidgetitem20 = self.tableWidget_2.horizontalHeaderItem(10)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"UBICACI\u00d3N/PASILLO", None));
        ___qtablewidgetitem21 = self.tableWidget_2.horizontalHeaderItem(11)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"ESTADO", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"REPORTES", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"AYUDA", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"INFORMACI\u00d3N", None))
        self.title.setText("")
        self.usuario_LE.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.Add.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.Menu_Der.setTabText(self.Menu_Der.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
    # retranslateUi

