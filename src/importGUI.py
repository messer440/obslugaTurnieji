#!/usr/bin/python2.7

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL, SLOT
import sys, string, re
from src.ui import dialogImport_ui


class ImportGUI(QtGui.QDialog, dialogImport_ui.Ui_dialogImport):
	def __init__(self, parent=None, name=None, fl=0):
		super(ImportGUI, self).__init__(parent)
		self.setupUi(self)
		
		### SIGNALS ### 
		self.buttonAnuluj.connect(self.buttonAnuluj, SIGNAL("clicked()"), self.close)
		self.buttonWybierz.connect(self.buttonWybierz, SIGNAL("clicked()"), self.openFile)
	
	def openFile(self):
		fname = QtGui.QFileDialog.getOpenFileName(self, 'Importuj plik', '/home')
		file = open(fname, 'r')

	def main(self):
		self.show()

	def exit(self):
		sys.exit()

