# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/wChooseCourts.ui'
#
# Created: Mon Jun  3 10:10:55 2013
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
        wChooseCourts.resize(398, 386)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(wChooseCourts.sizePolicy().hasHeightForWidth())
        wChooseCourts.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(wChooseCourts)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonExit = QtGui.QPushButton(self.centralwidget)
        self.buttonExit.setObjectName(_fromUtf8("buttonExit"))
        self.gridLayout.addWidget(self.buttonExit, 2, 1, 1, 1)
        self.buttonApply = QtGui.QPushButton(self.centralwidget)
        self.buttonApply.setObjectName(_fromUtf8("buttonApply"))
        self.gridLayout.addWidget(self.buttonApply, 2, 0, 1, 1)
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 376, 308))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 2, 1, 1, 1)
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 1, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 2)
        wChooseCourts.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(wChooseCourts)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        wChooseCourts.setStatusBar(self.statusbar)

        self.retranslateUi(wChooseCourts)
        QtCore.QMetaObject.connectSlotsByName(wChooseCourts)

    def retranslateUi(self, wChooseCourts):
        wChooseCourts.setWindowTitle(QtGui.QApplication.translate("wChooseCourts", "Wybór kortów", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonExit.setText(QtGui.QApplication.translate("wChooseCourts", "Wyjdź", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonApply.setText(QtGui.QApplication.translate("wChooseCourts", "Zatwierdź", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("wChooseCourts", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("wChooseCourts", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

