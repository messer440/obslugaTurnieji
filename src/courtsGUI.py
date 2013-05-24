#!/usr/bin/python2.7

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL, SLOT
import sys, string, re, os
from src.ui import windowCourts_ui
import courts
import myZODB, transaction

class CourtsGUI(QtGui.QMainWindow, windowCourts_ui.Ui_windowCourts):
	def __init__ (self, parent=None, name=None, fl=0):
		super(CourtsGUI, self).__init__(parent)
		self.setupUi(self)
		self.courtIdx = 0
		self.dbpath = 'src/db/courts.fs'
		
		self.initForm()

		### SIGNALS ### #{{{
		self.buttonNext.connect(self.buttonNext, SIGNAL("clicked()"), self.nextCourt)
		self.buttonPrev.connect(self.buttonPrev, SIGNAL("clicked()"), self.prevCourt)
		self.buttonDel.connect(self.buttonDel, SIGNAL("clicked()"), self.delCourt)
		self.buttonModif.connect(self.buttonModif, SIGNAL("clicked()"), self.modifCourt)
		self.buttonAdd.connect(self.buttonAdd, SIGNAL("clicked()"), self.addCourt)#}}}

	def initForm(self):#{{{
		self.courtsDB = myZODB.MyZODB(self.dbpath)
		self.courts = self.courtsDB.dbroot
		self.count = len(self.courts.keys())
		self.liczbaKortowVal.setText(str(self.count))
		if ((self.count != 0) and (self.count > self.courtIdx)):
			self.keys = self.courts.keys()
			uid = self.keys[self.courtIdx]
			self.inputNazwa.setText(self.courts[uid].name)
			self.inputUlica.setText(self.courts[uid].street)
			self.inputNrLokalu.setText(self.courts[uid].place)
			self.inputMiasto.setText(self.courts[uid].city)
			self.inputLiczba.setText(self.courts[uid].number)
		self.courtsDB.close()#}}}

	def delCourt(self):#{{{
		try:
			self.courtsDB = myZODB.MyZODB(self.dbpath)
			self.courts = self.courtsDB.dbroot
			self.count = len(self.courts.keys())
			self.keys = self.courts.keys()
			uid = self.keys[self.courtIdx]
			if (self.count > 1):
				del self.courts[uid]
				self.count = len(self.courts.keys())
				transaction.commit()
			else:
				QtGui.QMessageBox.information(self, 'Uwaga!',\
					'Ostatni kort w bazie danych, dokonaj modyfikacji pol!')
			self.courtsDB.close()
		except:
			QtGui.QMessageBox.warning(self, 'Error bazy danych!',\
					'Nie mozna otworzyc bazy kortow!')
		self.initForm(self.courtIdx)#}}}

	def modifCourt(self):#{{{
		try:
			exitVal = self.addCourt()
			if (exitVal == False):
				return
			
			self.courtsDB = myZODB.MyZODB(self.dbpath)
			self.courts = self.courtsDB.dbroot
			self.count = len(self.courts.keys())
			self.keys = self.courts.keys()
			uid = self.keys[self.courtIdx]
			del self.courts[uid]
			transaction.commit()
			self.courtsDB.close()
		except:
			QtGui.QMessageBox.warning(self, 'Error bazy danych!',\
					'Nie mozna otworzyc bazy kortow!')
		self.initForm()#}}}

	def addCourt(self):#{{{
		matchName = re.match(r'^(.*)$', str(self.inputNazwa.toPlainText()))
		matchStreet = re.match(r'^([a-zA-Z]*)$', str(self.inputUlica.toPlainText()))
		matchPlace = re.match(r'^(.*)$', str(self.inputNrLokalu.toPlainText()))
		matchCity = re.match(r'^([a-zA-Z]*)$', str(self.inputMiasto.toPlainText()))
		matchNumber = re.match(r'^([0-9]*)$', str(self.inputLiczba.toPlainText()))

		try:
			self.newCourt = courts.Courts(matchName.group(1), matchStreet.group(1), matchPlace.group(1), matchCity.group(1), matchNumber.group(1))
			try:
				self.courtsDB = myZODB.MyZODB(self.dbpath)
				self.courts = self.courtsDB.dbroot
			except:
				QtGui.QMessageBox.warning(self, 'Error bazy danych!',\
						'Nie mozna otworzyc bazy kortow!')

			if self.newCourt.uid not in self.courts:
				self.courts[self.newCourt.uid] = self.newCourt
				QtGui.QMessageBox.information(self, 'Uaktualnienie bazy',\
							str("Dodano poprawnie kort do bazy"))
			else:
				QtGui.QMessageBox.information(self, 'Kort juz istnieje!!',\
							str("Kort o podanych danych juz istnieje w bazie! "))
			
			transaction.commit()
			self.courtsDB.close()
			self.initForm()
			return True

		except:
			QtGui.QMessageBox.warning(self, 'Niepoprawne dane!',\
						'Niepoprawny format wprowadzonych danych!')
			return False
		#}}}
	
	def nextCourt(self):#{{{
		if (self.courtIdx < self.count-1):
			self.courtIdx += 1
		elif (self.count != 0):
			self.courtIdx = 0
		self.initForm()#}}}

	def prevCourt(self):#{{{
		if (self.courtIdx > 0):
			self.courtIdx -= 1
		elif (self.count != 0):
			self.courtIdx = self.count - 1
		self.initForm()#}}}
