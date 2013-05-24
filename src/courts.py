#!/usr/bin/python2.7
import md5

class Courts():
	def __init__ (self, name, street, place, city, number):
		self.name = name
		self.street = street
		self.place = place
		self.city = city
		self.number = number
		self.uid = str(md5.new(self.name + self.street + self.place + self.city + self.number).hexdigest())

	def __repr__ (self):
		msg = "Nazwa: %s\nAdres: %s\nLiczba kortow: %s"  % (self.name, self.street + self.place + "\n" + self.city, self.number)
		return msg
