#!/usr/bin/python2.7
from PyQt4 import QtCore, QtGui
from math import math
try:
	from ZODB import FileStorage, DB
	import transaction
	from persistent import Persistent
except:
	QtGui.QMessageBox.warning(self, 'Brakujacy modul',\
			'Do dzialania potrzebny jest modul ZODB do pythona')
import myZODB

class Tournament(Persistent):
	def __init__(self, lName, uid):
		try:
			self.name = lName
			self.uid = uid

			#### Sciezki do baz danych ####
			self.playersDB = 'src/db/players/' + str(uid) + '.fs'
			self.matchesDB = 'src/db/matches/' + str(uid) + '.fs'

			self.playerList = [] # Posortowana wg okreslonego typu lista graczy
			self.courts = [] # Lista id kortow na ktorych beda mecze	

		except:
			QtGui.QMessageBox.warning(self, 'Problem bazy danych',\
				'Nie mozna utworzyc turnieju!')
		
	