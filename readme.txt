convert qt: pyside2-uic paint_ui.ui -o paint_ui.py
convert icons: pyside2-rcc icons.qrc -o icons_rc.py
run: python main.py
compile: pyinstaller -w main.py ## https://www.learnpyqt.com/courses/packaging-and-distribution/packaging-pyqt5-pyside2-applications-windows-pyinstaller/



  self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 16, 16))
        self.grid = QGridLayout(self.gridLayoutWidget)




















