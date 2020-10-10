

import sys
from PySide2.QtGui import QPalette, QColor
from PySide2.QtCore import QRect
from PySide2.QtWidgets import *
from paint_ui import Ui_MainWindow
from PIL import Image


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
        self.pixels = [None] * 4096

        #Image
        self.image = Image.new("RGB", (64,64))

        # Создание формы и Ui (наш дизайн)
        self.setupUi(self)
        self.initCanvas()

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
        self.actionNew.triggered.connect(self.newImageHandler)
        self.actionLoad.triggered.connect(self.loadImageHandler)
        self.actionSave.triggered.connect(self.saveImageHandler)

        self.currentTool = None
        self.last_x, self.last_y = None, None
        self.currentColor = QColor(255,0,0)
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
        color = QColorDialog.getColor()
        self.currentColor = color
        print('Coloring', self.currentColor.name())

    def zoomInHandler(self):
        self.zoomState *= 2
        self.setCanvasSize()

    def zoomOutHandler(self):
        self.zoomState /= 2
        self.setCanvasSize()

    def newImageHandler(self):
        count = 0
        for i in range(0, 64):
            for j in range(0, 64):
                if (i+j) % 2 == 0:
                    self.colorCell(count, (255, 255, 255))
                else:
                    self.colorCell(count, (200, 200, 200))
                count += 1

    def loadImageHandler(self):
        fileName = QFileDialog.getOpenFileName(parent=self, caption="Open Image", dir=".", filter="Minecraft skin (*.png)")
        print(fileName)

        self.image = Image.open(fileName[0])
        colors = list(self.image.getdata())
        print('Image Load:', colors[0][0])
        count = 0
        for i in range(0, 64):
            for j in range(0, 64):
                self.colorCell(count, colors[count])
                count += 1

    def saveImageHandler(self):
        rgbList = []

        for pix in self.pixels:
            hexColor = pix.palette().button().color().name()
            rgbList.append(self.hex2rgb(hexColor))

        self.image.putdata(rgbList)

        filename, filter = QFileDialog.getSaveFileName(parent=self, caption="Select output file", dir=".", filter="Minecraft skin (*.png)")
        if filename:
            if '.png' != filename[-4:]:
                filename += ".png"

        self.image.save(filename)
        print(filename, filter)

    def addCell(self, i):
        pushButton = QPushButton(self.centralwidget)
        pushButton.setObjectName(u"pushButton")
        pushButton.pressed.connect(lambda: self.fill(i, pushButton))
        return pushButton

    def setCanvasSize(self):
        cellSize = 20 * self.zoomState
        cellSpace = 0
        cellCount = 64
        canvasWidth = cellCount * cellSize + cellSpace * cellCount
        canvasHeight = canvasWidth
        self.gridLayoutWidget.setGeometry(QRect(0, 0, canvasWidth, canvasHeight))

    def initCanvas(self):
        self.setCanvasSize()
        count = 0
        for i in range(0, 64):
            # create row pixels
            for j in range(0, 64):
                self.pixels[count] = self.addCell(count)
                self.pixels[count].pressed.connect(lambda: self.fill(count, None))
                self.grid.addWidget(self.pixels[count], i + 1, j + 1, 1, 1)
                count += 1
        self.newImageHandler()

    def fill(self, i, button):
        if self.currentTool.text() == 'pen':
            self.colorCell(i, self.currentColor.getRgb())
        elif self.currentTool.text() == 'erase':
            if i % 2 == 0:
                self.colorCell(i, (200, 200, 200))
            else:
                self.colorCell(i, (255, 255, 255))

        if button: button.setStyleSheet(self.pixels[i].styleSheet())

    def hex2rgb(self, hexColor):
        h = hexColor.lstrip('#')
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


    def colorCell(self, pixel=0, color=(255,255,255)):
        self.pixels[pixel].setStyleSheet(u"QPushButton\n"
                                         "{\n"
                                         "  border: none;\n"
                                         "  width: 100px;\n"
                                         "  height: 100px;\n"
                                         "	background-color: rgb(%s, %s, %s);\n"
                                         "}" % (color[0],
                                                color[1],
                                                color[2]
                                                ))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    paint = Paint()
    sys.exit(app.exec_())
