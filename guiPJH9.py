"""
Uses QT designer QtPJH.ui file
Convert to pythhon file by:
    pyuic5.bat -x QtPJH.ui -o QtPJH.py

V5 8/4/20: - Added nWindows and associated processing.  Incomplete;
        More to be added.  Set min window length to 1.
    - set the pushbuttons inactive until there is some data to act on,
        and inactive again after that page has used the data.
    - shorten the divider on tab 4 so it does not overlap into 2 lines
    - Added click sound to
v6 8/6/20: Added functions to Electrophoressis tab:
    - put all .fasta files in the data subdirectory
    - display a list of .fasta files.  Allow the user so select some of these.
        read the selected files.  Display their header line and a sample of
        their nucleides.
v7 8/8/20: - Deleted use of tkinter to select a .fasta file.
    - Added son QDialog to select .fasta file.  Format is now more consistent with
        the rest of this app.  Select .fasta file in son dialog; see fastaData.getFasta
    - Changed main window name to GASTR.
    - Added shared.py to hold data and routines common to all GASTR modules.
    - Log file output now uses sh.log.
    - Button clicks now use sh.click.
v8 8/12/20: Added nWindows tab
    - Require an MTT input.  Validate user MTT input.
    - Set nWindow length to 1 .. 100
    - Use set (was dict) for MTT finds
    - Added "About" tab - not implemented yet
    - Show only valid fasta file types
    - changed openLog to simplify changing the number of logs saved.
    - write all.fasta as a concatenation of all chosen files, with phage name
        heading each file data.
v9 8/14/20: allow nWindows analysis with np MTT
    - changed all.fasta to include source alphabetic ID

"""
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from Bio.Seq import Seq
from Bio.Restriction import AllEnzymes
from Bio.Restriction import Analysis
import matplotlib.pyplot as plt
from pathlib import Path

from QtPJH import Ui_MainWindow
import fastaData as fd
import shared as sh

userChoices = []
enzymes = [str(enz) for enz in AllEnzymes]
enzymes.sort()
nwindow = []
EnzymesSelected = False
fastaRead       = False

class myApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        global userChoices, enzymes, fastaChoices
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.tabWidget.setCurrentIndex(0)  # Start at 1st tab

        # ----------------------  Mount Fasta tab  --------------------------
        self.lookupButton.clicked.connect(self.putFasta)
        self.removeButton.clicked.connect(self.resetFasta)
        self.exitButton_1.clicked.connect(exitApp)

        # ----------------------  nWindows tab  ----------------------------
        self.find_nWindows.clicked.connect(self.find_windows)
        self.exitButton_5.clicked.connect(exitApp)

        # ----------------------  Digest Selection tab  --------------------
        userChoices = []
        for enz in enzymes:
            self.REnzList.addItem("{:s}".format(enz))
        self.clearArrayPushButton.clicked.connect(self.clearArray)
        self.REnzList.itemClicked.connect(self.addREnzyme)
        self.exitButton_2.clicked.connect(exitApp)

        # ----------------------  Restrict Results tab  ---------------------
        # Restriction points have been found using BioPythons RESTRICTION module.
        # http://biopython.org/DIST/docs/cookbook/Restriction.html
        self.restrictResults.insertPlainText("Cut results will display here")
        self.numeralResults.insertPlainText("Numeric results results will display here\n")
        self.detectPushButton.clicked.connect(self.run_p)
        self.exitButton_3.clicked.connect(exitApp)

        # ------------------------   Bayes tab   ---------------------------
        self.nPosPushButton.clicked.connect(self.markov)
        self.posnResults.insertPlainText("Results will appear here\n")
        self.exitButton_4.clicked.connect(exitApp)

        # ----------------------  FastX tab  --------------
        self.fastaChoices = []
        self.listFastaFiles()
        self.dataList.itemClicked.connect(self.addFile)
        self.acceptButton.clicked.connect(self.acceptFastas)
        self.exitButton_20.clicked.connect(exitApp)

        # ----------------------  About tab  --------------
        self.aboutExit.clicked.connect(exitApp)

    def putFasta(self):
        global fastaRead
        sh.log("\nstart putFasta")
        sh.click()
        self.removeButton.setEnabled(True)
        self.lookupButton.setEnabled(False)
        self.find_nWindows.setEnabled(True)
        fastaName, fasta = fd.readFasta()
        self.phageLabel.setText("{:s}:  {:s}".format(fastaName, fasta.phage))
        # Ensure that the purine length is a multiple of 3.  Truncate if needed.
        purnz = fasta.purines[:3*((len(fasta.purines)//3))]
        self.genTextEdit.insertPlainText(purnz)
        self.submit_nWindow.setText(purnz)
        self.rawLabel_2.setText ("Use {:s} sequence or paste a new one below"
            .format (fastaName))
        self.sequence = Seq(purnz)
        RNA = self.sequence.transcribe()  # DNA sequence -> RNA sequence
        self.transTextEdit.insertPlainText(str(RNA))
        protein = RNA.translate("Standard", "#")  # nucleotide sequence -> protein sequence
        self.protTextEdit.insertPlainText(str(protein))
        (act, gct, cct, tct) = (self.sequence.count(x) for x in ('A', 'G', 'C', 'T'))
        gcCount = (gct + cct) / (act + gct + cct + tct) * 100
        self.gcLabel.setText("{:5.2f}%".format(gcCount))
        atgcRatio = ((act + tct) / (gct + cct))
        self.atgcLabel.setText("{:4.2f}".format(atgcRatio))
        fastaRead = True

    def resetFasta(self):
        # erase the fasta file and clear all items depending on it
        global fastaRead, userChoices
        sh.click()
        self.removeButton.setEnabled(False)
        self.genTextEdit.clear()
        self.submit_nWindow.clear()
        self.transTextEdit.clear()
        self.protTextEdit.clear()
        self.phageLabel.clear()
        self.restrictResults.clear()
        self.numeralResults.clear()
        self.REnzSelect.clear()
        userChoices = []
        self.posnResults.clear()
        self.picture_results.clear()
        self.submit_nWindow.clear()
        self.nwindow_results.clear()
        self.nwindow_results_2.clear()
        self.target_seq.clear()
        self.lookupButton.setEnabled(True)
        self.clearArrayPushButton.setEnabled(False)												   
        self.detectPushButton.setEnabled(False)
        self.nPosPushButton.setEnabled(False)
        self.find_nWindows.setEnabled(False)
        self.acceptButton.setEnabled(False)
        fastaRead = False
        sh.log("Erased fasta file")

    def find_windows(self):
        # creates a window of information based on user parameters that can be submitted to other sequence software
        # Raw to Defined to string[ start_index_pos: end_index_pos: step_size]
        global nwindow
        sh.click()
        sh.log ("\nStart find_windows")
        length = int(self.nWindow_length.value())

        # First, identify user's FRAME reference.
        if self.frame_select.currentText() == 'Frame 1':
            #temp_hold = str(self.submit_nWindow.text())
            temp_hold = self.submit_nWindow.text()
        elif self.frame_select.currentText() == 'Frame 2':
            temp_hold = self.submit_nWindow.text()[1:]
        elif self.frame_select.currentText() == 'Frame 3':
            temp_hold = self.submit_nWindow.text()[2:]
        elif self.frame_select.currentText() == 'Frame -1':
            temp_hold = self.submit_nWindow.text()[::-1]
        elif self.frame_select.currentText() == 'Frame -2':
            temp_hold = self.submit_nWindow.text()[-2::-1]
        elif self.frame_select.currentText() == 'Frame -3':
            temp_hold = self.submit_nWindow.text()[-3::-1]

        # Second, use BIOPYTHON to translate the initial text using the central dogma
        if self.type_nwindow.currentText() == 'basic':
            nwindow = Seq(temp_hold).complement()
        elif self.type_nwindow.currentText() == 'transcribe':
            nwindow = Seq(temp_hold).transcribe()
        elif self.type_nwindow.currentText() == 'translate':
            nwindow = Seq(temp_hold).translate()
        #print("nwindow", nwindow[:80])
        window_out = [str(nwindow)[i:i + length] for i in range(0, len(nwindow), length)]
        sh.log ("window_out ({:n}): {:s}".format (len(window_out), str(window_out)[:80]))

        # Third, identify the USER requested MOTTIF target and display the
        # Check that the user MTT entry is valid
        self.nwindow_results_2.clear()
        tgtMTT = self.target_seq.text().upper()  # ensure MTT is all capitals
        if len(tgtMTT) > length:
            self.nwindow_results_2.insertPlainText \
                ("MTT length must be <= {:n}".format (length))
        else:
            if len(tgtMTT) == 0:
                self.nwindow_results_2.insertPlainText("No MTT selected")
            else:
                targetSet = set()       # set of all MTT matches
                for finds in window_out:
                    if finds.find(tgtMTT) >= 0:
                        targetSet.add (finds)
                if len(targetSet) == 0:
                    self.nwindow_results_2.insertPlainText(
                        'No matches found for {:s} ({:s})'
                            .format(tgtMTT, self.type_nwindow.currentText().upper()))
                else:
                    self.nwindow_results_2.insertPlainText(
                        'Target Spotted! - Displaying your {:s} ({:s}) report below\n\n' \
                        .format (tgtMTT, self.type_nwindow.currentText().upper()))
                    for finds in targetSet:
                        self.nwindow_results_2.insertPlainText(finds + '\n')
            for strings in window_out:
                if len(strings) < length:
                    window_out.pop(window_out.index(strings))
            xlate = str(list(window_out)).maketrans ("", "", "'[],")    # don't show "[],'"
            self.nwindow_results.setPlainText(str(list(window_out)).translate(xlate))

    def addREnzyme(self):
        # select enzymes to be used in the Restrict results tab
        global userChoices
        sh.log("\nstart addREnzyme")
        sh.click()															
        if sh.debug:
            userChoices = ["AanI", "BmeDI", "ZraI", "AquIII", "YkrI", "Bau1417V", "XmnI", "Ble402II"]
            self.REnzSelect.clear()
            for enz in userChoices:
                self.REnzSelect.insertPlainText("{:s}\n".format(enz))
        else:
            choice = self.REnzList.currentItem().text()
            sh.log("choice:" + choice)
            if choice in userChoices:
                userChoices.remove(choice)  # remove existing item
            else:
                userChoices.append(choice)  # add this item
            sh.log("user choices:" + str(userChoices))
            self.REnzSelect.clear()
            for enz in userChoices:
                self.REnzSelect.insertPlainText("{:s}\n".format(enz))
        self.detectPushButton.setEnabled(len(userChoices) > 0)
        self.clearArrayPushButton.setEnabled(len(userChoices) > 0)															  

    def clearArray(self):
        global userChoices
        sh.click()															
        userChoices = []
        self.REnzSelect.clear()
        sh.log("Clear choices")
        self.detectPushButton.setEnabled(len(userChoices) > 0)
        self.clearArrayPushButton.setEnabled(False)
        self.detectPushButton.setEnabled(False)															  

    def run_p(self):
        global userChoices, enzymes, fastaRead
        sh.log("\nstart run_p")
        sh.click()
        self.restrictResults.clear()
        self.numeralResults.clear()
        if not fastaRead:
            self.restrictResults.setPlainText("You must select a fasta file first")
            return
        if len(userChoices) <= 0:
            self.restrictResults.setPlainText("You must select R.Enzymes first")
            return
        self.detectPushButton.setEnabled(False)  # can't run twice
        try:
            linear = self.linearCheckBox.isChecked()
            analysis = Analysis(userChoices, self.sequence, linear=linear)
        except:
            sh.log("analysis failed " + sys.exc_info()[0])
        # print each enzyme with a list of it's matching sites
        cutSites = str(
            analysis.format_output(dct=None, title='',
                s1='\n  Enzymes which do not cut the sequence\n'))
        self.restrictResults.setPlainText(cutSites)
        # ------------------------------- FIND PALINDROME HIT COUNTS -----------------------------------------------
        try:
            endMarker = "END"
            enzymes.append(endMarker)
            # Extract enzymes and the index of their cutSites from cutSites
            palin = cutSites[:cutSites.find("Enzymes")].replace('.', "").replace(':', "").split()
            palin.append(endMarker)
            sh.log("palin: " + str(palin))
        except:
            sh.log("palin NG " + sys.exec_info()[0])
        try:
            # Calculate and display the number of matching sites for each enzyme
            # enzPosn initally has a list of lists.  Each sublist has the enzyme name
            #   and the index of the enzyme in palin
            # enzPosn sublist later has the enzyme name and the number of matches.
            enzPosn = []
            enzNone = []
            sh.log("len palin " + str(len(palin)))
            sh.log("user choices " + str(userChoices))
            allChoices = userChoices
            allChoices.append(endMarker)  # matches last name in palin
            sh.log("allChoices " + str(allChoices))
            for enz in allChoices:
                if enz in palin:
                    enzPosn.append([enz, palin.index(enz)])
                else:
                    sh.log(enz + " not in palin")
                    enzNone.append(enz)
            sh.log("enzPosn = " + str(enzPosn))
            enzPosn.sort(key=lambda x: x[1])  # sort on index of name in palin
            for i in range(len(enzPosn) - 1):  # Replace the index with the
                enzPosn[i][1] = enzPosn[i + 1][1] - enzPosn[i][1] - 1  # length of palin entry
            del enzPosn[-1]  # delete endMarker
            for enz in enzNone:
                enzPosn.append([enz, 0])  # add in enzymes not found; length = 0
            enzPosn.sort(key=lambda x: x[0])  # sort on name
            sh.log("enzPosn = " + str(enzPosn))
            for i in range(len(enzPosn)):  # show the number of matches for each enzyme
                matchStr = "{0:7,d} : {1:s}\n\n".format(enzPosn[i][1], enzPosn[i][0])
                self.numeralResults.insertPlainText(matchStr)
        except:
            sh.log('I cannot do that. ' + sys.exec_info()[0])
        self.detectPushButton.setEnabled(False)
        self.nPosPushButton.setEnabled(True)											   

    # -------------------------------- TAB 4 DEFINITIONS  ------------------------------------------------------------------

    def markov(self):
        # Markov Model Algorithm gathered from Drexel University
        # https://faculty.coe.drexel.edu/gailr/ECE-S690-503/markov_models.ppt.pdf
        # Equation used aBA=Pr(xi=B|xi-1=A)
        sh.log("\nstart markov")
        sh.click()															
        self.nPosPushButton.setEnabled(False)  # Need new fasta to run this again
        seq = 'ATGC'
        single = [x for x in seq]
        double = [x + y for x in seq for y in seq]
        triple = [x + y + z for x in seq for y in seq for z in seq]

        monograms = {monos: self.sequence.count(monos) / len(self.sequence) for monos in single}
        mono_counts = sum(monograms.values())  # Must be = 1.0

        # The following algorithm finds the probability of a dinucleotides in a sequence. --------------------------------------
        # DIGRAMS are used so the full len is found. ---------------------------------------------------------------------------

        adjusted_sequence = self.sequence[:-1]

        bi_monograms = {items: adjusted_sequence.count(items) for items in single}
        bigrams = {items: self.sequence.count(items) / bi_monograms[items[0]] for items in double}
        sh.log("monograms: " + str(monograms))
        sh.log("bi monograms " + str(bi_monograms))
        sh.log("bigrams " + str(bigrams))
        sh.log("double = " + str(double))
        bi = {x + y: bigrams[x + y] for x in seq for y in seq}
        self.posnResults.insertPlainText("Results 20\n")

        # The following algorithm finds the probability of a dinucleotides in a sequence. --------------------------------------
        # TRIGRAMS are used so the full len is found. ---------------------------------------------------------------------------

        adjusted_sequence = self.sequence[:-2]

        tri_monograms = {items: adjusted_sequence.count(items) for items in single}
        tri_bigrams = {items: adjusted_sequence.count(items) for items in double}
        trigrams = {items: self.sequence.count(items) / tri_bigrams[items[:-1]] for items in triple}
        sh.log("tri_monograms " + str(tri_monograms))
        sh.log("tri_bigrams   " + str(tri_bigrams))
        sh.log("trigrams      " + str(trigrams))

        self.posnResults.insertPlainText("Results 30")
        tri = {x + y + z: trigrams[x + y + z] for x in seq for y in seq for z in seq}
        self.posnResults.clear()

        # Generate report on the probabilities
        sep = '-----------------------------------------'
        rpt = "{:s}\nMONOGRAM PROBABILITIES\n\n".format(sep)
        for mon in seq:
            rpt += "{:s}: {:11.9f} \n".format(mon, monograms[mon])
        rpt += "\n\nTotal = {:3.1f}\n{:s}\nBIGRAM PROBABILITIES\n\n".format(sum(monograms.values()), sep)
        for duo in double:
            rpt += "{:2s}: {:11.9f} \n".format(duo, bi[duo])
            if duo[1] == "C": rpt += "\n"
        rpt += "\nTotal = {:3.1f}\n{:s}\nTRIGRAM PROBABILITIES\n\n".format(sum(bi.values()), sep)
        spc = 4
        for tre in triple:
            rpt += "{:s}: {:11.9f} \n".format(tre, tri[tre])
            if tre[2] == "C":
                rpt += "\n"
                spc -= 1
                if spc <= 0:
                    rpt += "\n"  # blank line between groups of 4
                    spc = 4
        rpt += "Total = {:3.1f}\n{:s}\n".format(sum(tri.values()), sep)

        #sh.log(str(rpt))
        self.posnResults.clear()          # Ensure we print to a blank window
        self.posnResults.insertPlainText(rpt)

        # ---------------------------------------------------------
        # Create a Bar Graph of all transition probabilities.
        # prob = dictionary of mono-, bi-, tri- grams
        # Each dictionary item has 2 lists:
        #   [leprober code] and corresponding [probability]
        # ---------------------------------------------------------
        prob = {xx: [[], []] for xx in seq}

        getStates(prob, monograms)
        getStates(prob, bigrams)
        getStates(prob, trigrams)
        for key, value in prob.items():
            sh.log("prob[{:s}]: {:s}".format(key, str(value[0])))
            sh.log("         {:s}".format(str(value[1])))

        fig, a = plt.subplots(2, 2)
        graphs = [a[0][0], a[0][1], a[1][0], a[1][1]]
        fig.set_size_inches(10, 8)
        a[0][0].bar(prob["A"][0], prob["A"][1])
        a[0][0].set_title('p(A) Transition States', fontsize=14)
        a[0][1].bar(prob["T"][0], prob["T"][1])
        a[0][1].set_title('p(T) Transition States', fontsize=14)
        a[1][0].bar(prob["C"][0], prob["C"][1])
        a[1][0].set_title('p(C) Transition States', fontsize=14)
        a[1][1].bar(prob["G"][0], prob["G"][1])
        a[1][1].set_title('p(G) Transition States', fontsize=14)
        for subs in graphs:
            plt.setp(subs.xaxis.get_majorticklabels(), rotation=90)
            subs.set_ylim(0, 1)
        plt.tight_layout(pad=1.5)
        if not Path('pictures').exists():
            Path('pictures').mkdir()  # create the directory if it is missing
        plt.savefig('pictures/Results.png', dpi=100)
        self.picture_results.setPixmap(QPixmap('pictures/Results.png'))
        # plt.show()

    def addFile (self):
        sh.click()
        sh.log ("\nstart addFile")
        choice = self.dataList.currentItem().text()
        sh.log("choice: " + choice)
        if choice in self.fastaChoices:
            self.fastaChoices.remove(choice)  # remove existing item
        else:
            self.fastaChoices.append(choice)  # add this item
        sh.log(".fasta choices: " + str(self.fastaChoices))
        self.fastaSelects.clear()
        for fast in self.fastaChoices:
            self.fastaSelects.insertPlainText("{:s}\n".format(fast))
        self.acceptButton.setEnabled(len(self.fastaChoices) > 0)

    def acceptFastas (self):
        # Show the chosen files
        sh.log ("\nstart acceptFastas")
        sh.click()
        self.acceptButton.setEnabled(False)
        savFile = "data/all.fasta"
        if Path (savFile).is_file():
            Path(savFile).unlink()      # delete old all.fasta
        sav = open (savFile, "a")       # open for append
        self.showSelects.clear()
        first = True                    # first file ID = alfa
        for choice in self.fastaChoices:
            fast = fd.fasta ("data/" + choice, reset = first)
            self.showSelects.insertPlainText ("{:s}: {:s} -> {:s}\n".format (fast.ID, choice, fast.phage))
            self.showSelects.insertPlainText ("length = {:,d} > {:s} ... {:s}\n\n"
                .format (len(fast.purines), fast.purines[:20], fast.purines[-20:]))
            print ("> {:s} {:s}".format (fast.ID, fast.phage), file=sav)
            print (fast.data, file=sav)        # copy choice to all.fasta
            first = False
        sav.close()
        self.showSelects.insertPlainText ("The concatenation of these choices saved as {:s}".format (savFile))

    def listFastaFiles (self):
        # Show available data files in the FastX tab
        sh.log ("\nstart listFastaFiles")
        fd.showValidFastaFiles (self.dataList)

def exitApp():
    sh.click()
    sh.logClose ()
    sys.exit(0)

def getStates(tt, probGram):
    for key, value in probGram.items():
        kkey = key[:1]
        if kkey == 'A':
            tt[kkey][0].append(key)
            tt[kkey][1].append(value)
        elif kkey == 'T':
            tt[kkey][0].append(key)
            tt[kkey][1].append(value)
        elif kkey == 'C':
            tt[kkey][0].append(key)
            tt[kkey][1].append(value)
        elif kkey == 'G':
            tt[kkey][0].append(key)
            tt[kkey][1].append(value)

sh.openLog()
app = QApplication(sys.argv)
GASTR = myApp()
GASTR.show()
sys.exit((app.exec_()))
