"""
    File name: 2_exercise_solutions_OOP
    Author: Eisha Ahmed
    Last Modified: 2021/02/25
    Python Version: 3.6
"""

class Dna:
    validChars = set(["A", "a", "T", "t", "C", "c", "G", "g"])
    def __init__(self, name, seq):
        """Initialize Dna object."""
        self.name = name
        self.seq = seq.replace(" ", "").upper()
        return

    def __repr__(self):
        """Returns string reprsentation of Dna object (FASTA format)."""
        return "> {}\n{}".format(self.name, self.seq)

    def __add__(self, o):
        """Overloads '+' operator; concatenates both DNA sequences and names
        when operated on, and returns a new Dna object."""
        newName = '{}_{}'.format(self.name, o.name)
        newSeq = self.seq + o.seq
        return Dna(newName, newSeq)

    def __len__(self):
        return len(self.seq)

    def gcContent(self):
        """Computes percent GC content of DNA sequence (ranges from 0 to 1).
        Returns float."""
        count = 0
        for c in self.seq:
            if (c == 'C') or (c == 'G'):
                count += 1
        return count/len(self.seq)

    @classmethod
    def isValidDNA(cls, myStr):
        """Determines if a given string is a valid DNA sequence, i.e. only
        contains characters a, t, c, and g. Returns Boolean value.

        Example usage: Dna.isValidDNA(someStrimg)"""
        isDNA = False
        if all(i in cls.validChars for i in myStr):
            isDNA = True
        return isDNA

class Orf(Dna):
    """Child class that extens Dna class; represents open reading frames."""
    codonMap = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }

    def translate(self, showStopCodon=False):
        """Generates the protein sequence associated with the ORF."""
        protein = ""
        endShift = 0 if showStopCodon else 3

        for i in range(0, len(self.seq)-endShift, 3):
            protein += Orf.codonMap[self.seq[i:i+3]]
        return protein

    @classmethod
    def isValidORF(cls, myStr):
        """Determines if a given string is a valid open reading frame. Returns
        Boolean value. To be a valud ORF, the following must be satisfied:

        (1) string only contains characters a, t, c, and g.
        (2) Length of string must be at least 6 characters
        (3) Length of string must be a multiple of 3
        (4) The first 3 characters must map to the start codon (i.e. 'ATG')
        (5) The last 3 characters must map to a stop codon

        Example usage: Dna.isValidDNA(someStrimg)"""
        isORF = False
        myStr = myStr.upper()

        # make a number of boolean expressions to check string characteristics
        isCorrectLength = (len(myStr) >= 6) and (len(myStr) % 3 == 0)

        if isCorrectLength:
            hasStartCodon = cls.codonMap[myStr[0:3].upper()] == 'M'

            stopCount = 0
            for i in range(0, len(myStr), 3):
                # count the number of stop codons
                if Orf.codonMap[myStr[i:i+3].upper()] == '_':
                    stopCount += 1

            hasEndingStopCodon = (cls.codonMap[myStr[-3:].upper()] == '_') and (stopCount == 1)

            if hasStartCodon and hasEndingStopCodon and cls.isValidDNA(myStr):
                isORF = True

        return isORF

if __name__ == "__main__":
    # test ORF class and translate method
    orf1 = Orf("Random ORF 1", "atgggcctaaagtag")
    print(orf1.translate())

    # test ORF string validation
    myStr1 = "atgggcctaaagtag"
    myStr2 = "atgccca"

    print(Orf.isValidORF(myStr1))
    print(Orf.isValidORF(myStr2))
