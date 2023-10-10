#This program gets two values from a DB into lineEdits.
import random

import sys
from disply import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import MySQLdb as mdb

con = mdb.connect('localhost', 'root', 'yogibaba9', 'coatoq'); 

class MyForm(QtGui.QMainWindow):
  def __init__(self,parent=None):
     QtGui.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL('clicked()'),self.displayvalues)
     QtCore.QObject.connect(self.ui.pushButton_2,QtCore.SIGNAL('clicked()'),self.evaluateqp)
     QtCore.QObject.connect(self.ui.pushButton_3,QtCore.SIGNAL('clicked()'),self.assescos)

  def displayvalues(self):
         
     with con:
    
        cur = con.cursor()
        self.ui.lineEdit.text()
        global s,co1,co2,co3,co4,ao1,ao2,ao3,ao4
        global List1
        List1 = []
        s = " "
        co1 = 0
	co2 = 0
	co3 = 0
	co4 = 0
	ao1 = 0
	ao2 = 0
	ao3 = 0
	ao4 = 0
        for i in range(1,5):
          j = random.randint(1,20)
          #To Do: Need to write code to avoid duplicate/same random numbers
          cur.execute('SELECT QuestionDesc FROM Question where QuestionId = %r;' % j); 
          result = cur.fetchall()
          for row in result:
  	    result1 = row[0]
            if (i == 1) : (self.ui.lineEdit.setText(result1))
            elif (i == 2) : (self.ui.lineEdit_2.setText(result1))
	    elif (i == 3) : (self.ui.lineEdit_3.setText(result1))
            else : (self.ui.lineEdit_4.setText(result1))
          cur.execute('SELECT QOptA FROM Question where QuestionId = %r;' % j); 
          result2 = cur.fetchall()
          for row in result2:
  	    result3 = row[0]
            if (i == 1) : (self.ui.lineEdit_5.setText(result3))
            elif (i == 2) : (self.ui.lineEdit_9.setText(result3))
	    elif (i == 3) : (self.ui.lineEdit_13.setText(result3))
            else : (self.ui.lineEdit_17.setText(result3))
            #To Do: Need to write code to add remaining three options
          cur.execute('SELECT QOptB FROM Question where QuestionId = %r;' % j); 
          result2 = cur.fetchall()
          for row in result2:
  	    result3 = row[0]
            if (i == 1) : (self.ui.lineEdit_6.setText(result3))
            elif (i == 2) : (self.ui.lineEdit_10.setText(result3))
	    elif (i == 3) : (self.ui.lineEdit_14.setText(result3))
            else : (self.ui.lineEdit_18.setText(result3))
          cur.execute('SELECT QOptC FROM Question where QuestionId = %r;' % j); 
          result2 = cur.fetchall()
          for row in result2:
  	    result3 = row[0]
            if (i == 1) : (self.ui.lineEdit_7.setText(result3))
            elif (i == 2) : (self.ui.lineEdit_11.setText(result3))
	    elif (i == 3) : (self.ui.lineEdit_15.setText(result3))
            else : (self.ui.lineEdit_19.setText(result3))
          cur.execute('SELECT QOptD FROM Question where QuestionId = %r;' % j); 
          result2 = cur.fetchall()
          for row in result2:
  	    result3 = row[0]
            if (i == 1) : (self.ui.lineEdit_8.setText(result3))
            elif (i == 2) : (self.ui.lineEdit_12.setText(result3))
	    elif (i == 3) : (self.ui.lineEdit_16.setText(result3))
            else : (self.ui.lineEdit_20.setText(result3))
	  cur.execute('SELECT Answer FROM Answer where QuestionId = %r;' % j); 
          answer = cur.fetchall()
          for row in answer:
  	    ans = row[0]
            s+=ans
	  cur.execute('SELECT OutcomeId FROM Question where QuestionId = %r;' % j); 
          outcome = cur.fetchall()
          for row in outcome:
  	    oc = row[0]
            if (oc == '1') : co1 = co1 + 1
            elif (oc == '2') : co2 = co2 + 1
	    elif (oc == '3') : co3 = co3 + 1
	    elif (oc == '4') : co4 = co4 + 1
	  List1.append(j);
	  print "Updated List : ", List1  # This is working
            
  def evaluateqp(self):
         
     with con:
        global s,ao1,ao2,ao3,ao4,List1 #ao stands for attained outcome
        # ao1 = 0
        # ao2 = 0
        # ao3 = 0
        # ao4 = 0
        cur = con.cursor()
	print s
        stuAns = " "+str(self.ui.lineEdit_41.text())+str(self.ui.lineEdit_42.text())+str(self.ui.lineEdit_43.text())+str(self.ui.lineEdit_44.text())
        marks = 0
	for i in range(1,len(s)):
    	  if (s[i] == stuAns[i]): 
	    marks = marks +1
            k = List1[i-1]
            cur.execute('SELECT OutcomeId FROM Question where QuestionId = %r;' % k); 
            outcome = cur.fetchall()
            for row in outcome:
  	       oc = row[0]
               if (oc == '1') : ao1 = ao1 + 1
               elif (oc == '2') : ao2 = ao2 + 1
	       elif (oc == '3') : ao3 = ao3 + 1
	       elif (oc == '4') : ao4 = ao4 + 1
        
	print marks

  def assescos(self):
         
     with con:
        global co1,co2,co3,co4,ao1,ao2,ao3,ao4
        print co1,co2,co3,co4  #These are the outcomes for the selected questions
        print ao1,ao2,ao3,ao4  #These are the attained outcomes

if __name__ == "__main__":  
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())


   
	

