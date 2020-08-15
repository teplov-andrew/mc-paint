

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
        print('Coloring', color)

    def loadImage(self):
        picture = QPixmap("Skinzones.png")
        self.picture.setPixmap(picture)
        self.picture.setGeometry(QRect(10, 40, picture.width(), picture.height()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    paint = Paint()
    sys.exit(app.exec_())
