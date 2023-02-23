# from Calcolator import *
#
# import sys
#
# app = QtWidgets.QApplication(sys.argv)
# Calculator = QtWidgets.QMainWindow()
# ui = Ui_Calculator()
# ui.setupUi(Calculator)
# Calculator.show()
# sys.exit(app.exec_())
#
# form.textEdit.setHtml('123234244')

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType("Calculator.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

def on_click():
    print("Click")
form.textEdit.setHtml.clicked.connect(on_click)

form.textEdit.setHtml('123234244')
app.exec_()