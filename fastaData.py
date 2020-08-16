"""
Read a fasta file and return its data as requested
Save the data in the fastaFiles dictionary
"""
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from pathlib import Path
from sonA import Ui_sonADialog
import shared as sh

alphabet = ("alfa",   "bravo",   "charlie", "delta",  "echo",   "foxtrot", "golf",
            "hotel",  "india",   "juliet",  "kilo",   "lima",   "mike",    "november",
            "oscar",  "papa",    "quebec",  "romeo",  "sierra", "tango",   "uniform",
            "victor", "whiskey", "xray",    "yankee", "zulu")
fastaFiles = {}     # All opened .fasta files
fastaTypes = ("fasta", "FASTA", "fas", "FAS", "txt") # allowable fasta file types

class showValidFastaFiles ():
    # Show the valid fasta files in fileWindow
    def __init__ (self, fileWindow):
        path = Path(r"data/")
        for entry in path.iterdir():
            whereDot = entry.name.find(".")
            if whereDot > 0:
                if entry.name[whereDot+1:] in fastaTypes:
                    if entry.name != "all.fasta":
                        fileWindow.addItem (entry.name)

class sonAWdw(QDialog, Ui_sonADialog):
    # Open a dialog an show a selection of .fasta files
    def __init__ (this):
        QDialog.__init__(this)
        this.setupUi(this)
        # list the candidate files
        showValidFastaFiles (this.sonAList)
        this.sonAList.itemClicked.connect(selectedFile)

def selectedFile ():
    # The user has selected a .fasta file for analysis
    global son, choice
    sh.click()
    choice = son.sonAList.currentItem().text()
    sh.log ("son choice: {:s}".format (choice))
    son.close ()        # close the son dialog

class fasta ():
    # .fasta file class.  Open the file and read its contents.
    crntAlfa = 0
    def __init__ (self, src, reset=False):
        if reset:
            fasta.crntAlfa = 0      # this file ID is alpha
        self.source = src
        try:
            fas = open (src)
            self.phage   = fas.readline()[1:].replace("\n", "")  # 1st line: name of the phage
            self.data    = fas.read()              # all the rest of the file
            self.purines = self.data[:].replace("\n", "")  # One long string
        except:
            print ("No valid .fasta file chosen: ", src)
            sh.log("No valid .fasta file chosen: " + src)
            exit(12)
        fas.close()
        self.ID = alphabet[fasta.crntAlfa]      # Assign a unique name from the alphabet
        fastaFiles[self.ID] = self
        fasta.crntAlfa += 1

def getFasta ():
    # have the user select a .fasta file, and return its contents
    global son, choice
    sh.log("start son")
    son = sonAWdw()
    son.exec_()         # Start son. Wait until son finishes
    sh.log("choice = " + choice)
    return choice, fasta("data/" + choice)

def readFasta():
    # Read a fasta file
    if sh.debug:
        fastaName, fast = "NHagos.fasta", fasta ("data/NHagos.fasta")
    else:
        fastaName, fast = getFasta ()
    sh.log (".fasta file: " + fast.source)
    sh.log ("phage: " + fast.phage)
    for key, value in fastaFiles.items ():
        sh.log ("{:s}: {:s}".format (key, value.phage))
    return fastaName, fast

