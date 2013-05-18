#!/usr/bin/python2.7

class Player:
    def __init__(self, fName, lName, id, gender):
        self.fName = fName
        self.lName = lName
        self.id = id
        self.gender=gender

	def __repr__(self):
		msg="Zawodnik: %s,o id  %s" % (self.fName + self.lName, self.id)
		return msg;
