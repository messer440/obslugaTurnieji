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
	def __init__(self,plyers=None,points=None)
		self.players = players
		self.ended = False
		self.points = points
	def addPlayer(self, player)
		if players.length<2:
			self.players.append(plyer)
	def addResult(self,points)
		self.points=points
		self.ended=True
	def addResult(self,p1,p2)
		addResult([p1,p2])
	
		