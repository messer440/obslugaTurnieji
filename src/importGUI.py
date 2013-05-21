#!/usr/bin/python2.7

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL, SLOT
import sys, string, re, transaction
from src.ui import dialogImport_ui
import playerGUI
import player, myZODB

class ImportGUI(QtGui.QDialog, dialogImport_ui.Ui_dialogImport):
	def __init__(self, parent=None, name=None, fl=0):
		super(ImportGUI, self).__init__(parent)
		self.setupUi(self)
		
		### SIGNALS ### 
		self.buttonAnuluj.connect(self.buttonAnuluj, SIGNAL("clicked()"), self.close)
		self.buttonWybierz.connect(self.buttonWybierz, SIGNAL("clicked()"), self.openFile)
	
	def openFile(self):
		importedPlayers = 0
		fname = QtGui.QFileDialog.getOpenFileName(self, 'Importuj plik', '.')
		file = open(fname, 'r')
#		self.playersDB = myZODB.MyZODB('db/players.fs')
#		self.players = self.playersDB.dbroot
		for line in file:
			try:
				matchPlayer = re.match(r'(.*)\s(.*)\s(M|K)\s([0-9]*)', line)
				newPlayer = player.Player(matchPlayer.group(1,2,3,4))
				players[str(newPlayer.uid)] = newPlayer
				importedPlayers+=1
			except:
				QtGui.QMessageBox.warning(self, 'Niepoprawne dane!!',\
						str("Bledne dane\nNie zaimportowano: " + line))
				
		QtGui.QMessageBox.information(self, 'Zakonczono import',\
				str("Poprawnie zaimportowano " + str(importedPlayers) + " rekordy!"))
