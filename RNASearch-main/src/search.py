from tf_idf import tf_idf
from all_path import jaccSimPath,diceSimPath,PCCPath,cosSimPath
from EDmeasure import wagner_fischer
from corpus_return import seq_corpus,path_based_corpus,tf_idf_corpus, idf_corpus, idf
from all_path import path_based
import time

def getCorpusesReady(filename):
    global sequences,corpus_path_based,corpus_tf_idf,corpus_idf
    sequences=seq_corpus(filename)
    corpus_path_based=path_based_corpus(filename)
    corpus_tf_idf=tf_idf_corpus(filename)
    corpus_idf=idf_corpus(filename)




def search(query,type_of_search, sim_measure):
    start = time.time()
    result=[]
    PR,R=0,0
    if type_of_search=="ED":
        result,pool= search_ED(query,sequences)
        R,PR=recall_precision(pool,path_based(query))
    elif type_of_search=="TF-IDF":
        query_paths=path_based(query)
        query_tf_idf=tf_idf(corpus_path_based,query_paths)
        result,pool= search_tf_idf(corpus_tf_idf,query_tf_idf,sequences,sim_measure)
        R,PR=recall_precision(pool,query_tf_idf)
    elif type_of_search=="TF":
        query_paths=path_based(query)
        result,pool= search_tf(corpus_path_based,query_paths,sequences,sim_measure)
        R,PR=recall_precision(pool,query_paths)
    elif type_of_search=="IDF":
        query_paths=path_based(query)
        query_idf=idf(corpus_idf,query_paths)
        result,pool= search_idf(corpus_idf,query_idf,sequences,sim_measure)
        R,PR=recall_precision(pool,query_idf)
    end = time.time()
    time_total=(end-start)

    return result,R,PR,time_total

def search_tf(corpus_pb, query_paths, sequences,sim_measure):
    sim_list=[]
    for i,seq in enumerate(corpus_pb):
        if sim_measure=='Jaccard':
            sim=jaccSimPath(seq,query_paths)
            sim_list.append(sim)
        elif sim_measure=='Dice':
            sim=diceSimPath(seq,query_paths)
            sim_list.append(sim)
        elif sim_measure=='PCC':
            sim=PCCPath(seq,query_paths)
            sim_list.append(sim)
        elif sim_measure=='Cosine':
            sim=cosSimPath(seq,query_paths)
            sim_list.append(sim)
    max1index,max1,max2index,max2,max3index,max3=top3Sim(sim_list)
    result_seq={}
    result_pb=[]
    result_pb.append(corpus_pb[max1index])
    result_pb.append(corpus_pb[max2index])
    result_pb.append(corpus_pb[max3index])
    seq1=sequences[max1index]
    seq1sim=max1
    seq2=sequences[max2index]
    seq2sim=max2
    seq3=sequences[max3index]
    seq3sim=max3
    result_seq[seq1]=seq1sim
    result_seq[seq2]=seq2sim
    result_seq[seq3]=seq3sim
    return result_seq,result_pb

def search_tf_idf(corpus_tf_idf, query_tf_idf, sequences,sim_measure):
    sim_list=[]
    for i,seq in enumerate(corpus_tf_idf):
        if sim_measure=='Jaccard':
            sim=jaccSimPath(seq,query_tf_idf)
            sim_list.append(sim)
        elif sim_measure=='Dice':
            sim=diceSimPath(seq,query_tf_idf)
            sim_list.append(sim)
        elif sim_measure=='PCC':
            sim=PCCPath(seq,query_tf_idf)
            sim_list.append(sim)
        elif sim_measure=='Cosine':
            sim=cosSimPath(seq,query_tf_idf)
            sim_list.append(sim)
    max1index,max1,max2index,max2,max3index,max3=top3Sim(sim_list)
    result_seq={}
    result_pb=[]
    result_pb.append(corpus_tf_idf[max1index])
    result_pb.append(corpus_tf_idf[max2index])
    result_pb.append(corpus_tf_idf[max3index])
    seq1=sequences[max1index]
    seq1sim=max1
    seq2=sequences[max2index]
    seq2sim=max2
    seq3=sequences[max3index]
    seq3sim=max3
    result_seq[seq1]=seq1sim
    result_seq[seq2]=seq2sim
    result_seq[seq3]=seq3sim
    return result_seq,result_pb

def search_idf(corpus_idf, query_idf, sequences,sim_measure):
    sim_list=[]
    for i,seq in enumerate(corpus_idf):
        if sim_measure=='Jaccard':
            sim=jaccSimPath(seq,query_idf)
            sim_list.append(sim)
        elif sim_measure=='Dice':
            sim=diceSimPath(seq,query_idf)
            sim_list.append(sim)
        elif sim_measure=='PCC':
            sim=PCCPath(seq,query_idf)
            sim_list.append(sim)
        elif sim_measure=='Cosine':
            sim=cosSimPath(seq,query_idf)
            sim_list.append(sim)
    max1index,max1,max2index,max2,max3index,max3=top3Sim(sim_list)
    result_seq={}
    result_pb=[]
    result_pb.append(corpus_idf[max1index])
    result_pb.append(corpus_idf[max2index])
    result_pb.append(corpus_idf[max3index])
    seq1=sequences[max1index]
    seq1sim=max1
    seq2=sequences[max2index]
    seq2sim=max2
    seq3=sequences[max3index]
    seq3sim=max3
    result_seq[seq1]=seq1sim
    result_seq[seq2]=seq2sim
    result_seq[seq3]=seq3sim
    return result_seq,result_pb

def top3Sim(list_of_sim):
    max1,max2,max3=0,0,0	#Initializing max1,max2,max3
    max1index,max2index,max3index=0,0,0
    for index,i in enumerate(list_of_sim):	#Iterations
        if i>max1:	#Comparison for max1
            max3=max2
            max3index=max2index
            max2=max1
            max2index=max1index
            max1=i
            max1index=index
        elif i>max2:	#comparison for max2
            max3=max2
            max3index=max2index
            max2=i
            max2index=index
        elif i>max3:	#Comparison for max3
            max3=i
            max3index=index
    return max1index,max1,max2index,max2,max3index,max3

def search_ED(query_seq,sequences):
    sim_dict={}
    sim_list=[]
    result_pb=[]
    for i,seq in enumerate(sequences):
        sim=wagner_fischer(seq,query_seq)
        sim_dict[i]=sim
        sim_list.append(sim)
    max1index,max1,max2index,max2,max3index,max3=top3Sim(sim_list)
    result={}
    seq1=sequences[max1index]
    seq1sim=max1
    seq2=sequences[max2index]
    seq2sim=max2
    seq3=sequences[max3index]
    seq3sim=max3
    result[seq1]=seq1sim
    result[seq2]=seq2sim
    result[seq3]=seq3sim
    result_pb.append(path_based(seq1))
    result_pb.append(path_based(seq2))
    result_pb.append(path_based(seq3))
    return result,result_pb

# print(search(query,"ED"))
# print(search(query,"idf"))
# print(search(query,"tf"))
def recall_precision(pool,query):
    query_seq=list(query.keys())
    PR,R=0,0
    for result_seq in pool:
        PR_current,R_current=0,0
        pool_seq=list(result_seq.keys())  #returned paths
        set1=set(query_seq)
        set2=set(pool_seq)
        TP=len(set1.intersection(set2))
        FP=len(set2-set1)
        FN=len(set1-set2)
        PR_current=TP/(TP+FP)
        R_current=TP/(TP+FN)
        PR+=PR_current
        R+=R_current
    PR=PR/len(pool)
    R=R/len(pool)
    return R,PR


