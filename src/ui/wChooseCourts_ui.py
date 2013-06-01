# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/wChooseCourts.ui'
#
# Created: Fri May 31 18:40:21 2013
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_wChooseCourts(object):
    def setupUi(self, wChooseCourts):
        wChooseCourts.setObjectName(_fromUtf8("wChooseCourts"))
        wChooseCourts.resize(197, 69)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(wChooseCourts.sizePolicy().hasHeightForWidth())
        wChooseCourts.setSizePolicy(sizePolicy)
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
        wChooseCourts.setWindowTitle(_translate("wChooseCourts", "Wybór kortów", None))
        self.buttonApply.setText(_translate("wChooseCourts", "Zatwierdź", None))
        self.buttonExit.setText(_translate("wChooseCourts", "Wyjdź", None))

