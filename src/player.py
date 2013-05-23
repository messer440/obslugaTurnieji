#!/usr/bin/python2.7
from persistent import Persistent
import md5

class Player(Persistent):
	def __init__(self, data):
		self.fName = data[0]
		self.lName = data[1]
		self.age = data[2]
		self.gender = data[3]
		self.rank = data[4]
		self.uid = str(md5.new(self.fName + self.rank + self.lName + self.age + self.gender).hexdigest())

	def __repr__(self):
		msg="Zawodnik: %s, nr w rankingu %s" % (self.fName + " " + self.lName, self.rank)
		return msg
