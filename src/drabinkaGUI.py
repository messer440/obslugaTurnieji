from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL, SLOT
import sys, string, re
#from src.ui import windowPlayers_ui
#import importGUI
import player
import myZODB, transaction
import matchGUI
import math
import match
from ui import  drabinka_ui
#    def __init__(self,  posx,  posy,levelUp=None,  text_match=None,  parent=None, name=None):
class drabinkaGUI(QtGui.QMainWindow,  drabinka_ui.Ui_Form):
    def __init__(self,  playerList, parent=None, name=None):
        self.setupUi(self)
        potega=int(math.log(len(playerList),2))
        mecze=[]
        poziom=[]
        poziom.append(matchGUI(10, 10) )
        mecze.appednd(poziom)
        for i in range(1, potega+1):
            poziom=[]
            for j in range (0, 2**i):
                poziom.append(matchGUI(10+i*10, 10+j*10, mecze[i-1][j/2]) )
        for k in range(0, 2**potega):
            mecze[potega+1][k].addPlayer(playerList[k])
    def zrobmecze(self, ilosc=None):
        for m in range(0, ilosc):
            matchGUI(10, 10, text_match=match.Match())
		
		
        
            
        
