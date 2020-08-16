# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtPick.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_pkWindow(object):
    def setupUi(self, pkWindow):
        pkWindow.setObjectName("pkWindow")
        pkWindow.resize(929, 380)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        pkWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(pkWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 561, 331))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.pkGrid = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.pkGrid.setContentsMargins(0, 0, 0, 0)
        self.pkGrid.setObjectName("pkGrid")
        self.pkText = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pkText.setFont(font)
        self.pkText.setObjectName("pkText")
        self.pkGrid.addWidget(self.pkText, 1, 1, 1, 1)
        self.pkSelect = QtWidgets.QListWidget(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.pkSelect.setFont(font)
        self.pkSelect.setObjectName("pkSelect")
        self.pkGrid.addWidget(self.pkSelect, 1, 0, 1, 1)
        self.dataLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.dataLabel.setObjectName("dataLabel")
        self.pkGrid.addWidget(self.dataLabel, 0, 0, 1, 1)
        self.selectLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.selectLabel.setObjectName("selectLabel")
        self.pkGrid.addWidget(self.selectLabel, 0, 1, 1, 1)
        self.pkAccept = QtWidgets.QPushButton(self.centralwidget)
        self.pkAccept.setEnabled(False)
        self.pkAccept.setGeometry(QtCore.QRect(580, 10, 211, 29))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.pkAccept.setFont(font)
        self.pkAccept.setStyleSheet("background-color:rgb(180,255,255);\n"
"border-width:2px;\n"
"border-color:green;\n"
"border-style:solid;")
        self.pkAccept.setObjectName("pkAccept")
        pkWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(pkWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 929, 24))
        self.menubar.setObjectName("menubar")
        pkWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(pkWindow)
        self.statusbar.setObjectName("statusbar")
        pkWindow.setStatusBar(self.statusbar)

        self.retranslateUi(pkWindow)
        QtCore.QMetaObject.connectSlotsByName(pkWindow)

    def retranslateUi(self, pkWindow):
        _translate = QtCore.QCoreApplication.translate
        pkWindow.setWindowTitle(_translate("pkWindow", "Pick File"))
        self.dataLabel.setText(_translate("pkWindow", "Choose files:"))
        self.selectLabel.setText(_translate("pkWindow", "Selections:"))
        self.pkAccept.setText(_translate("pkWindow", "Accept Selections"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pkWindow = QtWidgets.QMainWindow()
    ui = Ui_pkWindow()
    ui.setupUi(pkWindow)
    pkWindow.show()
    sys.exit(app.exec_())

