#!/usr/bin/python2.7

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL, SLOT
import sys, string, re
from src.ui import windowPlayers_ui
import importGUI
import player
import myZODB, transaction

class PlayersGUI(QtGui.QMainWindow, windowPlayers_ui.Ui_windowPlayers):
	def __init__(self, parent=None, name=None, fl=0):
		super(PlayersGUI, self).__init__(parent)
		self.setupUi(self)
		self.otherWindow = None
		self.playerIdx = 0

		self.initForm(self.playerIdx)

		### SIGNALS ### #{{{
		self.actionZakoncz.triggered.connect(self.close)
		self.actionImportuj.triggered.connect(self.openImport)
		self.buttonZakoncz.connect(self.buttonZakoncz, SIGNAL("clicked()"), self.close)
		self.buttonNext.connect(self.buttonNext, SIGNAL("clicked()"), self.nextPlayer)
		self.buttonPrev.connect(self.buttonPrev, SIGNAL("clicked()"), self.prevPlayer)
		self.buttonAdd.connect(self.buttonAdd, SIGNAL("clicked()"), self.addPlayer)#}}}

	def initForm(self, playerIdx):#{{{
		self.playersDB = myZODB.MyZODB('src/db/players.fs')
		self.players = self.playersDB.dbroot
		self.count = len(self.players.keys())
		if ((self.count != 0) and (self.count > self.playerIdx)):
			self.keys = self.players.keys()
			uid = self.keys[self.playerIdx]
			self.inputImie.setText(self.players[uid].fName)
			self.inputNazw.setText(self.players[uid].lName)
			self.inputPlec.setText(self.players[uid].gender)
			self.inputRank.setText(self.players[uid].rank)
		self.playersDB.close()#}}}

	def addPlayer(self):
		matchfName = re.match(r'^([a-zA-Z]*)$', str(self.inputImie.toPlainText()))
		matchlName = re.match(r'^([a-zA-Z]*)$', str(self.inputNazw.toPlainText()))
		matchGender = re.match(r'(M|K){1}$', str(self.inputPlec.toPlainText()))
		matchRank = re.match(r'^([0-9]*)$', str(self.inputRank.toPlainText()))
		
		try:
			self.params = (matchfName.group(1), matchlName.group(1), matchGender.group(1), matchRank.group(1))

			self.newPlayer = player.Player(self.params)
			try:
				self.playersDB = myZODB.MyZODB('src/db/players.fs')
				self.players = self.playersDB.dbroot
			except:
				QtGui.QMessageBox.warning(self, 'Error bazy danych!',\
						'Nie mozna otworzyc bazy zawodnikow!')

			if self.newPlayer.uid not in self.players:
				self.players[self.newPlayer.uid] = self.newPlayer
				QtGui.QMessageBox.information(self, 'Uaktualnienie bazy',\
							str("Dodano poprawnie zawodnika do bazy"))
			else:
				QtGui.QMessageBox.information(self, 'Zawodnik istnieje!!',\
							str("Zawodnik o podanych danych juz istnieje w bazie! "))
			
			transaction.commit()
			self.playersDB.close()
		except:
			QtGui.QMessageBox.warning(self, 'Niepoprawne dane!',\
						'Niepoprawny format wprowadzonych danych!')


		
	def nextPlayer(self):#{{{
		if (self.playerIdx < self.count-1):
			self.playerIdx += 1
		elif (self.count != 0):
			self.playerIdx = 0
		self.initForm(self.playerIdx)#}}}

	def prevPlayer(self):#{{{
		if (self.playerIdx > 0):
			self.playerIdx -= 1
		elif (self.count != 0):
			self.playerIdx = self.count - 1
		self.initForm(self.playerIdx)#}}}

	def openImport(self):#{{{
		self.otherWindow = importGUI.ImportGUI()
		self.otherWindow.show()#}}}

	def closeEvent(self, event):#{{{
		if (self.otherWindow != None):
			self.otherWindow.close()#}}}
