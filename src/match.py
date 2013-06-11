#!/usr/bin/python2.7
from PyQt4 import QtCore, QtGui
try:
	from ZODB import FileStorage, DB
	import transaction
except:
	QtGui.QMessageBox.warning(self, 'Brakujacy modul',\
			'Do dzialania potrzebny jest modul ZODB do pythona')
import myZODB

class Match(object):
    sredniCzasTrwania=60
    def __init__(self,players=None,points=None, dbpath=None, dbplayer1=None, dbplayer2=None):
        if players!=None:
            self.players = players
        else:
            self.players=[]
        self.ended = False
        if dbpath!=None:
            self.a=myZODB.MyZODB('src/db/players/hdgytra1.fs')
            self.p=self.a.dbroot
            self.players.append(self.p[self.p.keys()[dbplayer1] ]      )
            self.players.append(self.p[self.p.keys()[dbplayer2] ]      )
            transaction.commit()
            self.a.close()      
        if points!=None:
            self.points = points
        else:
            self.points=2*[None]
        
    def addPlayer(self, player):
		if len(self.players)<2:
			self.players.append(player)
    def addResult(self,points):
		self.points=points
		self.ended=True
    def addResult(self,p1,p2):
		addResult([p1,p2])
	
		
