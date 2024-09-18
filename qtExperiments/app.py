import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette, QColor

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("thingy")

        layout = QVBoxLayout()

        buttonLayout = QHBoxLayout()

        hi_button = QPushButton('hi')
        intro_button = QPushButton('*cool intro*')
        sigma_button = QPushButton('sigma bates male chad gigachad sigma male')

        hi_button.pressed.connect(lambda: self.switch_page_thingy(0))
        intro_button.pressed.connect(lambda: self.switch_page_thingy(1))
        sigma_button.pressed.connect(lambda: self.switch_page_thingy(2))

        buttonLayout.addWidget(hi_button)
        buttonLayout.addWidget(intro_button)
        buttonLayout.addWidget(sigma_button)

        layout.addLayout(buttonLayout)

        self.pagesLayout = QStackedLayout()
        self.pagesLayout.addWidget(QLabel("my name is slim shady"))
        self.pagesLayout.addWidget(QLabel("mustard on the beat ho"))
        self.pagesLayout.addWidget(QLabel("ddrc or whatever the heck"))

        layout.addLayout(self.pagesLayout)

        layout.setSpacing(1)
        layout.setContentsMargins(5, 5, 5, 5)

        dummy_widget = QWidget()
        dummy_widget.setLayout(layout)
        self.setCentralWidget(dummy_widget)

    def switch_page_thingy(self, page: int):
        self.pagesLayout.setCurrentIndex(page)

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

app = QApplication(sys.argv)
app.setStyle('Windows')

window = MainWindow()
window.show()

print("executing app")
app.exec()
