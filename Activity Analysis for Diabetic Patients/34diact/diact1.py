import sys
import os
from diact import *
from PyQt5 import QtWidgets, QtGui, QtCore

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.dinpgui)
     self.ui.pushButton_2.clicked.connect(self.dinpfil)
     self.ui.pushButton_3.clicked.connect(self.timespe)
     self.ui.pushButton_4.clicked.connect(self.calspe)
     self.ui.pushButton_5.clicked.connect(self.pdetails)

       

  def dinpgui(self):
    os.system("python datainpgui1.py")

  def pdetails(self):
    os.system("python patientdtls1.py")

  def dinpfil(self):
    os.system("python datainpfil1.py")

  def timespe(self):
    os.system("python samp2.py")

  def calspe(self):
    os.system("python samp3.py")

#  def gnrep(self):
#	os.system("python genrep1.py")
       

if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
