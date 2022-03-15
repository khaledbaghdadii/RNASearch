import xml.etree.ElementTree as ET

#represent in multi-set and vector-based
def represent(sequence):
    nuc=["A","C","G","U"]
    setBased={
        "G":0,
        "U":0,
        "A":0,
        "C":0
    }
    # G U A C
    vectorBased=[0,0,0,0]
    for nucleotide in sequence:
        if nucleotide in nuc:
            setBased[nucleotide]=setBased[nucleotide]+1
            if nucleotide=="G":
                vectorBased[0]=vectorBased[0]+1
            if nucleotide=="U":
                vectorBased[1]=vectorBased[1]+1
            if nucleotide=="A":
                vectorBased[2]=vectorBased[2]+1
            if nucleotide=="C":
                vectorBased[3]=vectorBased[3]+1
        else:
            if nucleotide=="R":
                setBased["A"]=setBased["A"]+0.5
                setBased["G"]=setBased["G"]+0.5
                vectorBased[0]=vectorBased[0]+0.5
                vectorBased[2]=vectorBased[2]+0.5
            if nucleotide=="M":
                setBased["A"]=setBased["A"]+0.5
                setBased["C"]=setBased["C"]+0.5
                vectorBased[2]=vectorBased[2]+0.5
                vectorBased[3]=vectorBased[3]+0.5
            if nucleotide=="S":
                setBased["C"]=setBased["C"]+0.5
                setBased["G"]=setBased["G"]+0.5
                vectorBased[0]=vectorBased[0]+0.5
                vectorBased[3]=vectorBased[3]+0.5
            if nucleotide=="V":
                setBased["A"]=setBased["A"]+(1/3)
                setBased["G"]=setBased["G"]+(1/3)
                setBased["C"]=setBased["C"]+(1/3)
                vectorBased[0]=vectorBased[0]+(1/3)
                vectorBased[2]=vectorBased[2]+(1/3)
                vectorBased[3]=vectorBased[3]+(1/3)
            if nucleotide=="N":
                setBased["A"]=setBased["A"]+0.25
                setBased["G"]=setBased["G"]+0.25
                setBased["C"]=setBased["C"]+0.25
                setBased["U"]=setBased["U"]+0.25
                vectorBased[0]=vectorBased[0]+0.25
                vectorBased[1]=vectorBased[1]+0.25
                vectorBased[2]=vectorBased[2]+0.25
                vectorBased[3]=vectorBased[3]+0.25
    return setBased,vectorBased


def parseSequences(path):
    tree = ET.parse(path)
    sequences = []

    RNAS = tree.findall('RNA')
    for RNA in RNAS:
        sequences.append(RNA[3].text)

    print("Parsed successfully")
    return sequences

