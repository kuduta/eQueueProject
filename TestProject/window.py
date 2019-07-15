# -*- coding: utf-8 -*-ซ


### size all for write 543 , start 150 to 693, 
###
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import *


class MainWindow(QWidget):
    def __init__(self):
       QWidget.__init__(self)
       self.setGeometry(100,100,1366,768)

       oImage = QImage("background1366.jpg")
       sImage = oImage.scaled(QSize(1366,768))                   # resize Image to widgets size
       palette = QPalette()
       palette.setBrush(10, QBrush(sImage))                     # 10 = Windowrole
       self.setPalette(palette)

       #self.label = QLabel('สวัสดีครับ สูตรเมนูอาหาร วิธีทำอาหาร เมนูต้ม เมนูแกง เมนูผัด เมนูทอด', self)                        # test, if it's really backgroundimage
       #self.label.setGeometry(0,0,200,50)
       #self.pushButton.setStyleSheet("background-color: red")
       #self.pushButton = QtGui.QPushButton(self)
       #self.pushButton.setGeometry(QtCore.QRect(120, 550, 150, 31))
       #self.pushButton.setObjectName(_fromUtf8("ทดสอบกดปุ่ม"))
       self.button1 = QPushButton('ทดสอบกดปุ่ม', self)
       
       self.button2 = QPushButton('Test2', self)
       self.button3 = QPushButton('Test3', self)
       self.button4 = QPushButton('Test4', self)
       self.button5 = QPushButton('Test5', self)
       self.button6 = QPushButton('Test6', self)
       self.button7 = QPushButton('Test7', self)
       #self.button = QPushButton('Test', self)
       #self.button1.setGeometry(QRect(320, 60, 93, 28))
       self.button1.move(33,150)
       self.button2.move(33,421)
       '''
       self.button3.move(33,330)
       self.button4.move(33,420)
       self.button5.move(33,510)
       self.button6.move(33,600)'''
       self.button7.move(0,693)
       
       
       self.button1.resize(1300, 271)
       
       self.button2.resize(1300, 271)
       '''
       self.button3.resize(1300, 90)
       self.button4.resize(1300, 90)
       self.button5.resize(1300, 90)
       self.button6.resize(1300, 90)'''
       self.button7.resize(1366, 75)
       
       
       #self.button2.setGeometry(QRect(300, 550, 50, 31))
       self.button1.clicked.connect(self.handleButton)
       self.button2.clicked.connect(self.handleButton)
       '''
       self.button3.clicked.connect(self.handleButton)
       self.button4.clicked.connect(self.handleButton)
       self.button5.clicked.connect(self.handleButton)
       self.button6.clicked.connect(self.handleButton)'''
       self.button7.clicked.connect(self.handleButton)
       '''
       layout = QVBoxLayout(self)
       layout.addWidget(self.button1)
       layout.addWidget(self.button2)
       layout.addWidget(self.button3)
       layout.addWidget(self.button4)
       
       pybutton = QPushButton('Click me', self)
       pybutton.resize(100,32)
       pybutton.move(250, 250)        
       pybutton.clicked.connect(self.handleButton)
       '''
       self.show()

    def handleButton(self):
        print ('Hello World')

if __name__ == "__main__":

    app = QApplication(sys.argv)
    oMainwindow = MainWindow()
    sys.exit(app.exec_())
