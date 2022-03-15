from Bio.SeqIO.FastaIO import FastaIterator
from tf_idf import tf_idf,idf
from all_path import path_based

def fasta_reader(filename):

    with open(filename) as handle:
        for record in FastaIterator(handle):
            yield record

#returns the sequences as is
def seq_corpus(file):
    counter = 0
    sequences=[]
    for entry in fasta_reader(file):
        counter=counter+1;
        sequences.append(str(entry.seq))
        if counter==100:
            break
    return sequences

#returns path based corpus same as tf
def path_based_corpus(file):
    corpus=[]
    sequences=seq_corpus(file)
    for seq in sequences:
        corpus.append(path_based(seq))
    return corpus

#returns tf_idf corpus
def tf_idf_corpus(file):
    corpus_tf_idf=[]
    corpus_path_based=path_based_corpus(file)
    for seq in corpus_path_based:
        corpus_tf_idf.append(tf_idf(corpus_path_based,seq))
    return corpus_tf_idf

def idf_corpus(file):
    corpus_idf=[]
    corpus_path_based=path_based_corpus(file)
    for seq in corpus_path_based:
        corpus_idf.append(idf(corpus_path_based,seq))
    return corpus_idf