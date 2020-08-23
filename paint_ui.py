# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'paint_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import application_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(917, 583)
        MainWindow.setStyleSheet(u"background-color: rgb(239, 239, 239);")
        MainWindow.setDocumentMode(True)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_5 = QAction(MainWindow)
        self.action_5.setObjectName(u"action_5")
        self.actionPen = QAction(MainWindow)
        self.actionPen.setObjectName(u"actionPen")
        self.actionPen.setCheckable(True)
        self.actionPen.setChecked(False)
        icon = QIcon()
        icon.addFile(u"ico/pencil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPen.setIcon(icon)
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.actionErase = QAction(MainWindow)
        self.actionErase.setObjectName(u"actionErase")
        self.actionErase.setCheckable(True)
        self.actionErase.setChecked(False)
        icon1 = QIcon()
        icon1.addFile(u"ico/clean.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionErase.setIcon(icon1)
        self.actionBin = QAction(MainWindow)
        self.actionBin.setObjectName(u"actionBin")
        self.actionBin.setCheckable(True)
        self.actionBin.setChecked(False)
        icon2 = QIcon()
        icon2.addFile(u"ico/bin.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionBin.setIcon(icon2)
        self.actionPipette = QAction(MainWindow)
        self.actionPipette.setObjectName(u"actionPipette")
        self.actionPipette.setCheckable(True)
        self.actionPipette.setChecked(False)
        icon3 = QIcon()
        icon3.addFile(u"ico/pipette.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPipette.setIcon(icon3)
        self.actionUndo = QAction(MainWindow)
        self.actionUndo.setObjectName(u"actionUndo")
        self.actionUndo.setCheckable(True)
        self.actionUndo.setChecked(False)
        icon4 = QIcon()
        icon4.addFile(u"ico/undo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionUndo.setIcon(icon4)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionColor = QAction(MainWindow)
        self.actionColor.setObjectName(u"actionColor")
        self.actionColor.setCheckable(True)
        icon5 = QIcon()
        icon5.addFile(u"ico/paint.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionColor.setIcon(icon5)
        self.actionPlus = QAction(MainWindow)
        self.actionPlus.setObjectName(u"actionPlus")
        icon6 = QIcon()
        icon6.addFile(u"ico/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPlus.setIcon(icon6)
        self.actionMinus = QAction(MainWindow)
        self.actionMinus.setObjectName(u"actionMinus")
        icon7 = QIcon()
        icon7.addFile(u"ico/minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionMinus.setIcon(icon7)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.picture = QLabel(self.centralwidget)
        self.picture.setObjectName(u"picture")
        self.picture.setEnabled(False)
        self.picture.setGeometry(QRect(0, 70, 16, 16))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.picture.sizePolicy().hasHeightForWidth())
        self.picture.setSizePolicy(sizePolicy)
        self.picture.setCursor(QCursor(Qt.CrossCursor))
        self.picture.setStyleSheet(u"background-color: rgb(255, 204, 83);")
        self.picture.setScaledContents(False)
        self.picture.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 2, 2))
        self.grid = QGridLayout(self.gridLayoutWidget)
        self.grid.setSpacing(1)
        self.grid.setObjectName(u"grid")
        self.grid.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 917, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_4 = QMenu(self.menubar)
        self.menu_4.setObjectName(u"menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.LeftToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_5)
        self.menu.addSeparator()
        self.menu.addAction(self.actionQuit)
        self.toolBar.addAction(self.actionPen)
        self.toolBar.addAction(self.actionErase)
        self.toolBar.addAction(self.actionPipette)
        self.toolBar.addAction(self.actionUndo)
        self.toolBar.addAction(self.actionBin)
        self.toolBar.addAction(self.actionColor)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPlus)
        self.toolBar.addAction(self.actionMinus)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.action_5.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.actionPen.setText(QCoreApplication.translate("MainWindow", u"Pen", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0430\u0441\u0442\u0438\u043a", None))
        self.actionErase.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0430\u0441\u0442\u0438\u043a", None))
        self.actionBin.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u0441\u0435", None))
        self.actionPipette.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0438\u043f\u0435\u0442\u043a\u0430", None))
        self.actionUndo.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.actionColor.setText(QCoreApplication.translate("MainWindow", u"Color", None))
        self.actionPlus.setText(QCoreApplication.translate("MainWindow", u"Plus", None))
        self.actionMinus.setText(QCoreApplication.translate("MainWindow", u"Minus", None))
        self.picture.setText("")
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0432\u043a\u0430", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

