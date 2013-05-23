#!/usr/bin/python2.7

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL, SLOT
import sys, string, re
from src.ui import windowTournaments_ui
import importGUI
import player
import myZODB, transaction

class DodajTurniejGUI(QtGui.QMainWindow, windowTournaments_ui.Ui_windowTournaments):
	def __init__(self, parent=None, name=None, fl=0):
		super(DodajTurniejGUI, self).__init__(parent)
		self.setupUi(self)
		self.otherWindow = None

		### SIGNALS ###
		self.buttonAnuluj.connect(self.buttonAnuluj, SIGNAL("clicked()"), self.close)


