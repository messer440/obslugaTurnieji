# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/dialogImport.ui'
#
# Created: Thu May 23 00:34:09 2013
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

class Ui_dialogImport(object):
    def setupUi(self, dialogImport):
        dialogImport.setObjectName(_fromUtf8("dialogImport"))
        dialogImport.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(dialogImport)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonWybierz = QtGui.QPushButton(dialogImport)
        self.buttonWybierz.setObjectName(_fromUtf8("buttonWybierz"))
        self.gridLayout.addWidget(self.buttonWybierz, 1, 0, 1, 1)
        self.buttonAnuluj = QtGui.QPushButton(dialogImport)
        self.buttonAnuluj.setObjectName(_fromUtf8("buttonAnuluj"))
        self.gridLayout.addWidget(self.buttonAnuluj, 1, 1, 1, 1)
        self.textInfo = QtGui.QTextEdit(dialogImport)
        self.textInfo.setReadOnly(True)
        self.textInfo.setObjectName(_fromUtf8("textInfo"))
        self.gridLayout.addWidget(self.textInfo, 0, 0, 1, 2)

        self.retranslateUi(dialogImport)
        QtCore.QMetaObject.connectSlotsByName(dialogImport)

    def retranslateUi(self, dialogImport):
        dialogImport.setWindowTitle(_translate("dialogImport", "Import graczy", None))
        self.buttonWybierz.setText(_translate("dialogImport", "Wybierz plik..", None))
        self.buttonAnuluj.setText(_translate("dialogImport", "Anuluj", None))
        self.textInfo.setHtml(_translate("dialogImport", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Wybierz plik do zaimportowania</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Poprawny format pliku:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Imie1 Nazwisko2 Płeć Nr_w_rankingu</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Imie2 Nazwisko2 Płeć Nr_w_rankingu</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Imie3 Nazwisko2 Płeć Nr_w_rankingu</p></body></html>", None))

