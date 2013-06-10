from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL, SLOT
import sys, string, re
#from src.ui import windowPlayers_ui
#import importGUI
import player
import myZODB, transaction
from ui import mecz_ui
from match import Match

class matchGUI(QtGui.QWidget, mecz_ui.Ui_Form):
    def __init__(self,  posx,  posy,levelUp=None,  text_match=None,  parent=None, name=None):
        super(matchGUI, self).__init__(parent)
        self.setupUi(self)
        self.otherWindow = None
        
        #self.initForm(self.playerId)
        if text_match!= None : 
            self.match=text_match
            self.label.setText(self.match.players[0].fName+" "+self.match.players[0].lName)
            self.label_2.setText(self.match.players[1].fName+" "+self.match.players[1].lName)
            self.noOfPlayers=2
        else:
            self.noOfPlayers=0
            self.match=Match()
        
        self.setGeometry(posx, posy, 100, 100)
      #  self.initForm()
        self.levelUp=levelUp
        if levelUp==None:
            self.pushButton.setDisabled(True)
        self.matchStatus=0
		### SIGNALS ### #
        self.pushButton .connect(self.pushButton, SIGNAL("clicked()"), self.submitMatch)
    def addMatch(self,match):
		self.match=match
		self.showPlayers()
    def showPlayers(self):
        self.label.setText(self.match.players[0].fName+" "+self.match.players[0].lName)
        self.label_2.setText(self.match.players[1].fName+" "+self.match.players[1].lName)
        self.pushButton.setDisabled(False)
    def submitMatch(self):
        self.match.points[0]=self.spinBox.value()
        self.match.points[1]=self.spinBox_2.value()
        self.pushButton.setDisabled(True)
        self.submitWinner()
        
    def addPlayerToMatch(self, player):
        self.match.addPlayer(player)
        self.noOfPlayers=self.noOfPlayers+1
        if self.noOfPlayers==2:
           self.showPlayers()
    def submitWinner(self):
		if self.spinBox.value()>self.spinBox_2.value():
			self.levelUp.addPlayerToMatch(self.match.players[0])
		else:
			self.levelUp.addPlayerToMatch(self.match.players[1])
    def addLevelUp(self, m):
        self.levelUp=m
        if self.noOfPlayers==2:
            self.pushButton.setDisabled(False)
