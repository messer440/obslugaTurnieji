import drabinkaGUI
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL, SLOT
import sys, string, re, os
import player
from tournament import Tournament
app = QtGui.QApplication(sys.argv)
mainWindow = drabinkaGUI.drabinkaGUI(16*[player.Player( ['piotr',' waszkiewicz- nowak',' c', 'd','e']  ), player.Player( ['krzysztof', 'cach- kowalski','a2', 'a3', 'a4' ]  )    ], text_parent=Tournament("ala","a" ))
mainWindow.show()
sys.exit(app.exec_())
