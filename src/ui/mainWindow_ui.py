# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/mainWindow.ui'
#
# Created: Thu May 23 11:58:28 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 600))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 0))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setMaximumSize(QtCore.QSize(1920, 1080))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.page)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 111, 558))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.verticalLayoutWidget_2)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.dodajTurniej = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.dodajTurniej.setObjectName(_fromUtf8("dodajTurniej"))
        self.gridLayout_4.addWidget(self.dodajTurniej, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gracze = QtGui.QPushButton(self.centralwidget)
        self.gracze.setObjectName(_fromUtf8("gracze"))
        self.gridLayout_3.addWidget(self.gracze, 0, 0, 1, 1)
        self.korty = QtGui.QPushButton(self.centralwidget)
        self.korty.setObjectName(_fromUtf8("korty"))
        self.gridLayout_3.addWidget(self.korty, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 0, 5, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.buttonExit = QtGui.QPushButton(self.centralwidget)
        self.buttonExit.setObjectName(_fromUtf8("buttonExit"))
        self.gridLayout_2.addWidget(self.buttonExit, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Obsługa Turniejów", None, QtGui.QApplication.UnicodeUTF8))
        self.dodajTurniej.setText(QtGui.QApplication.translate("MainWindow", "Dodaj turniej", None, QtGui.QApplication.UnicodeUTF8))
        self.gracze.setText(QtGui.QApplication.translate("MainWindow", "Gracze", None, QtGui.QApplication.UnicodeUTF8))
        self.korty.setText(QtGui.QApplication.translate("MainWindow", "Korty", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonExit.setText(QtGui.QApplication.translate("MainWindow", "Wyjdź", None, QtGui.QApplication.UnicodeUTF8))

