#!/usr/bin/python2.7
from persistent import Persistent
import md5

class Player(Persistent):
	def __init__(self, data):
		self.fName = data[0]
		self.lName = data[1]
		self.gender = data[2]
		self.rank = data[3]
		self.uid = md5.new(self.fName + self.rank + self.lName + self.gender)

	def __repr__(self):
		msg="Zawodnik: %s, nr w rankingu %s" % (self.fName + " " + self.lName, self.rank)
		return msg
