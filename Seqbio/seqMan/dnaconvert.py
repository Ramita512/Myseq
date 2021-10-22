def reverseSeq(seq):
    return seq[::-1]

def complementSeq(seq):
    compl = {"A": "T", "T": "A",
             "G": "C", "C": "G"}
    complementary = "".join([ compl[base] for base in seq ])
    return complementary

def reverseComplementSeq(seq):
    seq = seq.upper()
    revComp = complementSeq(reverseSeq(seq))
    return revComp

def transcription(seq):
    seq = seq.upper()
    rna = seq.replace("T","U")
    return rna

def translation(seq):
    seq = seq.upper()
    DNA_Codons = loadCodons()
    protein = ""
    for i in range(0,len(seq),3):
        dna = seq[i:i+3]
        protein += DNA_Codons.get(dna, "")
    return protein

def loadCodons():
    DNA_Codons = {
        # 'M' - START, '_' - STOP
        "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "TGT": "C", "TGC": "C",
        "GAT": "D", "GAC": "D",
        "GAA": "E", "GAG": "E",
        "TTT": "F", "TTC": "F",
        "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
        "CAT": "H", "CAC": "H",
        "ATA": "I", "ATT": "I", "ATC": "I",
        "AAA": "K", "AAG": "K",
        "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
        "ATG": "M",
        "AAT": "N", "AAC": "N",
        "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "CAA": "Q", "CAG": "Q",
        "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
        "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "AGT": "S", "AGC": "S",
        "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
        "TGG": "W",
        "TAT": "Y", "TAC": "Y",
        "TAA": "_", "TAG": "_", "TGA": "_"
    }
    return DNA_Codons