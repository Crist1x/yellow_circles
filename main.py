import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
import random
from UI import Ui_MainWindow

SCREEN_SIZE = [1000, 770]

class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.draw)
        self.flag = False


    def draw(self):
        self.size = random.randint(10, 100)
        self.color = (255, 255, 0)
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(*self.color))
            qp.setBrush(QColor(*self.color))
            self.x, self.y = random.randint(100, SCREEN_SIZE[0] - 100), random.randint(100, SCREEN_SIZE[1] - 100)
            qp.drawEllipse(self.x, self.y, self.size, self.size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Example()
    form.show()
    sys.exit(app.exec())
