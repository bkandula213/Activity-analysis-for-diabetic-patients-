# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dinpfil.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(671, 303)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 210, 191, 31))
        self.pushButton.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(190, 10, 451, 33))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 151, 21))
        self.label.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 151, 21))
        self.label_2.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 70, 451, 33))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 151, 21))
        self.label_3.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 120, 451, 33))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 210, 191, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 210, 181, 31))
        self.pushButton_3.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 581, 301))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../Users/home/Documents/image.jpg"))
        self.label_4.setObjectName("label_4")
        self.label_4.raise_()
        self.pushButton.raise_()
        self.lineEdit.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.lineEdit_2.raise_()
        self.label_3.raise_()
        self.lineEdit_3.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Accept Data Input Files"))
        self.pushButton.setText(_translate("MainWindow", "Accept Type_1 Bending  file"))
        self.label.setText(_translate("MainWindow", "Type_1 Bending  file:"))
        self.label_2.setText(_translate("MainWindow", "Type_2 Bending  file:"))
        self.label_3.setText(_translate("MainWindow", "Cycling File:"))
        self.pushButton_2.setText(_translate("MainWindow", "Accept Type_2 Bending  file:"))
        self.pushButton_3.setText(_translate("MainWindow", "Accept Cycling File "))
