import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("testui.ui", self)
        self.horizontalSlider.valueChanged.connect(self.on_slider_slid)

    def on_slider_slid(self, s):
        print('slider slid... we got a thing! ', s)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
