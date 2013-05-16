#!/usr/bin/python2.7

class Player:
	def __init__(self, fName, lName, rank):
		self.fName = fName
		self.lName = lName
		self.rank = rank

	def __repr__(self):
		msg="Zawodnik: %s, nr w rankingu %s" % (self.fName + self.lName, self.rank)
		return msg
