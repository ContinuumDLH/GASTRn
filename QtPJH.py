# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtPJH.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1338, 999)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(6, 0))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1280, 960))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(1280, 960))
        self.tabWidget.setMaximumSize(QtCore.QSize(1280, 960))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setToolTipDuration(-1)
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.genLabel = QtWidgets.QLabel(self.tab1)
        self.genLabel.setGeometry(QtCore.QRect(20, 10, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.genLabel.setFont(font)
        self.genLabel.setObjectName("genLabel")
        self.rawLabel = QtWidgets.QLabel(self.tab1)
        self.rawLabel.setGeometry(QtCore.QRect(20, 70, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.rawLabel.setFont(font)
        self.rawLabel.setObjectName("rawLabel")
        self.genTextEdit = QtWidgets.QPlainTextEdit(self.tab1)
        self.genTextEdit.setGeometry(QtCore.QRect(21, 100, 1241, 211))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(10)
        self.genTextEdit.setFont(font)
        self.genTextEdit.setReadOnly(True)
        self.genTextEdit.setObjectName("genTextEdit")
        self.rawXLabel = QtWidgets.QLabel(self.tab1)
        self.rawXLabel.setGeometry(QtCore.QRect(20, 330, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.rawXLabel.setFont(font)
        self.rawXLabel.setObjectName("rawXLabel")
        self.rawPLabel = QtWidgets.QLabel(self.tab1)
        self.rawPLabel.setGeometry(QtCore.QRect(20, 590, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.rawPLabel.setFont(font)
        self.rawPLabel.setObjectName("rawPLabel")
        self.transTextEdit = QtWidgets.QPlainTextEdit(self.tab1)
        self.transTextEdit.setGeometry(QtCore.QRect(21, 360, 1241, 211))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(10)
        self.transTextEdit.setFont(font)
        self.transTextEdit.setReadOnly(True)
        self.transTextEdit.setObjectName("transTextEdit")
        self.fastaLabel = QtWidgets.QLabel(self.tab1)
        self.fastaLabel.setGeometry(QtCore.QRect(110, 40, 881, 31))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(12)
        self.fastaLabel.setFont(font)
        self.fastaLabel.setText("")
        self.fastaLabel.setObjectName("fastaLabel")
        self.phageLabel = QtWidgets.QLabel(self.tab1)
        self.phageLabel.setGeometry(QtCore.QRect(90, 30, 1141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.phageLabel.setFont(font)
        self.phageLabel.setTextFormat(QtCore.Qt.PlainText)
        self.phageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.phageLabel.setObjectName("phageLabel")
        self.protTextEdit = QtWidgets.QTextEdit(self.tab1)
        self.protTextEdit.setGeometry(QtCore.QRect(21, 620, 1241, 241))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(10)
        self.protTextEdit.setFont(font)
        self.protTextEdit.setReadOnly(True)
        self.protTextEdit.setObjectName("protTextEdit")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab1)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 870, 1241, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.tab1Layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.tab1Layout.setContentsMargins(0, 0, 0, 0)
        self.tab1Layout.setObjectName("tab1Layout")
        self.lookupButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.lookupButton.setFont(font)
        self.lookupButton.setStyleSheet("background-color:rgb(180,255,255);\n"
"")
        self.lookupButton.setObjectName("lookupButton")
        self.tab1Layout.addWidget(self.lookupButton)
        self.removeButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.removeButton.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.removeButton.setFont(font)
        self.removeButton.setStyleSheet("background-color:rgb(180, 255, 255);")
        self.removeButton.setObjectName("removeButton")
        self.tab1Layout.addWidget(self.removeButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.tab1Layout.addItem(spacerItem)
        self.linearCheckBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.linearCheckBox.setFont(font)
        self.linearCheckBox.setObjectName("linearCheckBox")
        self.tab1Layout.addWidget(self.linearCheckBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.tab1Layout.addItem(spacerItem1)
        self.gctLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gctLabel.sizePolicy().hasHeightForWidth())
        self.gctLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.gctLabel.setFont(font)
        self.gctLabel.setObjectName("gctLabel")
        self.tab1Layout.addWidget(self.gctLabel)
        self.gcLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.gcLabel.setFont(font)
        self.gcLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.gcLabel.setText("")
        self.gcLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.gcLabel.setObjectName("gcLabel")
        self.tab1Layout.addWidget(self.gcLabel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.tab1Layout.addItem(spacerItem2)
        self.atgctLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.atgctLabel.sizePolicy().hasHeightForWidth())
        self.atgctLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.atgctLabel.setFont(font)
        self.atgctLabel.setObjectName("atgctLabel")
        self.tab1Layout.addWidget(self.atgctLabel)
        self.atgcLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.atgcLabel.setFont(font)
        self.atgcLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.atgcLabel.setText("")
        self.atgcLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.atgcLabel.setObjectName("atgcLabel")
        self.tab1Layout.addWidget(self.atgcLabel)
        self.exitButton_1 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.exitButton_1.setFont(font)
        self.exitButton_1.setStyleSheet("background-color:rgb(255, 147, 137);\n"
"border-color:red;\n"
"border-style:solid;\n"
"border-width:2px;")
        self.exitButton_1.setObjectName("exitButton_1")
        self.tab1Layout.addWidget(self.exitButton_1)
        self.tabWidget.addTab(self.tab1, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.genLabel_2 = QtWidgets.QLabel(self.tab_5)
        self.genLabel_2.setGeometry(QtCore.QRect(20, 10, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.genLabel_2.setFont(font)
        self.genLabel_2.setObjectName("genLabel_2")
        self.phageLabel_2 = QtWidgets.QLabel(self.tab_5)
        self.phageLabel_2.setGeometry(QtCore.QRect(90, 30, 1141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.phageLabel_2.setFont(font)
        self.phageLabel_2.setTextFormat(QtCore.Qt.PlainText)
        self.phageLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.phageLabel_2.setObjectName("phageLabel_2")
        self.nwindow_results = QtWidgets.QPlainTextEdit(self.tab_5)
        self.nwindow_results.setGeometry(QtCore.QRect(20, 240, 711, 631))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(10)
        self.nwindow_results.setFont(font)
        self.nwindow_results.setReadOnly(True)
        self.nwindow_results.setObjectName("nwindow_results")
        self.exitButton_5 = QtWidgets.QPushButton(self.tab_5)
        self.exitButton_5.setGeometry(QtCore.QRect(1151, 881, 110, 29))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitButton_5.sizePolicy().hasHeightForWidth())
        self.exitButton_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.exitButton_5.setFont(font)
        self.exitButton_5.setStyleSheet("background-color:rgb(255, 147, 137);\n"
"border-color:red;\n"
"border-style:solid;\n"
"border-width:2px;")
        self.exitButton_5.setObjectName("exitButton_5")
        self.rawLabel_2 = QtWidgets.QLabel(self.tab_5)
        self.rawLabel_2.setGeometry(QtCore.QRect(20, 70, 321, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.rawLabel_2.setFont(font)
        self.rawLabel_2.setObjectName("rawLabel_2")
        self.find_nWindows = QtWidgets.QPushButton(self.tab_5)
        self.find_nWindows.setGeometry(QtCore.QRect(820, 881, 211, 29))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.find_nWindows.setFont(font)
        self.find_nWindows.setStyleSheet("background-color:rgb(180,255,255);")
        self.find_nWindows.setObjectName("find_nWindows")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_5)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 140, 711, 91))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.nWindow_length = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_2)
        self.nWindow_length.setDecimals(0)
        self.nWindow_length.setMinimum(1.0)
        self.nWindow_length.setObjectName("nWindow_length")
        self.horizontalLayout_2.addWidget(self.nWindow_length)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.type_nwindow = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.type_nwindow.setObjectName("type_nwindow")
        self.type_nwindow.addItem("")
        self.type_nwindow.addItem("")
        self.type_nwindow.addItem("")
        self.type_nwindow.addItem("")
        self.horizontalLayout_2.addWidget(self.type_nwindow)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.frame_select = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.frame_select.setObjectName("frame_select")
        self.frame_select.addItem("")
        self.frame_select.addItem("")
        self.frame_select.addItem("")
        self.frame_select.addItem("")
        self.frame_select.addItem("")
        self.frame_select.addItem("")
        self.horizontalLayout_2.addWidget(self.frame_select)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.tab_5)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(760, 140, 461, 91))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.target_seq = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.target_seq.setEnabled(True)
        self.target_seq.setText("")
        self.target_seq.setObjectName("target_seq")
        self.horizontalLayout_6.addWidget(self.target_seq)
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.submit_nWindow = QtWidgets.QLineEdit(self.tab_5)
        self.submit_nWindow.setGeometry(QtCore.QRect(20, 100, 1241, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.submit_nWindow.setFont(font)
        self.submit_nWindow.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.submit_nWindow.setObjectName("submit_nWindow")
        self.nwindow_results_2 = QtWidgets.QPlainTextEdit(self.tab_5)
        self.nwindow_results_2.setGeometry(QtCore.QRect(760, 240, 461, 631))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(10)
        self.nwindow_results_2.setFont(font)
        self.nwindow_results_2.setReadOnly(True)
        self.nwindow_results_2.setObjectName("nwindow_results_2")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.REnzSelect = QtWidgets.QTextEdit(self.tab_2)
        self.REnzSelect.setGeometry(QtCore.QRect(460, 60, 341, 851))
        self.REnzSelect.setReadOnly(True)
        self.REnzSelect.setObjectName("REnzSelect")
        self.exitButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.exitButton_2.setGeometry(QtCore.QRect(1151, 881, 110, 29))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitButton_2.sizePolicy().hasHeightForWidth())
        self.exitButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.exitButton_2.setFont(font)
        self.exitButton_2.setStyleSheet("background-color:rgb(255, 147, 137);\n"
"border-color:red;\n"
"border-style:solid;\n"
"border-width:2px;")
        self.exitButton_2.setObjectName("exitButton_2")
        self.REnzList = QtWidgets.QListWidget(self.tab_2)
        self.REnzList.setGeometry(QtCore.QRect(20, 60, 341, 851))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.REnzList.setFont(font)
        self.REnzList.setObjectName("REnzList")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 341, 41))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(460, 10, 341, 41))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.clearArrayPushButton = QtWidgets.QPushButton(self.tab_2)
        self.clearArrayPushButton.setGeometry(QtCore.QRect(820, 881, 211, 29))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.clearArrayPushButton.setFont(font)
        self.clearArrayPushButton.setStyleSheet("background-color:rgb(180,255,255);")
        self.clearArrayPushButton.setObjectName("clearArrayPushButton")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.exitButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.exitButton_3.setGeometry(QtCore.QRect(1151, 881, 110, 29))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitButton_3.sizePolicy().hasHeightForWidth())
        self.exitButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.exitButton_3.setFont(font)
        self.exitButton_3.setStyleSheet("background-color:rgb(255, 147, 137);\n"
"border-color:red;\n"
"border-width:2px;\n"
"border-style:solid;\n"
"")
        self.exitButton_3.setObjectName("exitButton_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 1121, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.detectLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.detectLabel.setFont(font)
        self.detectLabel.setObjectName("detectLabel")
        self.horizontalLayout.addWidget(self.detectLabel)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.detectPushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.detectPushButton.setFont(font)
        self.detectPushButton.setStyleSheet("background-color:rgb(180,255,255);")
        self.detectPushButton.setObjectName("detectPushButton")
        self.horizontalLayout.addWidget(self.detectPushButton)
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_3)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 60, 1241, 811))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.numeralResults = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.numeralResults.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numeralResults.sizePolicy().hasHeightForWidth())
        self.numeralResults.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(14)
        self.numeralResults.setFont(font)
        self.numeralResults.setFrameShadow(QtWidgets.QFrame.Plain)
        self.numeralResults.setObjectName("numeralResults")
        self.gridLayout.addWidget(self.numeralResults, 2, 1, 1, 1)
        self.gCutLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gCutLabel.setObjectName("gCutLabel")
        self.gridLayout.addWidget(self.gCutLabel, 1, 0, 1, 1)
        self.restrictResults = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(12)
        self.restrictResults.setFont(font)
        self.restrictResults.setFrameShape(QtWidgets.QFrame.Panel)
        self.restrictResults.setFrameShadow(QtWidgets.QFrame.Plain)
        self.restrictResults.setObjectName("restrictResults")
        self.gridLayout.addWidget(self.restrictResults, 2, 0, 1, 1)
        self.gridLayout.setColumnStretch(0, 3)
        self.gridLayout.setColumnStretch(1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_3 = QtWidgets.QLabel(self.tab_4)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.tab_4)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(20, 10, 591, 41))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_9.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.dependLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.dependLabel.setFont(font)
        self.dependLabel.setObjectName("dependLabel")
        self.horizontalLayout_9.addWidget(self.dependLabel)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem6)
        self.nPosPushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_9)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.nPosPushButton.setFont(font)
        self.nPosPushButton.setStyleSheet("background-color:rgb(180,255,255);")
        self.nPosPushButton.setObjectName("nPosPushButton")
        self.horizontalLayout_9.addWidget(self.nPosPushButton)
        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 1)
        self.horizontalLayout_9.setStretch(2, 1)
        self.exitButton_4 = QtWidgets.QPushButton(self.tab_4)
        self.exitButton_4.setGeometry(QtCore.QRect(1151, 881, 110, 29))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitButton_4.sizePolicy().hasHeightForWidth())
        self.exitButton_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.exitButton_4.setFont(font)
        self.exitButton_4.setStyleSheet("background-color:rgb(255, 147, 137);\n"
"border-color:red;\n"
"border-width:2px;\n"
"border-style:solid;\n"
"")
        self.exitButton_4.setObjectName("exitButton_4")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab_4)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 100, 1241, 771))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.posnResults = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(11)
        self.posnResults.setFont(font)
        self.posnResults.setObjectName("posnResults")
        self.gridLayout_2.addWidget(self.posnResults, 0, 0, 1, 1)
        self.picture_results = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.picture_results.setText("")
        self.picture_results.setObjectName("picture_results")
        self.gridLayout_2.addWidget(self.picture_results, 0, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.exitButton_20 = QtWidgets.QPushButton(self.tab)
        self.exitButton_20.setGeometry(QtCore.QRect(1151, 881, 107, 29))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitButton_20.sizePolicy().hasHeightForWidth())
        self.exitButton_20.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.exitButton_20.setFont(font)
        self.exitButton_20.setStyleSheet("background-color:rgb(255, 147, 137);\n"
"border-color:red;\n"
"border-width:2px;\n"
"border-style:solid;\n"
"")
        self.exitButton_20.setObjectName("exitButton_20")
        self.acceptButton = QtWidgets.QPushButton(self.tab)
        self.acceptButton.setEnabled(False)
        self.acceptButton.setGeometry(QtCore.QRect(606, 34, 211, 29))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.acceptButton.setFont(font)
        self.acceptButton.setStyleSheet("background-color:rgb(180,255,255);\n"
"border-width:2px;\n"
"border-color:green;\n"
"border-style:solid;")
        self.acceptButton.setObjectName("acceptButton")
        self.showSelects = QtWidgets.QPlainTextEdit(self.tab)
        self.showSelects.setGeometry(QtCore.QRect(16, 289, 1280, 561))
        self.showSelects.setObjectName("showSelects")
        self.fastaSelects = QtWidgets.QPlainTextEdit(self.tab)
        self.fastaSelects.setGeometry(QtCore.QRect(300, 34, 276, 235))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fastaSelects.setFont(font)
        self.fastaSelects.setObjectName("fastaSelects")
        self.dataLabel = QtWidgets.QLabel(self.tab)
        self.dataLabel.setGeometry(QtCore.QRect(17, 10, 277, 18))
        self.dataLabel.setObjectName("dataLabel")
        self.dataList = QtWidgets.QListWidget(self.tab)
        self.dataList.setGeometry(QtCore.QRect(17, 34, 277, 235))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.dataList.setFont(font)
        self.dataList.setObjectName("dataList")
        self.selectLabel = QtWidgets.QLabel(self.tab)
        self.selectLabel.setGeometry(QtCore.QRect(300, 10, 276, 18))
        self.selectLabel.setObjectName("selectLabel")
        self.tabWidget.addTab(self.tab, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.aboutExit = QtWidgets.QPushButton(self.tab_6)
        self.aboutExit.setGeometry(QtCore.QRect(1150, 870, 110, 29))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aboutExit.sizePolicy().hasHeightForWidth())
        self.aboutExit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.aboutExit.setFont(font)
        self.aboutExit.setStyleSheet("background-color:rgb(255, 147, 137);\n"
"border-color:red;\n"
"border-style:solid;\n"
"border-width:2px;")
        self.aboutExit.setObjectName("aboutExit")
        self.tabWidget.addTab(self.tab_6, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionGastrL = QtWidgets.QAction(MainWindow)
        self.actionGastrL.setObjectName("actionGastrL")
        self.actionGastr = QtWidgets.QAction(MainWindow)
        self.actionGastr.setObjectName("actionGastr")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(6)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Genomic AnalySis ToolbaR (GASTR)"))
        self.genLabel.setText(_translate("MainWindow", "Genomic Profile"))
        self.rawLabel.setText(_translate("MainWindow", "Raw Genome"))
        self.rawXLabel.setText(_translate("MainWindow", "Raw Transcriptome"))
        self.rawPLabel.setText(_translate("MainWindow", "Raw Proteome"))
        self.phageLabel.setText(_translate("MainWindow", "[No genomic profile loaded, select \'lookup\' to begin]"))
        self.lookupButton.setText(_translate("MainWindow", "Lookup"))
        self.removeButton.setText(_translate("MainWindow", "Remove"))
        self.linearCheckBox.setText(_translate("MainWindow", "Check if genome is linear"))
        self.gctLabel.setText(_translate("MainWindow", "GC content"))
        self.atgctLabel.setText(_translate("MainWindow", "AT/GC ratio"))
        self.exitButton_1.setText(_translate("MainWindow", "Exit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Mount Fasta"))
        self.genLabel_2.setText(_translate("MainWindow", "nWindows"))
        self.phageLabel_2.setText(_translate("MainWindow", "Use nWindows to manipulate Whole Genes, CDS\'s, or Assemblies into separate and independent windows for analysis"))
        self.exitButton_5.setText(_translate("MainWindow", "Exit"))
        self.rawLabel_2.setText(_translate("MainWindow", "Use prior sequence or paste a new one below"))
        self.find_nWindows.setText(_translate("MainWindow", "Find nWindows"))
        self.label_5.setText(_translate("MainWindow", "Window Length"))
        self.type_nwindow.setItemText(0, _translate("MainWindow", "basic"))
        self.type_nwindow.setItemText(1, _translate("MainWindow", "complement"))
        self.type_nwindow.setItemText(2, _translate("MainWindow", "transcribe"))
        self.type_nwindow.setItemText(3, _translate("MainWindow", "translate"))
        self.label_6.setText(_translate("MainWindow", "Output Type"))
        self.frame_select.setItemText(0, _translate("MainWindow", "Frame 1"))
        self.frame_select.setItemText(1, _translate("MainWindow", "Frame -1"))
        self.frame_select.setItemText(2, _translate("MainWindow", "Frame 2"))
        self.frame_select.setItemText(3, _translate("MainWindow", "Frame -2"))
        self.frame_select.setItemText(4, _translate("MainWindow", "Frame 3"))
        self.frame_select.setItemText(5, _translate("MainWindow", "Frame -3"))
        self.label_7.setText(_translate("MainWindow", "Define Frame"))
        self.label_8.setText(_translate("MainWindow", "Motif Target Tag (MTT)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "nWindows"))
        self.exitButton_2.setText(_translate("MainWindow", "Exit"))
        self.label_2.setText(_translate("MainWindow", "Click an enzyme from the list below\n"
"Click it again to de-select it"))
        self.label_4.setText(_translate("MainWindow", "Selected enzymes"))
        self.clearArrayPushButton.setText(_translate("MainWindow", "Clear all selections"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Digest Selection"))
        self.exitButton_3.setText(_translate("MainWindow", "Exit"))
        self.detectLabel.setText(_translate("MainWindow", "Search the fasta file for embedded enzymes and cut sites"))
        self.detectPushButton.setText(_translate("MainWindow", "Find R.Enzymes"))
        self.label.setText(_translate("MainWindow", "Numerical Hits"))
        self.gCutLabel.setText(_translate("MainWindow", "Genome Cut Sites"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Restrict Results"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>Equation:  p(A|B) = (p(B|A) * p(A)) // p(B)</p></body></html>"))
        self.dependLabel.setText(_translate("MainWindow", "Dependent Positional Probability"))
        self.nPosPushButton.setText(_translate("MainWindow", "Find N-Positions"))
        self.exitButton_4.setText(_translate("MainWindow", "Exit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Bayes Statistics"))
        self.exitButton_20.setText(_translate("MainWindow", "Exit"))
        self.acceptButton.setText(_translate("MainWindow", "Accept Selections"))
        self.dataLabel.setText(_translate("MainWindow", "Choose files:"))
        self.selectLabel.setText(_translate("MainWindow", "Selections:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "FastX "))
        self.aboutExit.setText(_translate("MainWindow", "Exit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "About"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionGastrL.setText(_translate("MainWindow", "Gastr-A"))
        self.actionGastr.setText(_translate("MainWindow", "Gastr-Ω"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

