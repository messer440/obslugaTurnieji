# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/windowCourts.ui'
#
# Created: Fri May 31 18:40:21 2013
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_windowCourts(object):
    def setupUi(self, windowCourts):
        windowCourts.setObjectName(_fromUtf8("windowCourts"))
        windowCourts.resize(817, 511)
        self.centralwidget = QtGui.QWidget(windowCourts)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 7, 2, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.inputNrLokalu = QtGui.QTextBrowser(self.centralwidget)
        self.inputNrLokalu.setReadOnly(False)
        self.inputNrLokalu.setObjectName(_fromUtf8("inputNrLokalu"))
        self.gridLayout_2.addWidget(self.inputNrLokalu, 2, 1, 1, 1)
        self.inputUlica = QtGui.QTextBrowser(self.centralwidget)
        self.inputUlica.setReadOnly(False)
        self.inputUlica.setObjectName(_fromUtf8("inputUlica"))
        self.gridLayout_2.addWidget(self.inputUlica, 1, 1, 1, 1)
        self.ulica = QtGui.QLabel(self.centralwidget)
        self.ulica.setAlignment(QtCore.Qt.AlignCenter)
        self.ulica.setObjectName(_fromUtf8("ulica"))
        self.gridLayout_2.addWidget(self.ulica, 1, 0, 1, 1)
        self.miasto = QtGui.QLabel(self.centralwidget)
        self.miasto.setAlignment(QtCore.Qt.AlignCenter)
        self.miasto.setObjectName(_fromUtf8("miasto"))
        self.gridLayout_2.addWidget(self.miasto, 3, 0, 1, 1)
        self.nrLokalu = QtGui.QLabel(self.centralwidget)
        self.nrLokalu.setAlignment(QtCore.Qt.AlignCenter)
        self.nrLokalu.setObjectName(_fromUtf8("nrLokalu"))
        self.gridLayout_2.addWidget(self.nrLokalu, 2, 0, 1, 1)
        self.inputMiasto = QtGui.QTextBrowser(self.centralwidget)
        self.inputMiasto.setLocale(QtCore.QLocale(QtCore.QLocale.Polish, QtCore.QLocale.Poland))
        self.inputMiasto.setReadOnly(False)
        self.inputMiasto.setObjectName(_fromUtf8("inputMiasto"))
        self.gridLayout_2.addWidget(self.inputMiasto, 3, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 6, 2, 1, 1)
        self.inputLiczba = QtGui.QTextBrowser(self.centralwidget)
        self.inputLiczba.setReadOnly(False)
        self.inputLiczba.setObjectName(_fromUtf8("inputLiczba"))
        self.gridLayout.addWidget(self.inputLiczba, 8, 2, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.buttonAdd = QtGui.QPushButton(self.centralwidget)
        self.buttonAdd.setObjectName(_fromUtf8("buttonAdd"))
        self.horizontalLayout.addWidget(self.buttonAdd)
        self.buttonModif = QtGui.QPushButton(self.centralwidget)
        self.buttonModif.setObjectName(_fromUtf8("buttonModif"))
        self.horizontalLayout.addWidget(self.buttonModif)
        self.buttonDel = QtGui.QPushButton(self.centralwidget)
        self.buttonDel.setObjectName(_fromUtf8("buttonDel"))
        self.horizontalLayout.addWidget(self.buttonDel)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 3)
        self.nazwa = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setBold(True)
        font.setWeight(75)
        self.nazwa.setFont(font)
        self.nazwa.setAlignment(QtCore.Qt.AlignCenter)
        self.nazwa.setObjectName(_fromUtf8("nazwa"))
        self.gridLayout.addWidget(self.nazwa, 5, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 9, 0, 1, 1)
        self.adres = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setBold(True)
        font.setWeight(75)
        self.adres.setFont(font)
        self.adres.setAlignment(QtCore.Qt.AlignCenter)
        self.adres.setObjectName(_fromUtf8("adres"))
        self.gridLayout.addWidget(self.adres, 6, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.buttonPrev = QtGui.QPushButton(self.centralwidget)
        self.buttonPrev.setObjectName(_fromUtf8("buttonPrev"))
        self.horizontalLayout_2.addWidget(self.buttonPrev)
        self.buttonNext = QtGui.QPushButton(self.centralwidget)
        self.buttonNext.setObjectName(_fromUtf8("buttonNext"))
        self.horizontalLayout_2.addWidget(self.buttonNext)
        self.gridLayout.addLayout(self.horizontalLayout_2, 10, 0, 1, 3)
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 8, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.liczbaKortow = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Zero Threes"))
        font.setPointSize(12)
        self.liczbaKortow.setFont(font)
        self.liczbaKortow.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.liczbaKortow.setObjectName(_fromUtf8("liczbaKortow"))
        self.horizontalLayout_3.addWidget(self.liczbaKortow)
        self.liczbaKortowVal = QtGui.QTextBrowser(self.centralwidget)
        self.liczbaKortowVal.setObjectName(_fromUtf8("liczbaKortowVal"))
        self.horizontalLayout_3.addWidget(self.liczbaKortowVal)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 3, 3)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setLineWidth(3)
        self.line.setMidLineWidth(3)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 6, 1, 2, 1)
        self.inputNazwa = QtGui.QTextBrowser(self.centralwidget)
        self.inputNazwa.setReadOnly(False)
        self.inputNazwa.setObjectName(_fromUtf8("inputNazwa"))
        self.gridLayout.addWidget(self.inputNazwa, 5, 2, 1, 1)
        windowCourts.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(windowCourts)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        windowCourts.setStatusBar(self.statusbar)

        self.retranslateUi(windowCourts)
        QtCore.QMetaObject.connectSlotsByName(windowCourts)

    def retranslateUi(self, windowCourts):
        windowCourts.setWindowTitle(_translate("windowCourts", "Korty tenisowe", None))
        self.ulica.setText(_translate("windowCourts", "Ulica", None))
        self.miasto.setText(_translate("windowCourts", "Miasto", None))
        self.nrLokalu.setText(_translate("windowCourts", "Nr lokalu", None))
        self.buttonAdd.setText(_translate("windowCourts", "Dodaj", None))
        self.buttonModif.setText(_translate("windowCourts", "Modyfikuj", None))
        self.buttonDel.setText(_translate("windowCourts", "Usuń", None))
        self.nazwa.setText(_translate("windowCourts", "Nazwa", None))
        self.adres.setText(_translate("windowCourts", "Adres", None))
        self.buttonPrev.setText(_translate("windowCourts", "Poprzedni", None))
        self.buttonNext.setText(_translate("windowCourts", "Następny", None))
        self.label.setText(_translate("windowCourts", "Liczba kortów", None))
        self.liczbaKortow.setText(_translate("windowCourts", "Liczba dostępnych adresów", None))

