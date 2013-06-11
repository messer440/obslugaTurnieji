#!/usr/bin/python2.7
from PyQt4 import QtCore, QtGui
from drabinkaGUI import  drabinkaGUI
from match import Match
import math
from player import Player
try:
	from ZODB import FileStorage, DB
	import transaction
	from persistent import Persistent
except:
	QtGui.QMessageBox.warning(self, 'Brakujacy modul',\
			'Do dzialania potrzebny jest modul ZODB do pythona')
import myZODB

class Tournament(Persistent):
    def __init__(self, lName, uid):
        try:
            self.name = lName
            self.uid = uid
            #### Sciezki do baz danych ####
            self.playersDBPath = 'src/db/players/' + str(uid) + '.fs'
            self.matchesDBPath = 'src/db/matches/' + str(uid) + '.fs'
            self.matchId=0;
            self.playersDB=myZODB.MyZODB(self.playersDBPath)
            self.players=self.playersDB.dbroot
            for i in range(0, 8):
                k=Player(["a"+str(i), "b", str(i), "M", str(i)])
                self.players[k.uid]=k
            transaction.commit()
            self.playersDB.close()
            
           # self.playerList = [] # Posortowana wg okreslonego typu lista graczy
            #	self.courts = [] # Lista id kortow na ktorych beda mecze
            self.potega=1
        except:
            QtGui.QMessageBox.warning(self, 'Problem bazy danych',\
            'Nie mozna utworzyc turnieju!')

    def createMatchList(self):
        #self.matchesDB=myZODB.MyZODB(self.matchesDBPath)
        #self.matches=self.matchesDB.dbroot
        self.matches={}
        self.playersDB=myZODB.MyZODB(self.playersDBPath)
        self.players=self.playersDB.dbroot
        self.potega=int(math.log(len(self.players),2))

        for i in range(0, self.potega-2):
            self.poziom={}
            for j in range (0, 2**i):
                self.poziom[j]=Match()
            self.matches[i]=self.poziom
        self.poziom={}
        for k in range(0, 2**(self.potega-1),2 ):
            #self.playersDB=myZODB.MyZODB(self.playersDBPath)
           # self.players=self.playersDB.dbroot
           # a1=self.players.keys()[k] 
          #  a2=self.players.keys()[-(k+1)] 
         #   transaction.commit()
          #  self.playersDB.close()           
          #  self.poziom[k]=Match(dbpath=self.playersDBPath, dbplayer1=k, dbplayer2=k+1 )
            self.poziom[k]=Match(players=[ Player(["Jan", "Kowalski", str(k), "M", str(k)]), Player(["Adam", "Nowak", str(10*k), "M", str(k)]) ]) 
        self.matches[self.potega-2]=self.poziom
        #while i<len(playerlist):
         #   addMatch(match(players=[playerlist[playerlist.keys()[i]],playerlist[playerlist.keys()[-(i+1)]]]))
        transaction.commit()
        #self.matchesDB.close()
        self.playersDB.close()

    def addMatch(self,players):
        self.matches[self.matchid] = match.Match(players=players)
        self.matchid=self.matchid+1

    def showdrabinka(self):
        drabinka=drabinkaGUI(text_parent=self)
        drabinka.show()
        
    def matchesfromdrabinka(self, matchList):
        self.matchesDB=myZODB.MyZODB(self.matchesDBPath)
        self.matches=self.matchesDB.dbroot
        for i in range(0, len(matchList)):
            self.matches[i]=matchList[i]
        transaction.commit()
        self.tournamentsDB.close()
