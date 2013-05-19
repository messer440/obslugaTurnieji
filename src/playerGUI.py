#!/usr/bin/python2.7

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL, SLOT
import sys, string, re
from src.ui import windowPlayers_ui


class PlayersGUI(QtGui.QMainWindow, windowPlayers_ui.Ui_windowPlayers):
	def __init__(self, parent=None, name=None, fl=0):
		super(PlayersGUI, self).__init__(parent)
		self.setupUi(self)
		
		### SIGNALS ### 
		self.actionZakoncz.triggered.connect(self.close)

	def main(self):
		self.show()

	def exit(self):
		sys.exit()

