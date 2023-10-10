import sys
import os 
from dinpfil import *
from PyQt5 import QtWidgets, QtGui, QtCore

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.checkfile1)
     self.ui.pushButton_2.clicked.connect(self.checkfile2)
     self.ui.pushButton_3.clicked.connect(self.checkfile3)

  

  def checkfile1(self):        
         
        fname = str(self.ui.lineEdit.text())
        if (os.path.isfile(fname)):
          print(' file exists')
        else:
          print(' file does not exists') 

  def checkfile2(self):        
         
        fname = str(self.ui.lineEdit_2.text())
        if (os.path.isfile(fname)):
          print(' file exists')
        else:
          print(' file does not exists')

  def checkfile3(self):        
         
        fname = str(self.ui.lineEdit_3.text())
        if (os.path.isfile(fname)):
          print(' file exists')
        else:
          print(' file does not exists')     

if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
