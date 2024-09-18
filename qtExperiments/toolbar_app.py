import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('toolbar app')

        basic_label = QLabel('*spy*')
        basic_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.setCentralWidget(basic_label)

        toolbar = QToolBar('main toolbar')
        toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolbar.setIconSize(QSize(252, 129))
        self.addToolBar(toolbar)

        button_action = QAction(QIcon('madgoofy.png'), 'THIS is a BUTTON.', self)
        button_action.setStatusTip('DEAR GOD')
        button_action.triggered.connect(self.on_tool_bar_button_click)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        another_basic_label = QLabel('mentlegen')
        toolbar.addWidget(another_basic_label)

        toolbar.addSeparator()

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(QPushButton('we are not most men'))
        vertical_layout.addWidget(QPushButton('we are mercenaries.'))
        vertical_layout.setSpacing(0)
        vertical_layout.setContentsMargins(0, 0, 0, 0)
        dummy_widget = QWidget()
        dummy_widget.setLayout(vertical_layout)
        toolbar.addWidget(dummy_widget)

        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()

        food_menu = menu.addMenu('&Food')

        food_menu.addAction(button_action)
        food_menu.addSeparator()
        food_menu.addAction(button_action)

    def on_tool_bar_button_click(self, signal):
        print('there\'s more: ', signal)


app = QApplication(sys.argv)
app.setStyle('Windows')
w = MainWindow()
w.show()
app.exec()

