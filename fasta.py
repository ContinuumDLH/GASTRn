"""
Read a .fasta file and return its data or description as needed
"""

alphabet = ["alfa", "bravo", "charlie", "delta", "echo", "foxtrot", "golf",
            "hotel", "india", "juliet", "kilo", "lima", "mike", "november",
            "oscar", "papa", "quebec", "romeo", "sierra", "tango", "uniform",
            "victor", "whiskey", "xray", "yankee", "zulu"]

class fasta:
    crntAlfa = 0

    def __init__(self, src):
        global log
        crntAlfa = 0
        self.source = src
        self.phage = src.readline()[1:].replace("\n", "")  # 1st line: name of the phage
        self.data = src.read().replace("\n", "")
        self.name = alphabet[crntAlfa]
        crntAlfa += 1
        print("read Fasta file:", self.phage, file=log)
        src.close()

    def name(self):
        return self.name

    def data(self):
        return self.data

    def description(self):
        return self.phage

