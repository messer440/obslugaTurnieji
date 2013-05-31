# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/windowTournaments.ui'
#
# Created: Fri May 31 17:32:54 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_windowTournaments(object):
    def setupUi(self, windowTournaments):
        windowTournaments.setObjectName(_fromUtf8("windowTournaments"))
        windowTournaments.resize(800, 381)
        self.centralwidget = QtGui.QWidget(windowTournaments)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonZapisz = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Zero Threes"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.buttonZapisz.setFont(font)
        self.buttonZapisz.setObjectName(_fromUtf8("buttonZapisz"))
        self.gridLayout.addWidget(self.buttonZapisz, 6, 2, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.buttonWybierzZaw = QtGui.QPushButton(self.centralwidget)
        self.buttonWybierzZaw.setObjectName(_fromUtf8("buttonWybierzZaw"))
        self.horizontalLayout.addWidget(self.buttonWybierzZaw)
        self.buttonImport = QtGui.QPushButton(self.centralwidget)
        self.buttonImport.setObjectName(_fromUtf8("buttonImport"))
        self.horizontalLayout.addWidget(self.buttonImport)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 2, 1, 1)
        self.korty = QtGui.QLabel(self.centralwidget)
        self.korty.setAlignment(QtCore.Qt.AlignCenter)
        self.korty.setObjectName(_fromUtf8("korty"))
        self.gridLayout.addWidget(self.korty, 4, 0, 1, 1)
        self.buttonAnuluj = QtGui.QPushButton(self.centralwidget)
        self.buttonAnuluj.setObjectName(_fromUtf8("buttonAnuluj"))
        self.gridLayout.addWidget(self.buttonAnuluj, 6, 0, 1, 1)
        self.buttonWybierzKort = QtGui.QPushButton(self.centralwidget)
        self.buttonWybierzKort.setObjectName(_fromUtf8("buttonWybierzKort"))
        self.gridLayout.addWidget(self.buttonWybierzKort, 4, 2, 1, 1)
        self.rozstawienie = QtGui.QLabel(self.centralwidget)
        self.rozstawienie.setAlignment(QtCore.Qt.AlignCenter)
        self.rozstawienie.setObjectName(_fromUtf8("rozstawienie"))
        self.gridLayout.addWidget(self.rozstawienie, 5, 0, 1, 1)
        self.skrotNazwy = QtGui.QLabel(self.centralwidget)
        self.skrotNazwy.setAlignment(QtCore.Qt.AlignCenter)
        self.skrotNazwy.setObjectName(_fromUtf8("skrotNazwy"))
        self.gridLayout.addWidget(self.skrotNazwy, 2, 0, 1, 1)
        self.nazwaTurnieju = QtGui.QLabel(self.centralwidget)
        self.nazwaTurnieju.setAlignment(QtCore.Qt.AlignCenter)
        self.nazwaTurnieju.setObjectName(_fromUtf8("nazwaTurnieju"))
        self.gridLayout.addWidget(self.nazwaTurnieju, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.checkLosowe = QtGui.QCheckBox(self.centralwidget)
        self.checkLosowe.setChecked(True)
        self.checkLosowe.setObjectName(_fromUtf8("checkLosowe"))
        self.horizontalLayout_2.addWidget(self.checkLosowe)
        self.checkRanking = QtGui.QCheckBox(self.centralwidget)
        self.checkRanking.setObjectName(_fromUtf8("checkRanking"))
        self.horizontalLayout_2.addWidget(self.checkRanking)
        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 2, 1, 1)
        self.inputNazwa = QtGui.QTextBrowser(self.centralwidget)
        self.inputNazwa.setReadOnly(False)
        self.inputNazwa.setObjectName(_fromUtf8("inputNazwa"))
        self.gridLayout.addWidget(self.inputNazwa, 1, 2, 1, 1)
        self.zawodnicy = QtGui.QLabel(self.centralwidget)
        self.zawodnicy.setAlignment(QtCore.Qt.AlignCenter)
        self.zawodnicy.setObjectName(_fromUtf8("zawodnicy"))
        self.gridLayout.addWidget(self.zawodnicy, 3, 0, 1, 1)
        self.inputSkrotNazwy = QtGui.QTextBrowser(self.centralwidget)
        self.inputSkrotNazwy.setReadOnly(False)
        self.inputSkrotNazwy.setObjectName(_fromUtf8("inputSkrotNazwy"))
        self.gridLayout.addWidget(self.inputSkrotNazwy, 2, 2, 1, 1)
        windowTournaments.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(windowTournaments)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        windowTournaments.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(windowTournaments)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        windowTournaments.setStatusBar(self.statusbar)

        self.retranslateUi(windowTournaments)
        QtCore.QMetaObject.connectSlotsByName(windowTournaments)

    def retranslateUi(self, windowTournaments):
        windowTournaments.setWindowTitle(QtGui.QApplication.translate("windowTournaments", "Stwórz turniej", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonZapisz.setText(QtGui.QApplication.translate("windowTournaments", "Zapisz", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonWybierzZaw.setText(QtGui.QApplication.translate("windowTournaments", "Wybierz ...", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonImport.setText(QtGui.QApplication.translate("windowTournaments", "Import z pliku ...", None, QtGui.QApplication.UnicodeUTF8))
        self.korty.setText(QtGui.QApplication.translate("windowTournaments", "Korty", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonAnuluj.setText(QtGui.QApplication.translate("windowTournaments", "Anuluj", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonWybierzKort.setText(QtGui.QApplication.translate("windowTournaments", "Wybierz ...", None, QtGui.QApplication.UnicodeUTF8))
        self.rozstawienie.setText(QtGui.QApplication.translate("windowTournaments", "Rozstawienie", None, QtGui.QApplication.UnicodeUTF8))
        self.skrotNazwy.setText(QtGui.QApplication.translate("windowTournaments", "Skrócona nazwa", None, QtGui.QApplication.UnicodeUTF8))
        self.nazwaTurnieju.setText(QtGui.QApplication.translate("windowTournaments", "Nazwa turnieju", None, QtGui.QApplication.UnicodeUTF8))
        self.checkLosowe.setText(QtGui.QApplication.translate("windowTournaments", "Losowe", None, QtGui.QApplication.UnicodeUTF8))
        self.checkRanking.setText(QtGui.QApplication.translate("windowTournaments", "wg rankingu", None, QtGui.QApplication.UnicodeUTF8))
        self.zawodnicy.setText(QtGui.QApplication.translate("windowTournaments", "Zawodnicy", None, QtGui.QApplication.UnicodeUTF8))

