from main import represent
import numpy as np
from numpy import dot
from numpy.linalg import norm
import scipy.stats as sci

#vector based similarity measures
# tag based
def cosineSim(seq1,seq2):
    seq1vec=np.array(represent(seq1)[1])
    seq2vec=np.array(represent(seq2)[1])

    cosineSim = dot(seq1vec, seq2vec)/(norm(seq1vec)*norm(seq2vec))
    return cosineSim


def PCC(seq1,seq2):
    seq1vec=np.array(represent(seq1)[1])
    seq2vec=np.array(represent(seq2)[1])

    return abs(sci.pearsonr(seq1vec,seq2vec)[0])
