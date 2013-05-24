#!/usr/bin/python2.7
from PyQt4 import QtCore, QtGui
try:
	from ZODB import FileStorage, DB
	import transaction
except:
	QtGui.QMessageBox.warning(self, 'Brakujacy modul',\
			'Do dzialania potrzebny jest modul ZODB do pythona')
import myZODB

class Tournament(Persistent):
	def __init__(self, lName, uid):
		try:
			self.name = lName
			self.uid = uid
			self.playersDB = myZODB.MyZODB('src/db/players/' + str(uid) + '.fs')
			self.players = self.playersDB.dbroot
			self.matchesDB = myZODB.MyZODB('src/db/matches/' + str(uid) + '.fs')
			self.matches = self.matchesDB.dbroot
			self.courts = []
		except:
			QtGui.QMessageBox.warning(self, 'Problem bazy danych',\
				'Nie mozna utworzyc turnieju!')

