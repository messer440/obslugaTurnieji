#!/usr/bin/python2.7

try:
	from ZODB import FileStorage, DB
	import transaction
except:
	print "Need ZODB and transaction modules!"
	sys.exit()


class MyZODB(object):
	def __init__(self, path):
		self.storage = FileStorage.FileStorage(path)
		self.db = DB(self.storage)
		self.connection = self.db.open()
		self.dbroot = self.connection.root()

	def close(self):
		self.connection.close()
		self.db.close()
		self.storage.close()
