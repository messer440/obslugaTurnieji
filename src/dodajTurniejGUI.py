#!/usr/bin/python2.7

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL, SLOT
import sys, string, re, os, random, copy, transaction
from src.ui import windowTournaments_ui
import importGUI, playerGUI, chooseCourtsGUI
import player, tournament, myZODB

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
			self.child = chooseCourtsGUI.ChooseCourtsGUI(self.courts)
			self.child.show()#}}}

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
			self.uid = str(self.inputSkrotNazwy.toPlainText())
			self.name = str(self.inputNazwa.toPlainText())
			return True
		else:
			QtGui.QMessageBox.information(self, 'Brakuje informacji',\
						str("Prosze podac nazwe turnieju oraz skrocona wersje"))
			return False#}}}

	def saveTournament(self):#{{{
		if (self.checkUID()):
			self.tournamentsDB = myZODB.MyZODB(self.dbpath)
			self.tournaments = self.tournamentsDB.dbroot
			self.tournaments[self.uid] = tournament.Tournament(self.name, self.uid)
			#### Stworzenie turnieju! musi byc przed odwolywaniem do zmiennych! ####
			transaction.commit() 
			self.tournamentsDB.close()

			### Sortowanie graczy ###
			self.playersdb = myZODB.MyZODB(self.tournaments[self.uid].playersDB)
			self.players = self.playersdb.dbroot
			if (self.random == False):
				self.tmp = {}
				for key in self.players.keys():
					self.tmp[key] = self.players[key].rank
				self.tmp = sorted(self.tmp, key=self.tmp.get)
			else:
				self.tmp = copy.copy(self.players.keys())
				random.shuffle(self.tmp)
			import math
			i=0
			while math.ceil(math.log(len(self.tmp)))!=math.log(len(self.tmp)):
				self.tmp[i]=player(BYE,"",0,"",9999)
				i=i+1
			self.playersdb.close()
			self.tournaments[self.uid].playerList = self.tmp
			self.tournaments[self.uid].courts = copy.copy(self.courts)
			#### Sprawdzajace zapis ###
			print "Name: %s, uid: %s " % (self.tournaments[self.uid].name, self.tournaments[self.uid].uid)
			print "Hasze posortowanych graczy: ", self.tournaments[self.uid].playerList
			print "Hasze kortow: ", self.tournaments[self.uid].courts
			self.deleteLater() ## ZAMKNIECIE OKNA#}}}

			
		
			
		
