#!/usr/bin/python2.7
from PyQt4 import QtCore, QtGui
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
			self.playersDBPath = 'src/db/players/' + str(uid) + '.fs'
			self.matchesDBPath = 'src/db/matches/' + str(uid) + '.fs'
			this.matchId=0;
			#self.playerList = [] # Posortowana wg okreslonego typu lista graczy
		#	self.courts = [] # Lista id kortow na ktorych beda mecze
		except:
			QtGui.QMessageBox.warning(self, 'Problem bazy danych',\
				'Nie mozna utworzyc turnieju!')
	def createMatchList(self,playerlist):
		self.matchesDB=myZODB.MyZODB(self.matchesDBPath)
		self.matches=self.matchesDB.dbroot
		i=0
		while i<len(playerlist)
			addMatch(match(players=[playerlist[playerlist.keys()[i]],playerlist[playerlist.keys()[-(i+1)]]]))
		transaction.commit()
		self.tournamentsDB.close()		
	def addMatch(self,players):
		self.matches[self.matchid] = match.Match(players=players))
		self.matchid=self.matchid+1
		
		
		