# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sonA.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_sonADialog(object):
    def setupUi(self, sonADialog):
        sonADialog.setObjectName("sonADialog")
        sonADialog.resize(280, 392)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        sonADialog.setFont(font)
        self.sonALabel = QtWidgets.QLabel(sonADialog)
        self.sonALabel.setGeometry(QtCore.QRect(70, 10, 141, 31))
        self.sonALabel.setAlignment(QtCore.Qt.AlignCenter)
        self.sonALabel.setObjectName("sonALabel")
        self.sonAList = QtWidgets.QListWidget(sonADialog)
        self.sonAList.setGeometry(QtCore.QRect(0, 43, 280, 350))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.sonAList.setFont(font)
        self.sonAList.setObjectName("sonAList")

        self.retranslateUi(sonADialog)
        QtCore.QMetaObject.connectSlotsByName(sonADialog)

    def retranslateUi(self, sonADialog):
        _translate = QtCore.QCoreApplication.translate
        sonADialog.setWindowTitle(_translate("sonADialog", "Pick a file"))
        self.sonALabel.setText(_translate("sonADialog", "Select a file"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sonADialog = QtWidgets.QDialog()
    ui = Ui_sonADialog()
    ui.setupUi(sonADialog)
    sonADialog.show()
    sys.exit(app.exec_())

