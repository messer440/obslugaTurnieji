import drabinkaGUI
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL, SLOT
import sys, string, re, os
import player
from tournament import Tournament
app = QtGui.QApplication(sys.argv)
t=Tournament("atgsahgajj", "hdgytra")
t.createMatchList()
mainWindow = drabinkaGUI.drabinkaGUI(text_parent=t)

mainWindow.show()
sys.exit(app.exec_())
