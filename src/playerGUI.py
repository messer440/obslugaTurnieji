#!/usr/bin/python2.7

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL, SLOT
import sys, string, re, os
from src.ui import windowPlayers_ui
import importGUI
import player
import myZODB, transaction

class PlayerGUI(QtGui.QMainWindow, windowPlayers_ui.Ui_windowPlayers):
	def __init__(self, tournamentID, parent=None, name=None, fl=0):
		super(PlayerGUI, self).__init__(parent)
		self.setupUi(self)
		self.tournamentID = tournamentID
		self.otherWindow = None
		self.playerIdx = 0
		self.count = 0
		
		self.dbpath = 'src/db/players/' + str(self.tournamentID) + '.fs'

		self.initForm(self.playerIdx)

		### SIGNALS ### #{{{
		self.actionZakoncz.triggered.connect(self.close)
		self.actionImportuj.triggered.connect(self.openImport)
		self.actionEksportuj.triggered.connect(self.openExport)
		self.actionUsu_baze.triggered.connect(self.deleteDB)
		self.buttonSearch.connect(self.buttonSearch, SIGNAL("clicked()"), self.applySearch)
		self.buttonClear.connect(self.buttonClear, SIGNAL("clicked()"), self.clearSearch)
		self.buttonZakoncz.connect(self.buttonZakoncz, SIGNAL("clicked()"), self.close)
		self.buttonNext.connect(self.buttonNext, SIGNAL("clicked()"), self.nextPlayer)
		self.buttonPrev.connect(self.buttonPrev, SIGNAL("clicked()"), self.prevPlayer)
		self.buttonDelete.connect(self.buttonDelete, SIGNAL("clicked()"), self.delPlayer)
		self.buttonModif.connect(self.buttonModif, SIGNAL("clicked()"), self.modifPlayer)
		self.buttonAdd.connect(self.buttonAdd, SIGNAL("clicked()"), self.addPlayer)#}}}

	def setCount(self):#{{{
		self.searchTerm = str(self.inputSearch.toPlainText()) 
		self.searchList = []
		self.playersDB = myZODB.MyZODB(self.dbpath)
		self.players = self.playersDB.dbroot

		if (self.searchTerm == ''):
			self.count = len(self.players.keys())
			self.searchList = self.players.keys()
		else:
			self.filterIdx = self.comboFilter.currentIndex()
			### Wybieranie odpowiednich wartosci wg filtra ###
			if (self.filterIdx == 0):
				for playerUID in self.players:
					if (self.players[playerUID].lName == self.searchTerm):
						self.searchList.append(playerUID)
			elif (self.filterIdx == 4): 
				for playerUID in self.players:
					if (self.players[playerUID].rank == self.searchTerm):
						self.searchList.append(playerUID)
			elif (self.filterIdx == 1):
				for playerUID in self.players:
					if (self.players[playerUID].fName == self.searchTerm):
						self.searchList.append(playerUID)
			elif (self.filterIdx == 2):
				for playerUID in self.players:
					if (self.players[playerUID].age == self.searchTerm):
						self.searchList.append(playerUID)
			elif (self.filterIdx == 3):
				for playerUID in self.players:
					if (self.players[playerUID].gender == self.searchTerm):
						self.searchList.append(playerUID)
			self.count = len(self.searchList)
		self.playersDB.close()#}}}

	def initForm(self, playerIdx):#{{{
		if os.path.exists(self.dbpath):
			self.setCount()
			self.liczbaGraczyVal.setText(str(self.count))

			if ((self.count != 0) and (self.count > self.playerIdx)):
				self.playersDB = myZODB.MyZODB(self.dbpath)
				self.players = self.playersDB.dbroot
				uid = self.searchList[self.playerIdx]
				self.inputImie.setText(self.players[uid].fName)
				self.inputNazw.setText(self.players[uid].lName)
				self.inputWiek.setText(self.players[uid].age)
				self.inputPlec.setText(self.players[uid].gender)
				self.inputRank.setText(self.players[uid].rank)
				self.playersDB.close()
			else:
				self.setEmptyFields()
			
			self.playersDB.close()

		else:
			self.setEmptyFields()#}}}

	def setEmptyFields(self):#{{{
		self.inputImie.setText('')
		self.inputNazw.setText('')
		self.inputWiek.setText('')
		self.inputPlec.setText('')
		self.inputRank.setText('')#}}}

	def delPlayer(self):#{{{
		try:
			self.playersDB = myZODB.MyZODB(self.dbpath)
			self.players = self.playersDB.dbroot
			self.count = len(self.players.keys())
			self.keys = self.players.keys()
			uid = self.keys[self.playerIdx]
			if (self.count > 1):
				del self.players[uid]
				self.count = len(self.players.keys())
				transaction.commit()
			else:
				self.deleteDB()
			self.playersDB.close()
		except:
			QtGui.QMessageBox.warning(self, 'Error bazy danych!',\
					'Nie mozna otworzyc bazy zawodnikow!')
		self.initForm(self.playerIdx)#}}}

	def modifPlayer(self):#{{{
		try:
			exitVal = self.addPlayer()
			if (exitVal == False):
				return
			
			self.playersDB = myZODB.MyZODB(self.dbpath)
			self.players = self.playersDB.dbroot
			self.count = len(self.players.keys())
			self.keys = self.players.keys()
			uid = self.keys[self.playerIdx]
			del self.players[uid]
			transaction.commit()
			self.playersDB.close()
		except:
			QtGui.QMessageBox.warning(self, 'Error bazy danych!',\
					'Nie mozna otworzyc bazy zawodnikow!')
		self.initForm(self.playerIdx)#}}}

	def addPlayer(self):#{{{
		matchfName = re.match(r'^([a-zA-Z]*)$', str(self.inputImie.toPlainText()))
		matchlName = re.match(r'^([a-zA-Z]*)$', str(self.inputNazw.toPlainText()))
		matchAge = re.match(r'^([0-9]{1,2})$', str(self.inputWiek.toPlainText()))
		matchGender = re.match(r'(M|K){1}$', str(self.inputPlec.toPlainText()))
		matchRank = re.match(r'^([0-9]*)$', str(self.inputRank.toPlainText()))
		
		try:
			self.params = (matchfName.group(1), matchlName.group(1), matchAge.group(1), matchGender.group(1), matchRank.group(1))

			self.newPlayer = player.Player(self.params)
			try:
				self.playersDB = myZODB.MyZODB(self.dbpath)
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
			self.initForm(self.playerIdx)
			return True

		except:
			QtGui.QMessageBox.warning(self, 'Niepoprawne dane!',\
						'Niepoprawny format wprowadzonych danych!')
			return False
		#}}}
	
	def nextPlayer(self):#{{{
		self.setCount()
		if (self.playerIdx < self.count-1):
			self.playerIdx += 1
		elif (self.count != 0):
			self.playerIdx = 0
		self.initForm(self.playerIdx)#}}}

	def prevPlayer(self):#{{{
		self.setCount()
		if (self.playerIdx > 0):
			self.playerIdx -= 1
		elif (self.count != 0):
			self.playerIdx = self.count - 1
		self.initForm(self.playerIdx)#}}}

	def openExport(self):#{{{
		exportedPlayers = 0
		fname = QtGui.QFileDialog.getSaveFileName(self, 'Zapisz jako', '.')
		file = open(fname, 'w')
		try:
			self.playersDB = myZODB.MyZODB(self.dbpath)
			self.players = self.playersDB.dbroot
		except:
			QtGui.QMessageBox.warning(self, 'Error bazy danych!',\
					'Baza zawodnikow jest pusta! Przerywam eksport')
		for player in self.players.values():
			line = "%s %s %s %s %s\n" % (player.fName, player.lName, player.age, player.gender, player.rank)
			file.write(line)
			exportedPlayers += 1
		
		self.playersDB.close()
		QtGui.QMessageBox.information(self, 'Zakonczono eksport',\
				str("Poprawnie wyeksportowano:\t" + str(exportedPlayers)))#}}}

	def openImport(self):#{{{
		self.otherWindow = importGUI.ImportGUI(self.tournamentID)
		self.otherWindow.show()#}}}

	def applySearch(self):#{{{
		self.initForm(self.playerIdx)#}}}

	def closeEvent(self, event):#{{{
		if (self.otherWindow != None):
			self.otherWindow.close()#}}}

	def clearSearch(self):#{{{
		self.inputSearch.setText('')
		self.initForm(self.playerIdx)#}}}

	def deleteDB(self):#{{{
		os.remove(self.dbpath)
		self.initForm(self.playerIdx)
		self.liczbaGraczyVal.setText('0')#}}}
