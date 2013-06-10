from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL, SLOT
import sys, string, re
#from src.ui import windowPlayers_ui
#import importGUI
import player
import myZODB, transaction
import matchGUI
import math
from match import Match
from ui import  drabinka_ui

class drabinkaGUI(QtGui.QMainWindow,  drabinka_ui.Ui_Form):
    def __init__(self,  playerList, text_parent=None, name=None, parent=None):
        super(drabinkaGUI, self).__init__(parent)
        self.setupUi(self)
        potega=int(math.log(len(playerList),2))
        self.mecze=[]
        self.playerList=playerList
        self.w=230
        self.text_parent=text_parent
        for i in range(0, potega-1):
            self.poziom=[]
            for j in range (0, 2**i):
                self.poziom.append(matchGUI.matchGUI( (2*j+1)*self.width()/(2**(i+1)  )-self.w/2 , i*150,  parent=self) )
            self.mecze.append(self.poziom)
        self.poziom=[]
        for k in range(0, 2**(potega-1)):
            self.poziom.append(matchGUI.matchGUI( (2*k+1)*self.width()/(2**(potega)  )-self.w/2 , (potega-1)*150, text_match=Match(self.playerList), parent=self) )
        self.mecze.append(self.poziom)
        for p in range(1,len(self.mecze)):
            for m in range(0, len(self.mecze[p])):
                self.mecze[p][m].addLevelUp(self.mecze[p-1][m/2])
        ## SIGNALS ### #
        self.saveButton .connect(self.saveButton, SIGNAL("clicked()"), self.saveMatches())
    def saveMatches(self):
        self.temp=[]
        for p in range(0,len(self.mecze)):
            for m in range(0, len(self.mecze[p])):
                self.temp.append(self.mecze[p][m])
        self.text_parent.matchesfromdrabinka(self.temp)
        
   # def zrobmecze(self, ilosc=None):
      #  for m in range(0, ilosc):
         #   self.mecze.append(matchGUI.matchGUI(100+100*m, 100+100*m, text_match=match.Match(self.playerList) , parent=self))
            #self.mecze[m].show()
            
        
