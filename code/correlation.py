from scipy import stats
import numpy as np
from numpy import genfromtxt
import os

'''
path = '/opt/PhD/Work/StopWords/pos/Corpus/Custom/'
for d in os.listdir(path):
    for f in os.listdir(path + d):
        if f.find('lemma') == -1:
            corpus = d
            data = genfromtxt(path + d + '/' + f, delimiter=',', dtype = None, encoding = 'utf-8')
            rank = list()
            pos = list()

            #i = 1
            for tuple_item in data:
                if tuple_item[2] == "NN" or tuple_item[2]=="NNP" or tuple_item[2]=="NNPC":
                    label = 1
                else:
                    label = 0
                rank.append(tuple_item[1])
                pos.append(label)
                #i += 1



            rank = np.array(rank)
            pos = np.array(pos)
            print(len(rank), len(pos))
            file = open('noun_correlation.txt', 'a')
            file.write(corpus + ',' + str(stats.pointbiserialr(pos, rank)) + '\n')
            file.close()
'''
data = genfromtxt('/opt/PhD/Work/StopWords/pos/Corpus/Subtitles/lemma_freq.csv', delimiter=',', dtype = None, encoding = 'utf-8')
rank = list()
pos = list()

i = 1
for tuple_item in data:
    if tuple_item[2] == "VM":
        label = 1
    else:
        label = 0
    rank.append(i)
    pos.append(label)
    i += 1

corpus = 'custom'

rank = np.array(rank)
pos = np.array(pos)
print(len(rank), len(pos))
file = open('subtitles/verb_lemma_correlation.txt', 'a')
file.write(corpus + ',' + str(stats.pointbiserialr(pos, rank)) + '\n')
file.close()
