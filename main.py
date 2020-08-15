

import sys
from PySide2.QtGui import QPen, QPainter, QPixmap
from PySide2.QtCore import QObject, Qt, QTimer, QRect
from PySide2.QtWidgets import *
from paint_ui import Ui_MainWindow


class Paint(QMainWindow, Ui_MainWindow, QWidget):
    # Конструктор класса
    def __init__(self):
        super().__init__()
        # Создание формы и Ui (наш дизайн)
        self.setupUi(self)
        self.loadImage()
        self.drawSomething()
        # Показать наше окно
        self.show()
        self.actionQuit.triggered.connect(self.quitHandler)
        self.actionPen.triggered.connect(self.penHandler)
        self.actionErase.triggered.connect(self.eraseHandler)
        self.actionBin.triggered.connect(self.binHandler)
        self.actionPipette.triggered.connect(self.pipetteHandler)
        self.actionUndo.triggered.connect(self.undoHandler)
        self.actionColor.triggered.connect(self.colorHandler)
        self.currentTool = None
        self.last_x, self.last_y = None, None
        self.currentColor = None

    def uncheckedAll(self):
        self.actionPen.setChecked(False)
        self.actionErase.setChecked(False)
        self.actionPipette.setChecked(False)
        self.actionUndo.setChecked(False)
        self.actionBin.setChecked(False)
        self.actionColor.setChecked(False)

    def quitHandler(self):
        self.close()

    def penHandler(self):
        self.uncheckedAll()
        self.actionPen.setChecked(True)
        self.currentTool = self.actionPen
        print('Penning')

    def eraseHandler(self):
        self.uncheckedAll()
        self.actionErase.setChecked(True)
        self.currentTool = self.actionErase
        print('Erasing')

    def binHandler(self):
        self.uncheckedAll()
        self.actionBin.setChecked(True)
        self.currentTool = self.actionBin
        print('Binning')

    def pipetteHandler(self):
        self.uncheckedAll()
        self.actionPipette.setChecked(True)
        self.currentTool = self.actionPipette
        print('Pipetting')

    def undoHandler(self):
        self.uncheckedAll()
        self.actionUndo.setChecked(True)
        self.currentTool = self.actionUndo
        print('Undoing')


    def colorHandler(self):
        self.uncheckedAll()
        self.actionColor.setChecked(True)
        self.currentTool = self.actionColor
        color = QColorDialog.getColor()
        # self.textEdit.setTextColor(color)
        self.currentColor = color
        print('Coloring', color)

    def loadImage(self):
        picture = QPixmap("Skinzones.png")
        self.picture.setPixmap(picture)
        self.picture.setGeometry(QRect(10, 40, picture.width(), picture.height()))

    def drawSomething(self):
        painter = QPainter(self.picture.pixmap())
        painter.drawLine(10, 10, 300, 200)
        painter.end()

    # def mouseMoveEvent(self, e):
    #     painter = QPainter(self.picture.pixmap())
    #     painter.drawPoint(e.x(), e.y())
    #     painter.end()
    #     self.update()

    def mouseMoveEvent(self, e):
        if self.last_x is None:  # First event.
            self.last_x = e.x()
            self.last_y = e.y()
            return  # Ignore the first time.

        painter = QPainter(self.picture.pixmap())
        p = painter.pen()
        p.setWidth(10)
        # p.setColor('#ff0000')
        p.setColor(self.currentColor)
        painter.setPen(p)
        painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
        painter.end()
        self.update()

        # Update the origin for next time.
        self.last_x = e.x()
        self.last_y = e.y()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    paint = Paint()
    sys.exit(app.exec_())
