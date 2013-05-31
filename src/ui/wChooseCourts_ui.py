# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/wChooseCourts.ui'
#
# Created: Fri May 31 15:57:09 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_wChooseCourts(object):
    def setupUi(self, wChooseCourts):
        wChooseCourts.setObjectName(_fromUtf8("wChooseCourts"))
        wChooseCourts.resize(800, 600)
        self.centralwidget = QtGui.QWidget(wChooseCourts)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonApply = QtGui.QPushButton(self.centralwidget)
        self.buttonApply.setObjectName(_fromUtf8("buttonApply"))
        self.gridLayout.addWidget(self.buttonApply, 0, 0, 1, 1)
        self.buttonExit = QtGui.QPushButton(self.centralwidget)
        self.buttonExit.setObjectName(_fromUtf8("buttonExit"))
        self.gridLayout.addWidget(self.buttonExit, 0, 1, 1, 1)
        wChooseCourts.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(wChooseCourts)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        wChooseCourts.setStatusBar(self.statusbar)

        self.retranslateUi(wChooseCourts)
        QtCore.QMetaObject.connectSlotsByName(wChooseCourts)

    def retranslateUi(self, wChooseCourts):
        wChooseCourts.setWindowTitle(QtGui.QApplication.translate("wChooseCourts", "Wybór kortów", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonApply.setText(QtGui.QApplication.translate("wChooseCourts", "Zatwierdź", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonExit.setText(QtGui.QApplication.translate("wChooseCourts", "Wyjdź", None, QtGui.QApplication.UnicodeUTF8))

