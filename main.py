

import sys
import pickle
from PySide2.QtGui import QPalette, QColor
from PySide2.QtCore import QRect, QSize
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
        self.pixelsBg = [None] * 4096
        self.pixels = [None] * 4096

        #Image
        self.image = Image.new("RGBA", (64,64))

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
        self.actionNewBody.triggered.connect(self.newImageHandler)
        self.actionNewCoat.triggered.connect(self.newImageHandler)
        self.actionLoad.triggered.connect(self.loadImageHandler)
        self.actionSave.triggered.connect(self.saveImageHandler)
        self.actionImport.triggered.connect(self.loadTemplateHandler)
        self.actionExport.triggered.connect(self.saveImageHandler)

        self.currentTool = None
        self.last_x, self.last_y = None, None
        self.currentColor = QColor(255,0,0)
        self.canvas = None

    def mousePressEvent(self, QMouseEvent):
        # print mouse position
        print(QMouseEvent.pos())


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
        print('Pipetting', self.currentTool.text())

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
        # file = open(r'skin.mc', 'rb')
        # (colors, colorsBg) = pickle.load(file)
        # # print(colors)
        # file.close()
        for i in range(0, 64):
            for j in range(0, 64):
                self.colorCell(count, (255, 255, 255, 0))
                if (i+j) % 2 == 0:
                    # if (colorsBg[count][0]):
                    #     self.colorCellBg(count, (colorsBg[count][0], colorsBg[count][1], colorsBg[count][2], 150))
                    # else:
                        self.colorCellBg(count, (255, 255, 255, 150))
                else:
                    # if (colorsBg[count][0]):
                    #     self.colorCellBg(count, (colorsBg[count][0], colorsBg[count][1], colorsBg[count][2], 100))
                    # else:
                        self.colorCellBg(count, (185, 185, 185, 150))
                count += 1

    def loadTemplateHandler(self):
        fileName = QFileDialog.getOpenFileName(parent=self, caption="Open Image", dir=".",
                                               filter="Minecraft skin (*.png)")
        self.image = Image.open(fileName[0])
        colorsBg = list(self.image.getdata())
        print('Template Load:', fileName)
        count = 0
        for i in range(0, 64):
            for j in range(0, 64):
                if colorsBg[count][3] == 0 and (i + j) % 2 == 0:
                    self.colorCellBg(count, (255, 255, 255, 150))
                if colorsBg[count][3] == 0 and (i + j) % 2 == 1:
                    self.colorCellBg(count, (185, 185, 185, 150))
                else:
                    self.colorCellBg(count, (colorsBg[count][0], colorsBg[count][1], colorsBg[count][2], 100))
                count += 1

    # def loadProjectHandler(self):
    #     fileName = QFileDialog.getOpenFileName(parent=self, caption="Open MC Paint project", dir=".",
    #                                            filter="MC Paint project (*.mc)")
    #     print(fileName)
    #     file = open(fileName[0], 'rb')
    #     (colors, colorsBg) = pickle.load(file)
    #     file.close()
    #     print('Prject Load:', colors[0][0])
    #     count = 0
    #     for i in range(0, 64):
    #         for j in range(0, 64):
    #             self.colorCell(count, colors[count])
    #             self.colorCellBg(count, colorsBg[count])
    #             count += 1
    #
    # def saveProjectHandler(self):
    #     rgbList = []
    #     rgbListBg = []
    #     for pix in self.pixels:
    #         rgba = pix.palette().color(QPalette.Button).toTuple()
    #         # rgbList.append(rgba)
    #         rgbList.append((0,0,0,0))
    #
    #     for pix in self.pixels:
    #         rgba = pix.palette().color(QPalette.Button).toTuple()
    #         rgbListBg.append(rgba)
    #
    #     filename, filter = QFileDialog.getSaveFileName(parent=self, caption="Select output file", dir=".",
    #                                                    filter="MC Paint project (*.mc)")
    #     if filename:
    #         if '.mc' != filename[-3:]:
    #             filename += ".mc"
    #
    #     afile = open(filename, 'wb')
    #     pickle.dump((rgbList, rgbListBg), afile)
    #     afile.close()
    #     print(filename, filter)

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
            # hexColor = pix.palette().button().color().name()
            rgba = pix.palette().color(QPalette.Button).toTuple()
            print(rgba)
            # rgbList.append(self.hex2rgb(hexColor))
            rgbList.append(rgba)
        self.image.putdata(rgbList)

        filename, filter = QFileDialog.getSaveFileName(parent=self, caption="Select export file", dir=".", filter="Minecraft skin (*.png)")
        if filename:
            if '.png' != filename[-4:]:
                filename += ".png"

        self.image.save(filename)
        print(filename, filter)

    def addCell(self, i):
        pushButton = QPushButton(self.centralwidget)
        pushButton.setObjectName(u"pushButton")
        pushButton.pressed.connect(lambda: self.fill(i, pushButton))
        # pushButton.hover.connect(lambda: self.fill(i, pushButton))
        return pushButton

    def setCanvasSize(self):
        cellSize = 20 * self.zoomState
        cellSpace = 1
        cellCount = 64
        canvasWidth = cellCount * cellSize + cellSpace * cellCount
        canvasHeight = canvasWidth
        self.grid.setGeometry(QRect(0, 0, canvasWidth, canvasHeight))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(canvasWidth, canvasWidth))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(canvasWidth, canvasWidth))

    def initCanvas(self):
        self.setCanvasSize()
        count = 0
        for i in range(0, 64):
            # create row pixels
            for j in range(0, 64):
                self.pixelsBg[count] = self.addCell(count)
                self.pixels[count] = self.addCell(count)
                self.grid.addWidget(self.pixelsBg[count], i + 1, j + 1, 1, 1)
                self.grid.addWidget(self.pixels[count], i + 1, j + 1, 1, 1)
                count += 1

        self.newImageHandler()

    def fill(self, i, button):
        if self.currentTool.text() == 'pen':
            self.colorCell(i, self.currentColor.getRgb())
        elif self.currentTool.text() == 'pipette':
            self.currentColor = self.pixels[i].palette().color(QPalette.Button)
        elif self.currentTool.text() == 'erase':
            self.colorCell(i, (255, 255, 255, 0))

        if button: button.setStyleSheet(self.pixels[i].styleSheet())


    def colorCell(self, pixel=0, color=(255,255,255,0)):
        self.pixels[pixel].setStyleSheet(u"QPushButton\n"
                                         "{\n"
                                         "  border: none;\n"
                                         "  width: 100px;\n"
                                         "  height: 100px;\n"
                                         "	background-color: rgba(%s, %s, %s, %s);\n"
                                         "}" % (color[0],
                                                color[1],
                                                color[2],
                                                color[3]
                                                ))

    def colorCellBg(self, pixel=0, color=(255,255,255,0)):
        self.pixelsBg[pixel].setStyleSheet(u"QPushButton\n"
                                         "{\n"
                                         "  border: none;\n"
                                         "  width: 100px;\n"
                                         "  height: 100px;\n"
                                         "	background-color: rgba(%s, %s, %s, %s);\n"
                                         "}" % (color[0],
                                                color[1],
                                                color[2],
                                                color[3]
                                                ))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    paint = Paint()
    sys.exit(app.exec_())
