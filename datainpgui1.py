import sys
from dinpgui import *
from PyQt5 import QtWidgets, QtGui, QtCore

import sqlite3
con = sqlite3.connect('diact1')

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.insertvalues)

   

  def insertvalues(self):
         
     with con:
    
        cur = con.cursor()
        arss13 = str(self.ui.lineEdit.text())
        pid = str(self.ui.lineEdit_3.text())
        tseg = str(self.ui.lineEdit_4.text())
        vrss14 = str(self.ui.lineEdit_7.text())
        arss14 = str(self.ui.lineEdit_8.text())
        arss12 = str(self.ui.lineEdit_5.text())
        vrss12 = str(self.ui.lineEdit_6.text())	
        vrss13 = str(self.ui.lineEdit_2.text())
        actcode = str(self.ui.lineEdit_9.text())
        cur.execute('INSERT INTO dingui VALUES(?,?,?,?,?,?,?,?,?)',(pid,tseg,arss12,vrss12,arss13,vrss13,arss14,vrss14,actcode))
        con.commit()
        
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())


