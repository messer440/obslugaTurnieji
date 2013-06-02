#!/usr/bin/python2.7

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL, SLOT
import sys, string, re, os
from src.ui import mainWindow_ui
import playerGUI, dodajTurniejGUI, courtsGUI
import myZODB

class Turnieje(QtGui.QMainWindow, mainWindow_ui.Ui_MainWindow):
	def __init__(self, parent=None, name=None, fl=0):
		super(Turnieje, self).__init__(parent)
		self.setupUi(self)
		self.programTree()
		self.otherWindow = None

		### SIGNALS ####{{{
		self.korty.connect(self.korty, SIGNAL('clicked()'), self.openCourts)
		self.dodajTurniej.connect(self.dodajTurniej, SIGNAL('clicked()'), self.openTournaments)
		self.buttonExit.connect(self.buttonExit, SIGNAL('clicked()'), self.close)#}}}

	def openCourts(self):#{{{
		self.statusbar.showMessage("Edycja kortow tenisowych")
		self.otherWindow = courtsGUI.CourtsGUI()
		self.otherWindow.show()#}}}

	def openTournaments(self):#{{{
		self.statusbar.showMessage("Dodaj turniej")
		self.otherWindow = dodajTurniejGUI.DodajTurniejGUI() 
		self.otherWindow.show()#}}}

	def programTree(self):#{{{
		self.dirs = ['src/db', 'src/db/players', 'src/db/matches']
		for dir in self.dirs:
			if not os.path.exists(dir):
				os.makedirs(dir)#}}}
			
#	def openPlayers(self):#{{{
#		self.statusbar.showMessage("Edycja graczy")
#		self.otherWindow = playerGUI.PlayersGUI() 
#		self.otherWindow.show()#}}}
	
	def closeEvent(self, event):#{{{
		if (self.otherWindow != None):
			self.otherWindow.close()#}}}

	def main(self):#{{{
		self.show()#}}}

	def exit(self):#{{{
		sys.exit()#}}}
