import drabinkaGUI
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL, SLOT
import sys, string, re, os
import player
app = QtGui.QApplication(sys.argv)
mainWindow = drabinkaGUI.drabinkaGUI(4*[player.Player( ['piotr',' waszkiewicz- nowak',' c', 'd','e']  ), player.Player( ['krzysztof', 'cach- kowalski','a2', 'a3', 'a4' ]  )    ])
mainWindow.show()
#mainWindow.zrobmecze(10)
sys.exit(app.exec_())
