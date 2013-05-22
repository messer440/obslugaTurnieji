#!/usr/bin/python2.7

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL, SLOT
import sys, string, re
from src.ui import dialogImport_ui
import player, playerGUI
import myZODB, transaction

class ImportGUI(QtGui.QDialog, dialogImport_ui.Ui_dialogImport):
	def __init__(self, parent=None, name=None, fl=0):
		super(ImportGUI, self).__init__(parent)
		self.setupUi(self)
		
		### SIGNALS ### #{{{
		self.buttonAnuluj.connect(self.buttonAnuluj, SIGNAL("clicked()"), self.close)
		self.buttonWybierz.connect(self.buttonWybierz, SIGNAL("clicked()"), self.openFile)#}}}
	
	def openFile(self):#{{{
		importedPlayers = 0
		omittedPlayers = 0
		fname = QtGui.QFileDialog.getOpenFileName(self, 'Importuj plik', '.')
		file = open(fname, 'r')
		try:
			self.playersDB = myZODB.MyZODB('src/db/players.fs')
			self.players = self.playersDB.dbroot
		except:
			QtGui.QMessageBox.warning(self, 'Error bazy danych!',\
					'Nie mozna otworzyc bazy zawodnikow!')
		for line in file:
			try:
				matchPlayer = re.match(r'(.*)\s(.*)\s(M|K)\s([0-9]*)', line)
				newPlayer = player.Player(matchPlayer.group(1,2,3,4))
				if newPlayer.uid not in self.players:
					self.players[newPlayer.uid] = newPlayer
					importedPlayers+=1
				else:
					omittedPlayers+=1
			except:
				QtGui.QMessageBox.warning(self, 'Niepoprawne dane!!',\
						str("Bledne dane\nNie zaimportowano: " + line))
		transaction.commit()
		self.playersDB.close()
		QtGui.QMessageBox.information(self, 'Zakonczono import',\
				str("Poprawnie zaimportowano:\t" + str(importedPlayers) + "\n" + \
				"Powtorzone dane (ominieto):\t" + str(omittedPlayers)))
		self.close()#}}}
