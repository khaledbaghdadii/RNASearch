from set_based import jaccSim,dice,intersectSim
from vector_based import PCC,cosineSim
from all_path import jaccSimPath,path_based,diceSimPath,intersectSimPath,cosSimPath,PCCPath
import time
from EDmeasure import wagner_fischer
from corpus_return import seq_corpus

sequences=seq_corpus("replaced.fa")

def calculateTime(approach,model,set_measure,vector_measure):
    measure="Measure";
    if approach=="tag-based":
        if model=="set-based":
            if set_measure=="Jaccard":
                print("You are inside jacc")
                measure="Jaccard"
                return calculateJaccTag(),measure
            elif set_measure=="Dice":
                measure="Dice"
                print("You are inside dice")
                return calculateDiceTag(),measure
            elif set_measure=="Intersection":
                measure="Intersection"
                print("You are inside intersection")
                return calculateIntTag(),measure
        elif model=='vector-based':
            if vector_measure=="PCC":
                measure="PCC"
                print("You are inside PCC")
                return calculatePCCTag(),measure
            elif vector_measure=="Cosine":
                measure="Cosine"
                print("You are inside cosine")
                return calculateCosineTag(),measure
    if approach=='path-based':
        if model=='set-based':
            if set_measure=="Jaccard":
                measure="Jaccard"
                print("You are inside jacc")
                return calculateJaccPath(),measure
            elif set_measure=="Dice":
                measure="Dice"
                print("You are inside dice")
                return calculateDicePath(),measure
            elif set_measure=="Intersection":
                measure="Intersection"
                print("You are inside intersection")
                return calculateIntPath(),measure
        if model=='vector-based':
            if vector_measure=='Cosine':
                measure="Cosine"
                print("You are inside cosine")
                return calculateCosinePath(),measure
            if vector_measure=='PCC':
                measure="PCC"
                print("You are inside pcc")
                return calculatePCCPath(),measure

#TED based solution
def calculateWagner():
    stamps=[]
    start_time=time.process_time()
    for i in range(len(sequences)-1):
        #print(sequences[i])
        seq1=sequences[i]
        seq2=sequences[i+1]
        wagner_fischer(seq1,seq2)
        stamps.append(time.process_time()-start_time)
    end_time=time.time()
    return stamps

#tag based
#set based approach
#jacc
def calculateJaccTag():
    stamps=[]
    start_time=time.time()
    for i in range(len(sequences)-1):
        #print(sequences[i])
        seq1=sequences[i]
        seq2=sequences[i+1]
        jaccSim(seq1,seq2)
        stamps.append(time.time()-start_time)
    end_time=time.time()
    return stamps

#dice
def calculateDiceTag():
    stamps=[]
    start_time=time.time()
    for i in range(len(sequences)-1):
        #print(sequences[i])
        seq1=sequences[i]
        seq2=sequences[i+1]
        dice(seq1,seq2)
        stamps.append(time.time()-start_time)
    end_time=time.time()
    return stamps

#intersection
def calculateIntTag():
    stamps=[]
    start_time=time.time()
    for i in range(len(sequences)-1):
        #print(sequences[i])
        seq1=sequences[i]
        seq2=sequences[i+1]
        intersectSim(seq1,seq2)
        stamps.append(time.time()-start_time)
    end_time=time.time()
    return stamps


#vector based approach
#cosine
def calculateCosineTag():
    stamps=[]
    start_time=time.process_time()
    for i in range(len(sequences)-1):
        #print(sequences[i])
        seq1=sequences[i]
        seq2=sequences[i+1]
        cosineSim(seq1,seq2)
        stamps.append(time.process_time()-start_time)
    end_time=time.process_time()
    return stamps

#pcc
def calculatePCCTag():
    stamps=[]
    start_time=time.process_time()
    for i in range(len(sequences)-1):
        #print(sequences[i])
        seq1=sequences[i]
        seq2=sequences[i+1]
        PCC(seq1,seq2)
        stamps.append(time.process_time()-start_time)
    end_time=time.process_time()
    return stamps

#path based
#set based approach
#jacc
def calculateJaccPath():
    stamps=[]
    start_time=time.time()
    for i in range(len(sequences)-1):
        seq1=path_based(sequences[i])
        seq2=path_based(sequences[i+1])
        jaccSimPath(seq1,seq2)
        stamps.append(time.time()-start_time)
    end_time=time.time()
    return stamps

#dice
def calculateDicePath():
    stamps=[]
    start_time=time.time()
    for i in range(len(sequences)-1):
        seq1=path_based(sequences[i])
        seq2=path_based(sequences[i+1])
        diceSimPath(seq1,seq2)
        stamps.append(time.time()-start_time)
    end_time=time.time()
    return stamps

#intersection
def calculateIntPath():
    stamps=[]
    start_time=time.time()
    for i in range(len(sequences)-1):
        seq1=path_based(sequences[i])
        seq2=path_based(sequences[i+1])
        intersectSimPath(seq1,seq2)
        stamps.append(time.time()-start_time)
    end_time=time.time()
    return stamps


#vector based approach
#cosine
def calculateCosinePath():
    stamps=[]
    start_time=time.process_time()
    for i in range(len(sequences)-1):
        seq1=path_based(sequences[i])
        seq2=path_based(sequences[i+1])
        cosSimPath(seq1,seq2)
        stamps.append(time.process_time()-start_time)
    end_time=time.process_time()
    return stamps

#pcc
def calculatePCCPath():
    stamps=[]
    start_time=time.process_time()
    for i in range(len(sequences)-1):
        seq1=path_based(sequences[i])
        seq2=path_based(sequences[i+1])
        PCCPath(seq1,seq2)
        stamps.append(time.process_time()-start_time)
    end_time=time.process_time()
    return stamps
