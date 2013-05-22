#!/usr/bin/python2.7

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL, SLOT
import sys, string, re
from src.ui import windowPlayers_ui
import importGUI
import myZODB, transaction

class PlayersGUI(QtGui.QMainWindow, windowPlayers_ui.Ui_windowPlayers):
	def __init__(self, parent=None, name=None, fl=0):
		super(PlayersGUI, self).__init__(parent)
		self.setupUi(self)
		self.otherWindow = None
		self.playerIdx = 0

		self.initForm(self.playerIdx)

		### SIGNALS ### 
		self.actionZakoncz.triggered.connect(self.close)
		self.actionImportuj.triggered.connect(self.openImport)
		self.buttonZakoncz.connect(self.buttonZakoncz, SIGNAL("clicked()"), self.close)

	def initForm(self, playerIdx):
		self.playersDB = myZODB.MyZODB('src/db/players.fs')
		self.players = self.playersDB.dbroot
		if ((len(self.players.keys()) != 0) and (len(self.players.keys()) >= playerIdx)):
			keys = self.players.keys()
			uid = keys[playerIdx]
			self.inputImie.setText(self.players[uid].fName)
			self.inputNazw.setText(self.players[uid].lName)
			self.inputPlec.setText(self.players[uid].gender)
			self.inputRank.setText(self.players[uid].rank)

	def openImport(self):
		self.otherWindow = importGUI.ImportGUI()
		self.otherWindow.show()

	def closeEvent(self, event):
		if (self.otherWindow != None):
			self.otherWindow.close()
