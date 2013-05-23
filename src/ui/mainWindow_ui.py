# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/mainWindow.ui'
#
# Created: Thu May 23 14:56:37 2013
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
        self.buttonExit = QtGui.QPushButton(self.centralwidget)
        self.buttonExit.setObjectName(_fromUtf8("buttonExit"))
        self.gridLayout_2.addWidget(self.buttonExit, 1, 0, 1, 1)
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.stackedWidget = QtGui.QStackedWidget(self.widget)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 1, 1, 1, 1)
        self.frame = QtGui.QFrame(self.widget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_3 = QtGui.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.dodajTurniej = QtGui.QPushButton(self.frame)
        self.dodajTurniej.setObjectName(_fromUtf8("dodajTurniej"))
        self.gridLayout_3.addWidget(self.dodajTurniej, 0, 0, 1, 1)
        self.korty = QtGui.QPushButton(self.frame)
        self.korty.setObjectName(_fromUtf8("korty"))
        self.gridLayout_3.addWidget(self.korty, 1, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_3.addWidget(self.pushButton, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)
        self.label = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Radio Space"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setFrameShadow(QtGui.QFrame.Raised)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Obsługa Turniejów", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonExit.setText(QtGui.QApplication.translate("MainWindow", "Wyjdź", None, QtGui.QApplication.UnicodeUTF8))
        self.dodajTurniej.setText(QtGui.QApplication.translate("MainWindow", "Dodaj turniej", None, QtGui.QApplication.UnicodeUTF8))
        self.korty.setText(QtGui.QApplication.translate("MainWindow", "Korty", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Raporty", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Manager Turniejów", None, QtGui.QApplication.UnicodeUTF8))

