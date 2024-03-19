# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QStackedWidget,
    QWidget)

class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(817, 546)
        login.setStyleSheet(u"\n"
"background-color: rgb(0, 133, 175);")
        self.stackedWidget = QStackedWidget(login)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(40, 130, 341, 371))
        self.login_2 = QWidget()
        self.login_2.setObjectName(u"login_2")
        self.lineEdit_2 = QLineEdit(self.login_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(70, 150, 211, 31))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(2, 63, 82);\n"
"padding: 5px 10px;\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.lineEdit = QLineEdit(self.login_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(70, 70, 211, 31))
        self.lineEdit.setStyleSheet(u"\n"
"\n"
"background-color: rgb(2, 63, 82);\n"
"padding: 5px 10px;\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.line = QFrame(self.login_2)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(50, 100, 271, 51))
        self.line.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.pushButton = QPushButton(self.login_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(60, 210, 231, 41))
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(2, 63, 82);\n"
"border-radius: 5px;")
        self.crear = QPushButton(self.login_2)
        self.crear.setObjectName(u"crear")
        self.crear.setGeometry(QRect(80, 280, 191, 24))
        font1 = QFont()
        font1.setFamilies([u"Century Gothic"])
        font1.setPointSize(7)
        self.crear.setFont(font1)
        self.crear.setStyleSheet(u"background-color: rgb(2, 63, 82);\n"
"padding: 5px 10px;\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.login_2)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.pushButton_2 = QPushButton(self.page_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(60, 270, 231, 41))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(2, 63, 82);\n"
"border-radius: 5px;")
        self.identidad_LE = QLineEdit(self.page_4)
        self.identidad_LE.setObjectName(u"identidad_LE")
        self.identidad_LE.setGeometry(QRect(70, 20, 211, 31))
        self.identidad_LE.setStyleSheet(u"background-color: rgb(2, 63, 82);\n"
"padding: 5px 10px;\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"font: 700 9pt \"Century Gothic\";")
        self.user_LE = QLineEdit(self.page_4)
        self.user_LE.setObjectName(u"user_LE")
        self.user_LE.setGeometry(QRect(70, 70, 211, 31))
        self.user_LE.setStyleSheet(u"background-color: rgb(2, 63, 82);\n"
"padding: 5px 10px;\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"font: 700 9pt \"Century Gothic\";")
        self.telefono_LE = QLineEdit(self.page_4)
        self.telefono_LE.setObjectName(u"telefono_LE")
        self.telefono_LE.setGeometry(QRect(70, 120, 211, 31))
        self.telefono_LE.setStyleSheet(u"background-color: rgb(2, 63, 82);\n"
"padding: 5px 10px;\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"font: 700 9pt \"Century Gothic\";")
        self.tipo_LE = QComboBox(self.page_4)
        self.tipo_LE.addItem("")
        self.tipo_LE.addItem("")
        self.tipo_LE.setObjectName(u"tipo_LE")
        self.tipo_LE.setGeometry(QRect(69, 220, 211, 31))
        self.tipo_LE.setStyleSheet(u"background-color: rgb(2, 63, 82);\n"
"padding: 5px 10px;\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"font: 700 9pt \"Century Gothic\";")
        self.password_LE = QLineEdit(self.page_4)
        self.password_LE.setObjectName(u"password_LE")
        self.password_LE.setGeometry(QRect(70, 170, 211, 31))
        self.password_LE.setStyleSheet(u"background-color: rgb(2, 63, 82);\n"
"padding: 5px 10px;\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"font: 700 9pt \"Century Gothic\";")
        self.pushButton_3 = QPushButton(self.page_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(140, 320, 51, 21))
        self.pushButton_3.setStyleSheet(u"font: 700 7pt \"Century Gothic\";\n"
"\n"
"background-color: rgb(2, 63, 82);\n"
"padding: 5px 10px;\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.page_4)
        self.titulo = QLabel(login)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QRect(100, 50, 241, 51))
        font2 = QFont()
        font2.setFamilies([u"Century Gothic"])
        font2.setPointSize(48)
        font2.setBold(False)
        self.titulo.setFont(font2)
        self.titulo.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.widget = QWidget(login)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(430, 0, 401, 551))
        self.widget.setStyleSheet(u"background-color: rgb(2, 63, 82);")

        self.retranslateUi(login)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"login", None))
        self.pushButton.setText(QCoreApplication.translate("login", u"LOG IN", None))
        self.crear.setText(QCoreApplication.translate("login", u"\u00bfNo tienes una cuenta? \u00a1Crea una!", None))
        self.pushButton_2.setText(QCoreApplication.translate("login", u"REGISTRARSE", None))
        self.tipo_LE.setItemText(0, QCoreApplication.translate("login", u"NORMAL", None))
        self.tipo_LE.setItemText(1, QCoreApplication.translate("login", u"ADMIN", None))

        self.pushButton_3.setText(QCoreApplication.translate("login", u"LOGIN", None))
        self.titulo.setText(QCoreApplication.translate("login", u"SISTEBIB", None))
    # retranslateUi

