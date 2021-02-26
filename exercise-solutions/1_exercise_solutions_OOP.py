"""
    File name: 1_exercise_solutions_OOP
    Author: Eisha Ahmed
    Last Modified: 2021/02/25
    Python Version: 3.6
"""

class Dna:
    validChars = set(["A", "a", "T", "t", "C", "c", "G", "g", " "])
    def __init__(self, name, seq):
        """Initialize Dna object."""
        self.name = name
        self.seq = seq
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


if __name__ == "__main__":
    # test DNA string validation
    testString1 = "GGGCGTAGCGTAGCGC"
    testString2 = "I'm not DNA at all"
    print(Dna.isValidDNA(testString1))
    print(Dna.isValidDNA(testString2))

    # test other methods
    seq1 = Dna("name1", "GGGCCCAAATTT")
    seq2 = Dna("name1", "ATGGCTAGCTAGCTGAC")

    print(seq1.gcContent())                     # should return 0.5
    print(len(seq2))                            # should return 17
    print(seq1)                                 # output in FASTA format

    # test addition
    seq3 = seq1 + seq2
    print(seq3)                                 # output in FASTA format
