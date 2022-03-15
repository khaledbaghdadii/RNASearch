from main import represent
#set-based similarity measures
# tag based
def jaccSim(seq1,seq2):
    seq1set=represent(seq1)[0]
    seq2set=represent(seq2)[0]
    minsum=0
    multA=0
    multB=0
    for nuc in seq1set.keys():
        minsum=minsum+min(seq1set.get(nuc),seq2set.get(nuc))
        multA=multA+seq1set.get(nuc)
        multB=multB+seq2set.get(nuc)
    jaccardSim=minsum/(multA+multB-minsum)
    return jaccardSim

def dice(seq1,seq2):
    seq1set=represent(seq1)[0]
    seq2set=represent(seq2)[0]
    minsum=0
    multA=0
    multB=0
    for nuc in seq1set.keys():
        minsum=minsum+min(seq1set.get(nuc),seq2set.get(nuc))
        multA=multA+seq1set.get(nuc)
        multB=multB+seq2set.get(nuc)
    diceSim=(2*minsum)/(multA+multB)
    print(seq1set)
    print(seq2set)
    return diceSim

def intersectSim(seq1,seq2):
    seq1set=represent(seq1)[0]
    seq2set=represent(seq2)[0]
    minsum=0
    for nuc in seq1set.keys():
        minsum=minsum+min(seq1set.get(nuc),seq2set.get(nuc))
    intersectSim=minsum
    print(seq1set)
    print(seq2set)
    return intersectSim
