# -*- coding: utf-8 -*-
'''
Created on May , 2015
@author: stevey
http://www.codewars.com/kata/554ea533527c2ad10d000018/train/python
'''

import numpy as np
np.random.seed(1428)
import pandas as pd
from matplotlib import style
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
import os, sys
from sklearn import datasets
style.use('ggplot')

note = '''

TF-IDF stands for term frequency-inverse document frequency.
It is also used with the weighted method -- TF-IDF weight.

The weight is a statistical measure used to evaluate how important a word a word is to a document of corpus.
The importance increases proportionally to the number of times a word appears in the document but is offset by the frequency of the word in the corpus.  Variations of the tf-idf weighting scheme are often used by search engines as a central tool in scoring and ranking a document's relevance givena user query.


------------------------------------------------------------------------
The Formular for calculating TF*IDF is:
词频
TF: Term Frequency, which measures how frequently a term occurs in a document. Since every document is different in length, it is possible that a term would appear much more times in long documents than shorter ones. Thus, the term frequency is often divided by the document length (aka. the total number of terms in the document) as a way of normalization:

TF(t) = (Number of times term t appears in a document) / (Total number of terms in the document).
TF(t)  文档中t出现次数/文档一共的单词数

IDF: Inverse Document Frequency, which measures how important a term is. While computing TF, all terms are considered equally important. However it is known that certain terms, such as "is", "of", and "that", may appear a lot of times but have little importance. Thus we need to weigh down the frequent terms while scale up the rare ones, by computing the following:

IDF(t) = log_e(Total number of documents / Number of documents with term t in it).

Implement TF-IDF. For this, you may also need to implement a data structure to contain a corpus of documents. You'll also a way to tokenize each document to supoprt TF, for this problem, it's ok to split on spaces, lower case the words, and remove punctuations.
'''



import re
import math

'''
    doc = "I am well, I know"
    returns a term frequency dict for doc {'i':2,'am':1,'well':1,'know':1}
'''


def tokenize(doc, total_word_freq):

    doc_dics = {} # term frequencies of the document
    words = re.split('\W+', doc)
    for word in words:
        word = word.lower().strip()
        if(len(word)<1): continue
        if word in doc_dics:
            doc_dics[word] +=1
        else: doc_dics[word] = 1
        if word in total_word_freq:
            total_word_freq[word] += 1
        else: total_word_freq[word] =1
    return doc_dics

# corpus like
'''
    corpus = ["I am well, I know","I wonder!"]
    returns a term frequency dict for corpus {'i':2,'am':1,'well':1,'know':1,'wonder':1}
'''

def create_term_dict_for_corpus(corpus, corpus_doc_dicts=[]):
    total_word_freq={}
    corpus_as_tfs = []
    for x in range(0, len(corpus)):
        corpus_doc_dicts.append(tokenize(corpus[x],total_word_freq))
    return total_word_freq, corpus_doc_dicts

corpus = ["I am well, I know",
        "I wonder!",
        "have you ever thought",
        "oh my my",
        "I'm so excited for you"
        ]


total_word_freq, corpus_doc_dicts = create_term_dict_for_corpus(corpus)
from pprint import pprint
print '*'*58
pprint(sorted(total_word_freq.items(),key=lambda x: x[0]))
pprint(corpus_doc_dicts)


def tf(term,doc_dics,tot_numdocs):
  tf =  float(doc_dics[term])/float(tot_numdocs)
  return tf


from math import log
def idf(term, tot_numdocs, total_word_freq):
  idf =  math.log(tot_numdocs/total_word_freq[term], 2)
  return idf

def tfidf(term,row_index,corpus_doc_dicts ,total_word_freq):
  _tf = tf(term,corpus_doc_dicts[row_index],len(corpus_doc_dicts))
  _idf = idf(term,len(corpus_doc_dicts),total_word_freq)
  tfidf = _tf * _idf
  return tfidf


def tfidf(term, row_index, corpus_doc_dicts, total_word_freq):
    tf = total_word_freq[term] / float( sum(total_word_freq.values() ))
    term_docs = sum([1 for doc in corpus_doc_dicts if term in doc])
    total_docs = len(corpus_doc_dicts)
    return tf * log(total_docs/float(term_docs), 2)

print tfidf("wonder",1,corpus_doc_dicts,total_word_freq)