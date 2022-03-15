from numpy.lib import math

def intersectSimPath(seq1set,seq2set):
    minsum=0
    for nuc in seq1set.keys():
        if nuc in seq2set.keys():
            minsum=minsum+min(seq1set.get(nuc),seq2set.get(nuc))
    intersectSim=minsum
    return intersectSim

def jaccSimPath(seq1set,seq2set):
    minsum=0
    multA=0
    multB=0
    for nuc in seq1set.keys():
        if nuc in seq2set.keys():
            minsum=minsum+min(seq1set.get(nuc),seq2set.get(nuc))
            multA=multA+seq1set.get(nuc)
            multB=multB+seq2set.get(nuc)
        else:
            multA=multA+seq1set.get(nuc)
    for nuc3 in seq2set.keys():
        if nuc3 not in seq1set.keys():
            multB=multB+seq2set.get(nuc3)
    jaccardSim=minsum/(multA+multB-minsum)
    return jaccardSim

def diceSimPath(seq1set,seq2set):
    minsum=0
    multA=0
    multB=0
    for nuc in seq1set.keys():
        if nuc in seq2set.keys():
            minsum=minsum+min(seq1set.get(nuc),seq2set.get(nuc))
            multA=multA+seq1set.get(nuc)
            multB=multB+seq2set.get(nuc)
        else:
            multA=multA+seq1set.get(nuc)
    for nuc3 in seq2set.keys():
        if nuc3 not in seq1set.keys():
            multB=multB+seq2set.get(nuc3)
    diceSim=(2*minsum)/(multA+multB)
    #print(seq1set)
    #print(seq2set)
    return diceSim


def allPath(sequence,index,path,nuc,cost,dict_list):
    paths={}
    nuc_list=["A","C","G","U"]
    ambigious=["R","M","S","V","N"]
    ambs={"R":["G","A"],
          "M":["A","C"],
          "S":["G","C"],
          "V":["G","A","C"],
          "N":["G","U","A","C"]
          }
    if nuc in nuc_list:
        path=path+nuc
        if path not in paths.keys():
            paths[path]=cost
            dict_list.append(paths)
            if index<len(sequence)-1:
                paths=allPath(sequence,index+1,path,sequence[index+1],cost,dict_list)

        # else:
        #   paths[path]+=cost
        #   print("fouund",paths)
        #   if index<len(sequence)-1:
        #     paths=allPath(sequence,index+1,path,paths,sequence[index+1],cost,dict_list)
    elif nuc in ambigious:
        if nuc=="R":
            paths=allPath(sequence,index,path,"A",0.5,dict_list)
            paths=allPath(sequence,index,path,"G",0.5,dict_list)
        elif nuc=="M":
            paths=allPath(sequence,index,path,"A",0.5,dict_list)
            paths=allPath(sequence,index,path,"C",0.5,dict_list)
        elif nuc=="S":
            paths=allPath(sequence,index,path,"G",0.5,dict_list)
            paths=allPath(sequence,index,path,"C",0.5,dict_list)
        elif nuc=="V":
            paths=allPath(sequence,index,path,"A",1/3,dict_list)
            paths=allPath(sequence,index,path,"G",1/3,dict_list)
            paths=allPath(sequence,index,path,"C",1/3,dict_list)
        elif nuc=="N":
            paths=allPath(sequence,index,path,"A",0.25,dict_list)
            paths=allPath(sequence,index,path,"G",0.25,dict_list)
            paths=allPath(sequence,index,path,"C",0.25,dict_list)
            paths=allPath(sequence,index,path,"U",0.25,dict_list)
    if index==len(sequence)-1:
        #print("Return: ",paths)
        return paths


def calculateCost(nuc):
    if nuc in ["R","M","S"]:
        return 0.5
    elif nuc in ["V"]:
        return 1/3
    elif nuc in ["N"]:
        return 1/4
    else:
        return 1

def path_based(sequence):
    dict_list=[]
    for i in range (len(sequence)):
        allPath(sequence, i, "", sequence[i], calculateCost(sequence[i]),dict_list)
    paths={}
    for item in dict_list:
        key=list(item.keys())[0]
        if key in paths.keys():
            paths[key]+=item[key]
        else:
            paths[key]=item[key]
    return paths


def cosSimPath(seq1set,seq2set):
    dot=0
    multA=0
    multB=0
    for nuc in seq1set.keys():
        if nuc in seq2set.keys():
            dot=dot+(seq1set.get(nuc))*(seq2set.get(nuc))
            multA=multA+(seq1set.get(nuc))**2
            multB=multB+(seq2set.get(nuc))**2
        else:
            multA=multA+(seq1set.get(nuc))**2
    for nuc3 in seq2set.keys():
        if nuc3 not in seq1set.keys():
            multB=multB+(seq2set.get(nuc3))**2
    cosineSim=dot/(math.sqrt(multA)*math.sqrt(multB))
    return cosineSim

def PCCPath(seq1set,seq2set):
    dot=0
    multA=0
    multB=0
    sequence1=set(seq1set.keys())
    sequence2=set(seq2set.keys())
    length=len(sequence1.union(sequence2))
    seq1list=seq1set.values()
    seq1bar=sum(seq1list)/length
    seq2list=seq2set.values()
    seq2bar=sum(seq2list)/length
    for nuc in seq1set.keys():
        if nuc in seq2set.keys():
            dot=dot+(seq1set.get(nuc)-seq1bar)*(seq2set.get(nuc)-seq2bar)
            multA=multA+(seq1set.get(nuc)-seq1bar)**2
            multB=multB+(seq2set.get(nuc)-seq2bar)**2
        else:
            multA=multA+(seq1set.get(nuc)-seq1bar)**2
    for nuc3 in seq2set.keys():
        if nuc3 not in seq1set.keys():
            multB=multB+(seq2set.get(nuc3)-seq2bar)**2
    PCCSim=dot/(math.sqrt(multA)*math.sqrt(multB))
    return PCCSim
