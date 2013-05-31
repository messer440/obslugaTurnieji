#!/usr/bin/python2.7

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL, SLOT
import sys, string, re, os
from src.ui import wChooseCourts_ui
import player
import myZODB, transaction

class ChooseCourtsGUI(QtGui.QMainWindow, wChooseCourts_ui.Ui_wChooseCourts):
	def __init__(self, courtsList, parent=None, name=None, fl=0):
		super(ChooseCourtsGUI, self).__init__(parent)
		self.setupUi(self)
		self.dbpath = 'src/db/courts.fs'
		self.courtsList = courtsList
		self.otherWindow = None

		### Dynamic layout ###
		self.centralwidget = QtGui.QWidget(self)
		self.centralwidget.adjustSize() #resize(800,600)
		self.gridLayout = QtGui.QGridLayout(self.centralwidget)

		self.courtsDB = myZODB.MyZODB(self.dbpath)
		self.courts = self.courtsDB.dbroot
		self.courtNumb = 0
		self.checkboxes = []
		for key in self.courts.keys():
			self.checkboxes.append(QtGui.QCheckBox(self.courts[key].name, self))
			self.gridLayout.addWidget(self.checkboxes[self.courtNumb], self.courtNumb, self.courtNumb % 2, 1, 1)
			self.courtNumb += 1

		for checkBox in self.checkboxes:
			checkBox.show()

		self.courtsDB.close()


