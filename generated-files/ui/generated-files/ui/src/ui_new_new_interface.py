# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_new_new_interface.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLineEdit, QMainWindow, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

from Custom_Widgets.Theme import (QLabelThemed, QPushButtonThemed)
from Custom_Widgets.Widgets import (QCustomSlideMenu, QCustomStackedWidget)
class Ui_MainWindow(object):
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
        self.Prestamos = QPushButtonThemed(self.frame)
        self.Prestamos.setObjectName(u"Prestamos")
        font1 = QFont()
        font1.setFamilies([u"Century Gothic"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.Prestamos.setFont(font1)
        self.Prestamos.setCursor(QCursor(Qt.PointingHandCursor))
        self.Prestamos.setStyleSheet(u"text-align: left;\n"
"background-color: rgb(2, 63, 82);\n"
"color: rgb(255, 255, 255);\n"
"border-left-color: rgb(255, 255, 255);")
        icon3 = QIcon()
        icon3.addFile(u"../../Qss/icons/Icons/font_awesome/solid/cart-flatbed.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Prestamos.setIcon(icon3)
        self.Prestamos.setIconSize(QSize(40, 40))

        self.verticalLayout_5.addWidget(self.Prestamos)

        self.Catalogo = QPushButtonThemed(self.frame)
        self.Catalogo.setObjectName(u"Catalogo")
        font2 = QFont()
        font2.setFamilies([u"Century Gothic"])
        font2.setPointSize(12)
        self.Catalogo.setFont(font2)
        self.Catalogo.setCursor(QCursor(Qt.PointingHandCursor))
        self.Catalogo.setStyleSheet(u"text-align: left;\n"
"color: rgb(255, 255, 255);")
        icon4 = QIcon()
        icon4.addFile(u"../../Qss/icons/Icons/font_awesome/solid/book.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Catalogo.setIcon(icon4)
        self.Catalogo.setIconSize(QSize(40, 40))

        self.verticalLayout_5.addWidget(self.Catalogo)

        self.Reportes = QPushButtonThemed(self.frame)
        self.Reportes.setObjectName(u"Reportes")
        self.Reportes.setFont(font2)
        self.Reportes.setCursor(QCursor(Qt.PointingHandCursor))
        self.Reportes.setStyleSheet(u"text-align: left;\n"
"color: rgb(255, 255, 255);")
        icon5 = QIcon()
        icon5.addFile(u"../../Qss/icons/Icons/font_awesome/solid/file-signature.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Reportes.setIcon(icon5)
        self.Reportes.setIconSize(QSize(40, 40))

        self.verticalLayout_5.addWidget(self.Reportes)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


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
        font3 = QFont()
        font3.setFamilies([u"Century Gothic"])
        font3.setPointSize(10)
        self.Ayuda.setFont(font3)
        self.Ayuda.setCursor(QCursor(Qt.PointingHandCursor))
        self.Ayuda.setStyleSheet(u"text-align: left;\n"
"color: rgb(255, 255, 255);")
        icon6 = QIcon()
        icon6.addFile(u"../../Qss/icons/Icons/material_design/help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Ayuda.setIcon(icon6)
        self.Ayuda.setIconSize(QSize(30, 30))

        self.verticalLayout_6.addWidget(self.Ayuda)

        self.Informacion = QPushButtonThemed(self.frame_2)
        self.Informacion.setObjectName(u"Informacion")
        self.Informacion.setFont(font3)
        self.Informacion.setCursor(QCursor(Qt.PointingHandCursor))
        self.Informacion.setStyleSheet(u"text-align: left;\n"
"color: rgb(255, 255, 255);")
        icon7 = QIcon()
        icon7.addFile(u"../../Qss/icons/Icons/material_design/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Informacion.setIcon(icon7)
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
        font4 = QFont()
        font4.setFamilies([u"Century Gothic"])
        font4.setPointSize(28)
        font4.setBold(True)
        self.label_3.setFont(font4)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_3, 0, Qt.AlignLeft)

        self.showForm = QPushButtonThemed(self.frame_4)
        self.showForm.setObjectName(u"showForm")
        font5 = QFont()
        font5.setFamilies([u"Century Gothic"])
        font5.setPointSize(11)
        font5.setBold(True)
        self.showForm.setFont(font5)
        self.showForm.setCursor(QCursor(Qt.PointingHandCursor))
        self.showForm.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 133, 175);")
        icon8 = QIcon()
        icon8.addFile(u"../../../../Qss/icons/Icons/feather/log-in.png", QSize(), QIcon.Normal, QIcon.Off)
        self.showForm.setIcon(icon8)
        self.showForm.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.showForm, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.frame_4)

        self.tableWidget = QTableWidget(self.widget_3)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_11.addWidget(self.tableWidget)


        self.verticalLayout_10.addWidget(self.widget_3)

        self.mainPages.addWidget(self.prestamosP)
        self.catalogoP = QWidget()
        self.catalogoP.setObjectName(u"catalogoP")
        self.label_5 = QLabelThemed(self.catalogoP)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(280, 50, 231, 71))
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.mainPages.addWidget(self.catalogoP)
        self.reportesP = QWidget()
        self.reportesP.setObjectName(u"reportesP")
        self.label_2 = QLabelThemed(self.reportesP)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 40, 231, 71))
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.mainPages.addWidget(self.reportesP)
        self.ayudaP = QWidget()
        self.ayudaP.setObjectName(u"ayudaP")
        self.label_6 = QLabelThemed(self.ayudaP)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(280, 50, 231, 71))
        self.label_6.setFont(font4)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.mainPages.addWidget(self.ayudaP)
        self.infoP = QWidget()
        self.infoP.setObjectName(u"infoP")
        self.label_4 = QLabelThemed(self.infoP)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(220, 40, 391, 71))
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(Qt.AlignCenter)
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
        self.widget_2 = QWidget(self.MenuDer)
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
        self.lineEdit = QLineEdit(self.frame_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: rgb(2, 63, 82);\n"
"padding: 5px 10px;\n"
"border-radius: 5px;")

        self.verticalLayout_9.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.frame_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(2, 63, 82);\n"
