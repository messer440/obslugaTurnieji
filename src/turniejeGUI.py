#!/usr/bin/python2.7

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL, SLOT
import sys, string, re, os
from src.ui import mainWindow_ui
import playerGUI
import myZODB

class Turnieje(QtGui.QMainWindow, mainWindow_ui.Ui_MainWindow):
	def __init__(self, parent=None, name=None, fl=0):
		super(Turnieje, self).__init__(parent)
		self.setupUi(self)
		
		self.otherWindow = None

		### Connect to zodb databases ###
#		try:
#			self.playersDB = myZODB.MyZODB('src/db/players.fs')
#			self.players = self.playersDB.dbroot
#			self.tournamentsDB = myZODB.MyZODB('src/db/tournaments.fs')
#			self.tournaments = self.tournamentsDB.dbroot
#			self.statusbar.showMessage("Wczytano poprawnie bazy danych")
#		except:
#			self.statusbar.showMessage("Blad bazy danych")
		
		### SIGNALS ###
		self.gracze.connect(self.gracze, SIGNAL('clicked()'), self.openPlayers)
		self.buttonExit.connect(self.buttonExit, SIGNAL('clicked()'), self.close)

	def openPlayers(self):
		self.statusbar.showMessage("Edycja graczy")
		self.otherWindow = playerGUI.PlayersGUI() 
		self.otherWindow.show()
	
	def closeEvent(self, event):
		if (self.otherWindow != None):
			self.otherWindow.close()

	def main(self):
		self.show()

	def exit(self):
		sys.exit()
