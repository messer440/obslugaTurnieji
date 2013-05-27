from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL, SLOT
import sys, string, re
from src.ui import windowPlayers_ui
import importGUI
import player
import myZODB, transaction


class matchGUI(QtGui.QtForm, mecz_ui.Ui_Form):
    def __init__(self,  posx,  posy,levelUp=None,  text_match=None,  parent=None, name=None):
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
    def submitMatch(self):
        if self.spinBox.value()>self.spinBox2.value():
            levelUp.addPlayer(this. player1)
        else:
            levelUp.addPlayer(this. player2)
    def addPlayer(self, player):
        if self.noOfPlayers==0:
            self.label.setText(self, player.fName+" "+player.lName)
            self.player1=player
        elif  self.noOfPlayers==1:
            self.label2.setText(self, player.fName+" "+player.lName)
            self.player2=player
        self.noOfPlayers=self.noOfPlayers+1