"padding: 5px 10px;\n"
"border-radius: 5px;\n"
"")

        self.verticalLayout_9.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.frame_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(2, 63, 82);\n"
"padding: 5px 10px;\n"
"border-radius: 5px;")

        self.verticalLayout_9.addWidget(self.lineEdit_3)


        self.verticalLayout_8.addWidget(self.frame_3)

        self.Add = QPushButtonThemed(self.widget_2)
        self.Add.setObjectName(u"Add")
        self.Add.setFont(font5)
        self.Add.setCursor(QCursor(Qt.PointingHandCursor))
        self.Add.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(2, 63, 82);\n"
"")
        icon9 = QIcon()
        icon9.addFile(u"../../../../Qss/icons/Icons/feather/check-square.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Add.setIcon(icon9)
        self.Add.setIconSize(QSize(25, 25))

        self.verticalLayout_8.addWidget(self.Add, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.widget_2, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.MenuDer)


        self.verticalLayout.addWidget(self.mainBody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menubtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"SISTEBIB", None))
        self.Settings.setText("")
        self.User.setText("")
        self.Prestamos.setText(QCoreApplication.translate("MainWindow", u"Prestamos", None))
        self.Catalogo.setText(QCoreApplication.translate("MainWindow", u"Catalogo", None))
        self.Reportes.setText(QCoreApplication.translate("MainWindow", u"Reportes", None))
        self.Ayuda.setText(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.Informacion.setText(QCoreApplication.translate("MainWindow", u"Informaci\u00f3n", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"PRESTAMOS", None))
        self.showForm.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir Prestamo", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"CODIGO", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"FECHA PRESTAMO", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"FECHA DEVOLUCION", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"LIBRO", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"USUARIO", None));
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"CATALOGO", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"REPORTES", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"AYUDA", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"INFORMACI\u00d3N", None))
        self.title.setText("")
        self.Add.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
    # retranslateUi

