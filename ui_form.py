# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(444, 546)
        login.setStyleSheet(u"\n"
"background-color: rgb(77, 161, 167);")
        self.pushButton = QPushButton(login)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(100, 400, 231, 41))
        self.pushButton_2 = QPushButton(login)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(100, 460, 231, 41))
        self.lineEdit = QLineEdit(login)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(110, 210, 151, 31))
        self.lineEdit.setStyleSheet(u"border-color: rgba(255, 255, 255, 0);")
        self.lineEdit_2 = QLineEdit(login)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(110, 290, 211, 31))
        self.line = QFrame(login)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(100, 240, 261, 51))
        self.line.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_2 = QLabel(login)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 210, 41, 31))
        self.label_2.setStyleSheet(u"border-image: url(:/icons/icons/user_32x32.png);")
        self.label_3 = QLabel(login)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 290, 41, 31))
        self.label_3.setStyleSheet(u"image: url(:/icons/icons/lock_32x32.png);")
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.lineEdit_2.raise_()
        self.line.raise_()
        self.lineEdit.raise_()
        self.label_2.raise_()
        self.label_3.raise_()

        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"login", None))
        self.pushButton.setText(QCoreApplication.translate("login", u"LOG IN", None))
        self.pushButton_2.setText(QCoreApplication.translate("login", u"REGISTRARSE", None))
        self.label_2.setText("")
        self.label_3.setText("")
    # retranslateUi

