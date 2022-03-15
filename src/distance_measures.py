import scipy
import numpy as np
from main import represent
import time

#You can use jacc sim to get jacc distance without computation
#jaccdis = 1- jaccSim
def jaccardSim(seq1,seq2):
    seq1vec=np.array(represent(seq1)[1])
    seq2vec=np.array(represent(seq2)[1])

    return (1-scipy.spatial.distance.jaccard(seq1vec,seq2vec))
#jaccardSim("CUA","A")

def euclidDis(seq1,seq2):
    seq1vec=np.array(represent(seq1)[1])
    seq2vec=np.array(represent(seq2)[1])

    return scipy.spatial.distance.euclidean(seq1vec,seq2vec)

#euclidDis("CUA","A")

def manhattanDis(seq1,seq2):
    seq1vec=np.array(represent(seq1)[1])
    seq2vec=np.array(represent(seq2)[1])

    return scipy.spatial.distance.cityblock(seq1vec,seq2vec)
#manhattanDis("CUA","A")

#You can use dice sim to get dice distance without computation
#dicDis=1-simdice

def diceDis(seq1,seq2):
    start_time=time.time()
    seq1vec=np.array(represent(seq1)[1])
    seq2vec=np.array(represent(seq2)[1])
    end_time=time.time()
    return scipy.spatial.distance.dice(seq1vec,seq2vec),(end_time-start_time)
#diceDis("CUA","A")