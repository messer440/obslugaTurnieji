#!/usr/bin/python2.7
from PyQt4 import QtCore, QtGui

try:
	from ZODB import FileStorage, DB
	import transaction
except:
	print "Need ZODB and transaction modules!"
	sys.exit()

class MyZODB(object):
	def __init__(self, path):
		try:
			self.storage = FileStorage.FileStorage(path)
			self.db = DB(self.storage)
			self.connection = self.db.open()
			self.dbroot = self.connection.root()
		except:
			QtGui.QMessageBox.warning(self, 'Error bazy danych!',\
					'Nie mozna otworzyc bazy danych!')

	def close(self):
		self.connection.close()
		self.db.close()
		self.storage.close()

	def count(self, path):
		try:
			self.storage = FileStorage.FileStorage(path)
			self.db = DB(self.storage)
			self.connection = self.db.open()
			self.dbroot = self.connection.root()
			self.keys = self.dbroot.keys()
			self.lenght = len(self.keys)
		except:
			QtGui.QMessageBox.warning(self, 'Error bazy danych!',\
					'Nie mozna pobrac wielkosci bazy!')


