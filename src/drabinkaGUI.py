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
    def __init__(self,text_parent=None, name=None, parent=None):
        super(drabinkaGUI, self).__init__(parent)
        self.setupUi(self)
        potega=text_parent.potega
        self.mecze=[]
        self.w=230
        self.text_parent=text_parent
        
        for i in range(0, potega-2):
            self.poziom=[]
            for j in range (0, 2**i):
                self.poziom.append(matchGUI.matchGUI( (2*j+1)*self.width()/(2**(i+1)  )-self.w/2 , i*150,  parent=self, text_match=self.text_parent.matches[i][j]) )
            self.mecze.append(self.poziom)
        self.poziom=[]
        for k in range(0, 2**(potega-1), 2):
            self.poziom.append(matchGUI.matchGUI( (k+1)*self.width()/(2**(potega-1)  )-self.w/2 , (potega-2)*150, text_match=self.text_parent.matches[potega-2][k],  parent=self) )
        self.mecze.append(self.poziom)
        
        
        
        for p in range(1,len(self.mecze)):
            for m in range(0, len(self.mecze[p])):
                self.mecze[p][m].addLevelUp(self.mecze[p-1][m/2])
        ## SIGNALS ### #
        #self.saveButton .connect(self.saveButton, SIGNAL("clicked()"), self.saveMatches())
    def saveMatches(self):
        self.temp=[]
        for p in range(0,len(self.mecze)):
            for m in range(0, len(self.mecze[p])):
                self.temp.append(self.mecze[p][m])
        self.text_parent.matchesfromdrabinka(self.temp)
