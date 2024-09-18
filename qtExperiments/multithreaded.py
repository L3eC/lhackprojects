from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import time

class MainWindow(QMainWindow):


    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.counter = 0

        layout = QVBoxLayout()

        self.l = QLabel("Start")
        b = QPushButton("DANGER!")
        b.pressed.connect(self.oh_no)

        worldkiller = QPushButton("WORLD KILLA!!!")
        worldkiller.pressed.connect(self.world_killa)

        layout.addWidget(self.l)
        layout.addWidget(b)
        layout.addWidget(worldkiller)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)

        self.show()

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

        self.message = 'message (do not change or we all die'

    def world_killa(self):
        print('world dying...')
        self.message = 'message was changed, we are dead now!'

    def oh_no(self):
        for n in range(5):
            QApplication.processEvents()
            time.sleep(1)
            print(self.message)

    def recurring_timer(self):
        self.counter +=1
        self.l.setText("Counter: %d" % self.counter)


app = QApplication([])
window = MainWindow()
app.exec_()
