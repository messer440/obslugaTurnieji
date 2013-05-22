#!/usr/bin/python2.7

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL, SLOT
import sys, string, re, os
from src import turniejeGUI

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	mainWindow = turniejeGUI.Turnieje()
	mainWindow.show()
	sys.exit(app.exec_())
