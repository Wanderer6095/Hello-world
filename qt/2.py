import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QWidget, QApplication, QLabel)
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Car(QWidget):

    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)
        # Список доступных картинок
        self.cars = ['car1.png', 'car2.png', 'car3.png']
        # Изначальная картинка
        self.current = 'car1.png'
        self.i = 0
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Машинка')

        self.pixmap = QPixmap(self.cars[0])

        self.lbl = QLabel(self)
        self.lbl.setPixmap(self.pixmap)

    # Обработка движения мыши
    def mouseMoveEvent(self, event):
        if event.pos().x() <= 250 and event.pos().y() <= 250:
            self.lbl.move(event.pos().x(), event.pos().y())

    # Обработка нажатия на клавиатуру
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Space:
            self.i = (self.i + 1) % 3
            self.current = self.cars[self.i]
            self.pixmap.load(self.current)
            self.lbl.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Car()
    ex.show()
    sys.exit(app.exec())
