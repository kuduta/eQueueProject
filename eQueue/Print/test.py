from PyQt5 import QtWidgets, uic
#import queue

import sys


app = QtWidgets.QApplication([])

dlgdisplay = uic.loadUi("QPrint.ui")
dlgdisplay.show()


app.exec_()

'''
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = Ui_MainWindow()
    myapp.show()
    sys.exit(app.exec_())
'''
