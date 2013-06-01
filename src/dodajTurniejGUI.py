#!/usr/bin/python2.7

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL, SLOT
import sys, string, re, os, random
from src.ui import windowTournaments_ui
import importGUI, playerGUI, chooseCourtsGUI
import player, tournament
import myZODB, transaction

class DodajTurniejGUI(QtGui.QMainWindow, windowTournaments_ui.Ui_windowTournaments):
	def __init__(self, parent=None, name=None, fl=0):
		super(DodajTurniejGUI, self).__init__(parent)
		self.setupUi(self)
		self.otherWindow = None
		self.dbpath = 'src/db/tournaments.fs'

		### Tournaments var ####{{{
		self.name = None
		self.uid = None
		self.random = True
		self.courts = []
		#}}}

		### SIGNALS ####{{{
		self.buttonAnuluj.connect(self.buttonAnuluj, SIGNAL("clicked()"), self.close)
		self.buttonImport.connect(self.buttonImport, SIGNAL("clicked()"), self.openImportPlayer)
		self.buttonWybierzKort.connect(self.buttonWybierzKort, SIGNAL("clicked()"), self.openChooseCourts)
		self.buttonWybierzZaw.connect(self.buttonWybierzZaw, SIGNAL("clicked()"), self.openWindowPlayer)

		self.buttonZapisz.connect(self.buttonZapisz, SIGNAL("clicked()"), self.saveTournament) 
			
		self.checkLosowe.connect(self.checkLosowe, SIGNAL("stateChanged(int)"), self.setRandom)
		self.checkRanking.connect(self.checkRanking, SIGNAL("stateChanged(int)"), self.setRanking)

		self.inputSkrotNazwy.connect(self.inputSkrotNazwy, SIGNAL("textChanged()"), self.checkUID)
		#}}}

	def setRandom(self,state):#{{{
		if state == 2:
			self.checkRanking.setCheckState(0)
			self.random = True
		if state == 0:
			self.checkRanking.setCheckState(2)
			self.random = False#}}}

	def setRanking(self,state):#{{{
		if state == 2:
			self.checkLosowe.setCheckState(0)
			self.random = False
		if state == 0:
			self.checkLosowe.setCheckState(2)
			self.random = True#}}}
	
	def checkUID(self):#{{{
		self.getExisted()
		if (self.getId()):
			if self.uid not in self.existing:
				return True
			else:
				QtGui.QMessageBox.warning(self, 'Podany turniej istnieje!',\
						'Podany turniej istnieje juz w bazie\nProsze podac inna skrocona nazwe!')
				return False#}}}

	def getExisted(self):#{{{
		self.tournamentsDB = myZODB.MyZODB('src/db/tournaments.fs')
		self.tournaments = self.tournamentsDB.dbroot
		self.existing = self.tournaments.keys()
		self.tournamentsDB.close()#}}}
	
	def openChooseCourts(self):#{{{
		if (self.checkUID()):
			self.otherWindow = chooseCourtsGUI.ChooseCourtsGUI(self.courts)
			self.otherWindow.show()#}}}

	def openWindowPlayer(self):#{{{
		if (self.checkUID()):
			self.otherWindow = playerGUI.PlayerGUI(self.uid)
			self.otherWindow.show()#}}}

	def openImportPlayer(self):#{{{
		if (self.checkUID()):
			self.otherWindow = importGUI.ImportGUI()
			self.otherWindow.show()#}}}

	def getId(self):#{{{
		if (self.inputSkrotNazwy.toPlainText() != '') and (self.inputNazwa.toPlainText() != ''):
			self.uid = self.inputSkrotNazwy.toPlainText()
			self.name = self.inputNazwa.toPlainText()
			return True
		else:
			QtGui.QMessageBox.information(self, 'Brakuje informacji',\
						str("Prosze podac nazwe turnieju oraz skrocona wersje"))
			return False#}}}

	def sortPlayers(self):#{{{
		if (self.random = False):
			self.tmp = {}
			for key in self.tournaments[self.uid].players.keys():
				self.tmp[key] = self.tournaments[self.uid].players[key].rank
			self.tournaments[self.uid].playerList = sorted(self.tmp, key=self.tmp.get)
		else:
			self.tournaments[self.uid].playerList = random.shuffle(self.tournaments[self.uid].players.keys())				#}}}

	def saveTournament(self):#{{{
		if (checkUID()):
			self.tournamentsDB = myZODB.MyZODB(self.dbpath)
			self.tournaments = self.tournamentsDB.dbroot
			self.tournaments[self.uid] = tournament.Tournament(self.name, self.uid)
			sortPlayers()
			self.tournamentsDB.close()#}}}
			
		
