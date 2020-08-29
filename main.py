

import sys
from PySide2.QtGui import QPen, QPainter, QPixmap, QPalette, QColor, QCursor
from PySide2.QtCore import QObject, Qt, QTimer, QRect, QSize
from PySide2.QtWidgets import *
from paint_ui import Ui_MainWindow


class Color(QWidget):

    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class Paint(QMainWindow, Ui_MainWindow, QWidget):
    # Конструктор класса
    def __init__(self):
        super().__init__()
        self.canvasOffsetX = 40
        self.canvasOffsetY = 25
        self.zoomState = 1
        self.pixels = [[None] * 64] * 64


        # Создание формы и Ui (наш дизайн)
        self.setupUi(self)
        self.initCanvas()
        # self.loadImage()

        # Показать наше окно
        self.show()

        self.actionQuit.triggered.connect(self.quitHandler)
        self.actionPen.triggered.connect(self.penHandler)
        self.actionErase.triggered.connect(self.eraseHandler)
        self.actionBin.triggered.connect(self.binHandler)
        self.actionPipette.triggered.connect(self.pipetteHandler)
        self.actionUndo.triggered.connect(self.undoHandler)
        self.actionColor.triggered.connect(self.colorHandler)
        self.actionPlus.triggered.connect(self.zoomInHandler)
        self.actionMinus.triggered.connect(self.zoomOutHandler)
        self.currentTool = None
        self.last_x, self.last_y = None, None
        self.currentColor = QColor(255,0,0, 255)
        self.canvas = None



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

    def zoomInHandler(self):
        self.zoomState *= 2
        self.setCanvasSize()
        # self.loadImage()

    def zoomOutHandler(self):
        self.zoomState /= 2
        self.setCanvasSize()
        # self.loadImage()

    # def loadImage(self):
    #     self.canvas = QPixmap("Skinzones.png")
    #     imageSize = self.canvas.size()
    #     imageSize.setWidth(imageSize.width() * self.zoomState)
    #     imageSize.setHeight(imageSize.height() * self.zoomState)
    #     self.picture.setPixmap(self.canvas.scaled(imageSize, Qt.KeepAspectRatioByExpanding))
    #     self.picture.setGeometry(QRect(1, 1, self.width(), self.height()))

    def addCell(self):
        pushButton = QPushButton(self.centralwidget)
        pushButton.setObjectName(u"pushButton")
        # pushButton.setGeometry(QRect(850, 10, 21, 23))

        pushButton.setStyleSheet(u"border: none;\n"
                                 "width:100px;\n"
                                 "height:100px;\n"
                                 "background-color: rgb(255, 255, 255);")

        pushButton.pressed.connect(lambda: self.fill(pushButton))

        return pushButton

    def setCanvasSize(self):
        cellSize = 20 * self.zoomState
        cellSpace = 1
        cellCount = 64
        canvasWidth = cellCount * cellSize + cellSpace * cellCount
        canvasHeight = canvasWidth
        self.gridLayoutWidget.setGeometry(QRect(0, 0, canvasWidth, canvasHeight))

    def initCanvas(self):
        self.setCanvasSize()


        for i in range(0, 64):
            # create row pixels
            for j in range(0, 64):
                self.pixels[i][j] = self.addCell()

                # self.pixels[i][j] = QLabel(self.gridLayoutWidget)
                # self.pixels[i][j].setStyleSheet(u"background-color: rgb(255, 255, 255);")
                # self.pixels[i][j].setMouseTracking(True)
                # self.pixels[i][j].setCursor(QCursor(Qt.PointingHandCursor))

                self.grid.addWidget(self.pixels[i][j], j + 1, i + 1, 1, 1)

        # for i in range(0, 64):
        #     for j in range(0, 64):
        #         self.grid.addWidget(self.pixels[i][j], j+1, i+1, 1, 1)

        # print(self.pixels)

    # def mouseMoveEvent(self, event):
    #     print("On Hover")
    #     print(event)

    def fill(self, button):
        print(self.currentTool.text())
        if self.currentTool.text() == 'pen':
            button.setStyleSheet(u"QPushButton\n"
                                         "{\n"
                                         "  border: none;\n"
                                         "  width: 100px;\n"
                                         "  height: 100px;\n"
                                         "	background-color: %s;\n"
                                         "}" % self.currentColor.name())
        elif self.currentTool.text() == 'erase':
            button.setStyleSheet(u"QPushButton\n"
                                         "{\n"
                                         "  border: none;\n"
                                         "  width: 100px;\n"
                                         "  height: 100px;\n"
                                         "	background-color: rgb(255,255,255);\n"
                                         "}")

    # def mouseMoveEvent(self, e):
    #     if self.last_x is None:  # First event.
    #         self.last_x = e.x() - self.canvasOffsetX
    #         self.last_y = e.y() - self.canvasOffsetY
    #         return  # Ignore the first time.
    #
    #     painter = QPainter(self.picture.pixmap())
    #     p = painter.pen()
    #     p.setWidth(10)
    #     p.setColor(self.currentColor)
    #     painter.setPen(p)
    #     painter.drawLine(
    #         self.last_x,
    #         self.last_y,
    #         e.x() - self.canvasOffsetX,
    #         e.y() - self.canvasOffsetY
    #     )
    #     painter.end()
    #     self.update()
    #
    #     # Update the origin for next time.
    #     self.last_x = e.x() - self.canvasOffsetX
    #     self.last_y = e.y() - self.canvasOffsetY

    # def mouseReleaseEvent(self, e):
    #     self.last_x = None
    #     self.last_y = None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    paint = Paint()
    sys.exit(app.exec_())
