# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/windowPlayers.ui'
#
# Created: Mon Jun  3 10:10:55 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_windowPlayers(object):
    def setupUi(self, windowPlayers):
        windowPlayers.setObjectName(_fromUtf8("windowPlayers"))
        windowPlayers.resize(935, 685)
        self.centralwidget = QtGui.QWidget(windowPlayers)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.buttonZakoncz = QtGui.QPushButton(self.centralwidget)
        self.buttonZakoncz.setObjectName(_fromUtf8("buttonZakoncz"))
        self.gridLayout_2.addWidget(self.buttonZakoncz, 6, 1, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.inputSearch = QtGui.QTextEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputSearch.sizePolicy().hasHeightForWidth())
        self.inputSearch.setSizePolicy(sizePolicy)
        self.inputSearch.setObjectName(_fromUtf8("inputSearch"))
        self.gridLayout_4.addWidget(self.inputSearch, 0, 2, 2, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Sans Mono"))
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_4.addWidget(self.label, 0, 1, 1, 1)
        self.comboFilter = QtGui.QComboBox(self.centralwidget)
        self.comboFilter.setObjectName(_fromUtf8("comboFilter"))
        self.comboFilter.addItem(_fromUtf8(""))
        self.comboFilter.addItem(_fromUtf8(""))
        self.comboFilter.addItem(_fromUtf8(""))
        self.comboFilter.addItem(_fromUtf8(""))
        self.comboFilter.addItem(_fromUtf8(""))
        self.gridLayout_4.addWidget(self.comboFilter, 1, 1, 1, 1)
        self.buttonSearch = QtGui.QPushButton(self.centralwidget)
        self.buttonSearch.setObjectName(_fromUtf8("buttonSearch"))
        self.gridLayout_4.addWidget(self.buttonSearch, 0, 3, 1, 1)
        self.buttonClear = QtGui.QPushButton(self.centralwidget)
        self.buttonClear.setObjectName(_fromUtf8("buttonClear"))
        self.gridLayout_4.addWidget(self.buttonClear, 1, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_4, 0, 0, 1, 2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.inputPlec = QtGui.QTextBrowser(self.centralwidget)
        self.inputPlec.setReadOnly(False)
        self.inputPlec.setObjectName(_fromUtf8("inputPlec"))
        self.gridLayout.addWidget(self.inputPlec, 4, 2, 1, 1)
        self.plec = QtGui.QLabel(self.centralwidget)
        self.plec.setAlignment(QtCore.Qt.AlignCenter)
        self.plec.setObjectName(_fromUtf8("plec"))
        self.gridLayout.addWidget(self.plec, 4, 0, 1, 1)
        self.inputImie = QtGui.QTextBrowser(self.centralwidget)
        self.inputImie.setReadOnly(False)
        self.inputImie.setObjectName(_fromUtf8("inputImie"))
        self.gridLayout.addWidget(self.inputImie, 1, 2, 1, 1)
        self.buttonNext = QtGui.QPushButton(self.centralwidget)
        self.buttonNext.setObjectName(_fromUtf8("buttonNext"))
        self.gridLayout.addWidget(self.buttonNext, 6, 2, 1, 1)
        self.inputNazw = QtGui.QTextBrowser(self.centralwidget)
        self.inputNazw.setReadOnly(False)
        self.inputNazw.setObjectName(_fromUtf8("inputNazw"))
        self.gridLayout.addWidget(self.inputNazw, 2, 2, 1, 1)
        self.rank = QtGui.QLabel(self.centralwidget)
        self.rank.setAlignment(QtCore.Qt.AlignCenter)
        self.rank.setObjectName(_fromUtf8("rank"))
        self.gridLayout.addWidget(self.rank, 5, 0, 1, 1)
        self.inputRank = QtGui.QTextBrowser(self.centralwidget)
        self.inputRank.setReadOnly(False)
        self.inputRank.setObjectName(_fromUtf8("inputRank"))
        self.gridLayout.addWidget(self.inputRank, 5, 2, 1, 1)
        self.nazwisko = QtGui.QLabel(self.centralwidget)
        self.nazwisko.setAlignment(QtCore.Qt.AlignCenter)
        self.nazwisko.setObjectName(_fromUtf8("nazwisko"))
        self.gridLayout.addWidget(self.nazwisko, 2, 0, 1, 1)
        self.buttonPrev = QtGui.QPushButton(self.centralwidget)
        self.buttonPrev.setObjectName(_fromUtf8("buttonPrev"))
        self.gridLayout.addWidget(self.buttonPrev, 6, 0, 1, 1)
        self.imie = QtGui.QLabel(self.centralwidget)
        self.imie.setAlignment(QtCore.Qt.AlignCenter)
        self.imie.setObjectName(_fromUtf8("imie"))
        self.gridLayout.addWidget(self.imie, 1, 0, 1, 1)
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtGui.QFrame.Box)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.liczbaGraczy = QtGui.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Zero Threes"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.liczbaGraczy.setFont(font)
        self.liczbaGraczy.setAlignment(QtCore.Qt.AlignCenter)
        self.liczbaGraczy.setObjectName(_fromUtf8("liczbaGraczy"))
        self.horizontalLayout.addWidget(self.liczbaGraczy)
        self.liczbaGraczyVal = QtGui.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Zero Threes"))
        font.setPointSize(12)
        self.liczbaGraczyVal.setFont(font)
        self.liczbaGraczyVal.setAlignment(QtCore.Qt.AlignCenter)
        self.liczbaGraczyVal.setObjectName(_fromUtf8("liczbaGraczyVal"))
        self.horizontalLayout.addWidget(self.liczbaGraczyVal)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addWidget(self.frame_2, 0, 2, 1, 1)
        self.wiek = QtGui.QLabel(self.centralwidget)
        self.wiek.setAlignment(QtCore.Qt.AlignCenter)
        self.wiek.setObjectName(_fromUtf8("wiek"))
        self.gridLayout.addWidget(self.wiek, 3, 0, 1, 1)
        self.inputWiek = QtGui.QTextBrowser(self.centralwidget)
        self.inputWiek.setReadOnly(False)
        self.inputWiek.setObjectName(_fromUtf8("inputWiek"))
        self.gridLayout.addWidget(self.inputWiek, 3, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 3, 0, 2, 1)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setLineWidth(2)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_3 = QtGui.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.infoAction = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.infoAction.setFont(font)
        self.infoAction.setAlignment(QtCore.Qt.AlignCenter)
        self.infoAction.setObjectName(_fromUtf8("infoAction"))
        self.verticalLayout.addWidget(self.infoAction)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonAdd = QtGui.QPushButton(self.frame)
        self.buttonAdd.setObjectName(_fromUtf8("buttonAdd"))
        self.verticalLayout.addWidget(self.buttonAdd)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.buttonModif = QtGui.QPushButton(self.frame)
        self.buttonModif.setObjectName(_fromUtf8("buttonModif"))
        self.verticalLayout.addWidget(self.buttonModif)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.buttonDelete = QtGui.QPushButton(self.frame)
        self.buttonDelete.setObjectName(_fromUtf8("buttonDelete"))
        self.verticalLayout.addWidget(self.buttonDelete)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 3, 1, 3, 1)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 1, 0, 2, 1)
        windowPlayers.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(windowPlayers)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 935, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuPlik = QtGui.QMenu(self.menubar)
        self.menuPlik.setObjectName(_fromUtf8("menuPlik"))
        self.menuBaza = QtGui.QMenu(self.menubar)
        self.menuBaza.setObjectName(_fromUtf8("menuBaza"))
        windowPlayers.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(windowPlayers)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        windowPlayers.setStatusBar(self.statusbar)
        self.actionImportuj = QtGui.QAction(windowPlayers)
        self.actionImportuj.setObjectName(_fromUtf8("actionImportuj"))
        self.actionEksportuj = QtGui.QAction(windowPlayers)
        self.actionEksportuj.setObjectName(_fromUtf8("actionEksportuj"))
        self.actionZakoncz = QtGui.QAction(windowPlayers)
        self.actionZakoncz.setObjectName(_fromUtf8("actionZakoncz"))
        self.actionUsu_baze = QtGui.QAction(windowPlayers)
        self.actionUsu_baze.setObjectName(_fromUtf8("actionUsu_baze"))
        self.menuPlik.addAction(self.actionImportuj)
        self.menuPlik.addAction(self.actionEksportuj)
        self.menuPlik.addSeparator()
        self.menuPlik.addAction(self.actionZakoncz)
        self.menuPlik.addSeparator()
        self.menuBaza.addAction(self.actionUsu_baze)
        self.menubar.addAction(self.menuPlik.menuAction())
        self.menubar.addAction(self.menuBaza.menuAction())

        self.retranslateUi(windowPlayers)
        QtCore.QMetaObject.connectSlotsByName(windowPlayers)

    def retranslateUi(self, windowPlayers):
        windowPlayers.setWindowTitle(QtGui.QApplication.translate("windowPlayers", "Gracze", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonZakoncz.setText(QtGui.QApplication.translate("windowPlayers", "Zakończ", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("windowPlayers", "Szukaj:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboFilter.setItemText(0, QtGui.QApplication.translate("windowPlayers", "Nazwisko", None, QtGui.QApplication.UnicodeUTF8))
        self.comboFilter.setItemText(1, QtGui.QApplication.translate("windowPlayers", "Imię", None, QtGui.QApplication.UnicodeUTF8))
        self.comboFilter.setItemText(2, QtGui.QApplication.translate("windowPlayers", "Wiek", None, QtGui.QApplication.UnicodeUTF8))
        self.comboFilter.setItemText(3, QtGui.QApplication.translate("windowPlayers", "Płeć", None, QtGui.QApplication.UnicodeUTF8))
        self.comboFilter.setItemText(4, QtGui.QApplication.translate("windowPlayers", "Ranking", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonSearch.setText(QtGui.QApplication.translate("windowPlayers", "Znajdź", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonClear.setText(QtGui.QApplication.translate("windowPlayers", "Wyczyść", None, QtGui.QApplication.UnicodeUTF8))
        self.plec.setText(QtGui.QApplication.translate("windowPlayers", "Płeć", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonNext.setText(QtGui.QApplication.translate("windowPlayers", "Następny", None, QtGui.QApplication.UnicodeUTF8))
        self.rank.setText(QtGui.QApplication.translate("windowPlayers", "Nr w rankingu", None, QtGui.QApplication.UnicodeUTF8))
        self.nazwisko.setText(QtGui.QApplication.translate("windowPlayers", "Nazwisko", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonPrev.setText(QtGui.QApplication.translate("windowPlayers", "Poprzedni", None, QtGui.QApplication.UnicodeUTF8))
        self.imie.setText(QtGui.QApplication.translate("windowPlayers", "Imię", None, QtGui.QApplication.UnicodeUTF8))
        self.liczbaGraczy.setText(QtGui.QApplication.translate("windowPlayers", "Liczba graczy", None, QtGui.QApplication.UnicodeUTF8))
        self.liczbaGraczyVal.setText(QtGui.QApplication.translate("windowPlayers", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.wiek.setText(QtGui.QApplication.translate("windowPlayers", "Wiek", None, QtGui.QApplication.UnicodeUTF8))
        self.infoAction.setText(QtGui.QApplication.translate("windowPlayers", "Działanie na danych z formularza", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonAdd.setText(QtGui.QApplication.translate("windowPlayers", "Dodaj", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonModif.setText(QtGui.QApplication.translate("windowPlayers", "Modyfikuj", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonDelete.setText(QtGui.QApplication.translate("windowPlayers", "Usuń", None, QtGui.QApplication.UnicodeUTF8))
        self.menuPlik.setTitle(QtGui.QApplication.translate("windowPlayers", "Plik", None, QtGui.QApplication.UnicodeUTF8))
        self.menuBaza.setTitle(QtGui.QApplication.translate("windowPlayers", "Baza", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImportuj.setText(QtGui.QApplication.translate("windowPlayers", "Importuj", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEksportuj.setText(QtGui.QApplication.translate("windowPlayers", "Eksportuj", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZakoncz.setText(QtGui.QApplication.translate("windowPlayers", "Zakończ", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUsu_baze.setText(QtGui.QApplication.translate("windowPlayers", "Usuń baze", None, QtGui.QApplication.UnicodeUTF8))

