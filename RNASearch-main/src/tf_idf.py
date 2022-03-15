import math

def idf_per_word(list,path):
    count=0;
    for seq in list:
        if path in seq.keys():
            count+=1
    if count==0:
        return 0
    else:
        return math.log10(len(list)/count)


def idf(list,sequence):
    idf_dict={}
    for path in sequence.keys():
        idf_dict[path]=(idf_per_word(list,path))
    return idf_dict

#return tf_idf value for the sequence (not all corpus)
def tf_idf(list,sequence):
    tf_idf_dict={}
    for path in sequence.keys():
        weight=sequence[path]
        tf_idf_value=weight*idf_per_word(list,path)
        tf_idf_dict[path]=(tf_idf_value)
    return tf_idf_dict

