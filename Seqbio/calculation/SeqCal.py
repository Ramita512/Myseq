

def gcContent(seq):
    # G+C/(A+T+G+C)
    seq = seq.upper()
    return (countBase(seq, 'G') + countBase(seq, 'C'))/len(seq)

def atContent(seq):
    # A+T/(A+T+G+C)
    seq = seq.upper()
    return (countBase(seq, 'A') + countBase(seq, 'T'))/len(seq)

def countBase(seq, base):
    seq = seq.upper()
    cBase = seq.count(base.upper())
    return cBase
    
def countBases(seq):
    seq = seq.upper()
    basesM = {}
    for base in seq:
        basesM[base] = basesM.get(base, 0)+1
    return basesM



# if __name__ == '__main__':
#     seq = 'ATGGGccGTAGAATTCTTGCaaGCCCGT'
    
#     print("testttt:GC Content:", gcContent(seq))
#     print("Count Bases: ", countBasesDict(seq))



    