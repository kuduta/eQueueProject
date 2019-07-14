# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QPrint.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(False)
        MainWindow.resize(1366, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(1366, 768))
        MainWindow.setStyleSheet("QWidget#centralwidget\n"
"{\n"
"background-image: url(:/images/background1366.jpg);\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(200, 170, 961, 71))
        font = QtGui.QFont()
        font.setFamily("supermarket")
        font.setPointSize(40)
        self.pushButton1.setFont(font)
        self.pushButton1.setStyleSheet("QPushButton{\n"
"    color: #FFFFFF;\n"
"    background-color: #3498db;\n"
"      border-color: beige;\n"
"      border-color: #f8f9fa;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(200, 260, 961, 71))
        font = QtGui.QFont()
        font.setFamily("supermarket")
        font.setPointSize(40)
        self.pushButton2.setFont(font)
        self.pushButton2.setStyleSheet("QPushButton{\n"
"    color: #FFFFFF;\n"
"    background-color: #3498db;\n"
"      border-color: beige;\n"
"      border-color: #f8f9fa;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(200, 350, 961, 71))
        font = QtGui.QFont()
        font.setFamily("supermarket")
        font.setPointSize(40)
        self.pushButton3.setFont(font)
        self.pushButton3.setStyleSheet("QPushButton{\n"
"    color: #FFFFFF;\n"
"    background-color: #3498db;\n"
"      border-color: beige;\n"
"      border-color: #f8f9fa;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton3.setObjectName("pushButton3")
        self.pushButton4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton4.setGeometry(QtCore.QRect(200, 440, 961, 71))
        font = QtGui.QFont()
        font.setFamily("supermarket")
        font.setPointSize(40)
        self.pushButton4.setFont(font)
        self.pushButton4.setStyleSheet("QPushButton{\n"
"    color: #FFFFFF;\n"
"    background-color: #3498db;\n"
"      border-color: beige;\n"
"      border-color: #f8f9fa;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton4.setObjectName("pushButton4")
        self.pushButton5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton5.setGeometry(QtCore.QRect(200, 530, 961, 71))
        font = QtGui.QFont()
        font.setFamily("supermarket")
        font.setPointSize(40)
        self.pushButton5.setFont(font)
        self.pushButton5.setStyleSheet("QPushButton{\n"
"    color: #FFFFFF;\n"
"    background-color: #3498db;\n"
"      border-color: beige;\n"
"      border-color: #f8f9fa;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton5.setObjectName("pushButton5")
        self.pushButton5_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton5_2.setGeometry(QtCore.QRect(200, 620, 961, 71))
        font = QtGui.QFont()
        font.setFamily("supermarket")
        font.setPointSize(40)
        self.pushButton5_2.setFont(font)
        self.pushButton5_2.setStyleSheet("QPushButton{\n"
"    color: #FFFFFF;\n"
"    background-color: #3498db;\n"
"      border-color: beige;\n"
"      border-color: #f8f9fa;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton5_2.setObjectName("pushButton5_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RD2 - Queue Print System"))
        self.pushButton1.setText(_translate("MainWindow", "1. ตรวจแบบ / เขียนแบบ  "))
        self.pushButton2.setText(_translate("MainWindow", " 2. รับชำระ                   "))
        self.pushButton3.setText(_translate("MainWindow", "  3. ขอเลขประจำตัวผู้เสียภาษี"))
        self.pushButton4.setText(_translate("MainWindow", "  4. จดทะเบียนภาษีมูลค่าเพิ่ม"))
        self.pushButton5.setText(_translate("MainWindow", "     5. ติดต่องานสำรวจ / เร่งรัดฯ"))
        self.pushButton5_2.setText(_translate("MainWindow", "     6. อื่นๆ                         "))

import background_rc
