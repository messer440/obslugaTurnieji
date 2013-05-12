#!/usr/bin/python2.7

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL, SLOT
import sys, string, re
import mainWindow_ui

class Turnieje(QtGui.QMainWindow, mainWindow_ui.Ui_MainWindow):
	def __init__(self, parent=None, name=None, fl=0):
		super(Turnieje, self).__init__(parent)

	def main(self):
		self.show()

	def exit(self):
		sys.exit()


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	turnieje = Turnieje()
	turnieje.main()
	app.exec_()
