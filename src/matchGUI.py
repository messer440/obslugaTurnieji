from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL, SLOT
import sys, string, re
from src.ui import windowPlayers_ui
import importGUI
import player
import myZODB, transaction


class matchGUI(QtGui.QtForm, mecz_ui.Ui_Form):
    def __init__(self,  posx,  posy,levelUp=None,  text_match=match(),  parent=None, name=None):
        super(matchGUI, self).__init__(parent)
        self.setupUi(self)
        self.otherWindow = None
        self.initForm(self.playerIdx)
        self.label.setText(self, player1.fName+" "+player1.lName)
        self.label2.setText(self, player2.fName+" "+player2.lName)
        self.noOfPlayers=0
        ### SIGNALS ### #{{{
        self.buttonModif.connect(self.pushButton, SIGNAL("clicked()"), self.submitMatch)
        self.setGeometry(posx, posy, 100, 100)
        if levelUp=None:
            self.pushButton.setDisabled(True)
		self.matchStatus=0;
		self.match=text_match
	def addMatch(self,match)
		self.label.setText(self, match.players[0].fName+" "+match.players[0].lName)
		self.label.setText(self, match.players[1].fName+" "+match.players[1].lName)	
    def submitMatch(self):
		match.points[0]=self.spinBox.value()
		match.points[1]=self.spinBox2.value()
		submitWinner()
    def addPlayerToMatch(self, player):
		self.match.addPlayer(player)
	def submitWinner(self)
		if self.spinBox.value()>self.spinBox2.value():
			levelUp.addPlayerToMatch(player[0])
		else:
			levelUp.addPlayerToMatch(player[1])
			
		
		
		

