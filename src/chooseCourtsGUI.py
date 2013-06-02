#!/usr/bin/python2.7

import PySide
from PySide import QtCore, QtGui
from PySide.QtCore import SIGNAL, SLOT
import sys, string, re, os
#from src.ui import self_ui
import player
from src.ui import windowTournaments_ui
import myZODB, transaction

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


class ChooseCourtsGUI(QtGui.QMainWindow):
	def __init__ (self, courts, parent=None): 
		super(ChooseCourtsGUI,self).__init__(parent)
		self.courts = courts
		self.resize(640, 480)
		self.centralwidget = QtGui.QWidget(self)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.gridLayout_main = QtGui.QGridLayout(self.centralwidget)
		self.gridLayout_main.setObjectName(_fromUtf8("gridLayout_main"))
		self.buttonApply = QtGui.QPushButton(self.centralwidget)
		self.buttonApply.setObjectName(_fromUtf8("buttonApply"))
		self.gridLayout_main.addWidget(self.buttonApply, 0, 0, 1, 1)
		self.buttonExit = QtGui.QPushButton(self.centralwidget)
		self.buttonExit.setObjectName(_fromUtf8("buttonExit"))
		self.gridLayout_main.addWidget(self.buttonExit, 0, 1, 1, 1)
		self.setCentralWidget(self.centralwidget)
		self.statusbar = QtGui.QStatusBar(self)
		self.statusbar.setObjectName(_fromUtf8("statusbar"))
		self.setStatusBar(self.statusbar)

		self.scrollArea = QtGui.QScrollArea(self.centralwidget)
		self.scrollArea.setWidgetResizable(True)
		self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
		self.scrollAreaWidgetContents = QtGui.QWidget()
		self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 640, 480))
		self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
		self.gridLayout_main.addWidget(self.scrollArea, 1, 0, 1, 2)
		self.scrollArea.setWidget(self.scrollAreaWidgetContents)

		self.gridLayout = QtGui.QGridLayout(self.scrollAreaWidgetContents)
		self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

		### Dynamic layout ###
		self.dbpath = 'src/db/courts.fs'

		self.courtsDB = myZODB.MyZODB(self.dbpath)
		self.courts = self.courtsDB.dbroot
		self.courtNumb = 0
		self.checkboxes = []
		self.labels = []
		for key in self.courts.keys():
			self.checkboxes.append(QtGui.QCheckBox(self.courts[key].name,self.scrollAreaWidgetContents))
			self.labels.append(QtGui.QLabel(self.courts[key].address,self.scrollAreaWidgetContents))
			self.gridLayout.addWidget(self.checkboxes[self.courtNumb], 1+self.courtNumb, 0, 1, 1)
			self.gridLayout.addWidget(self.labels[self.courtNumb], 1+self.courtNumb, 1, 1, 1)

			self.courtNumb += 1

		for checkBox in self.checkboxes:
			checkBox.show()

		for label in self.labels:
			label.show()

		self.centralwidget.adjustSize()
		self.centralwidget.setLayout(self.gridLayout)
		self.courtsDB.close()

		### SIGNALS ###
		self.buttonExit.connect(self.buttonExit, SIGNAL("clicked()"), self.close)

		self.retranslateUi()
		QtCore.QMetaObject.connectSlotsByName(self)

	def retranslateUi(self):
		self.setWindowTitle(_translate("self", "Wybor kortow", None))
		self.buttonApply.setText(_translate("self", "Zatwierdz", None))
		self.buttonExit.setText(_translate("self", "Wyjdz", None))


