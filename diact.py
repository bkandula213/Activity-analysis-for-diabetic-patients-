# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diact.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(582, 306)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(130, 70, 271, 31))
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 120, 271, 31))
        self.pushButton_2.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 170, 271, 31))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(130, 220, 271, 31))
        self.pushButton_4.setStyleSheet("\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 0);\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        #self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        #self.pushButton_5.setGeometry(QtCore.QRect(130, 20, 271, 31))
        #self.pushButton_5.setMaximumSize(QtCore.QSize(271, 16777215))
        #self.pushButton_5.setStyleSheet("background-color: rgb(255, 170, 0);\n"
        #"font: 75 14pt \"MS Shell Dlg 2\";")
        #self.pushButton_5.setObjectName("pushButton_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 571, 321))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Users/home/Documents/image.jpg"))
        self.label.setObjectName("label")
        self.label.raise_()
        self.pushButton_5.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        #self.pushButton_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Diabetic Activity Analysis"))
        self.pushButton_5.setText(_translate("MainWindow", "Patient Profile Details"))
        self.pushButton_2.setText(_translate("MainWindow", "Data Input through Files"))
        self.pushButton_3.setText(_translate("MainWindow", "Calculate Time Spent"))
        self.pushButton_4.setText(_translate("MainWindow", "Calculate Calories Spent"))
        #self.pushButton_5.setText(_translate("MainWindow", "Patient Profile Details"))
