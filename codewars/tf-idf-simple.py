
import re
from string import punctuation
from collections import defaultdict, Counter

def tokenize(doc, total_word_freq=None):

    doc = ''.join(i.lower() for i in doc if i not in punctuation)
    words = re.split('\s+', doc)
    total_word_freq = Counter(words)
    return total_word_freq

test1 = 'I am well, I know'
print tokenize(test1)

oye('token')

'''
    corpus = ["I am well, I know","I wonder!"]
    returns a term frequency dict for corpus {'i':2,'am':1,'well':1,'know':1,'wonder':1}
'''


def create_term_dict_for_corpus(corpus, corpus_doc_dicts=[]):
    total_word_freq = Counter()
    for doc in corpus:
        corpus_doc_dicts.append(tokenize(doc))
        total_word_freq +=  tokenize(doc)
    return total_word_freq, corpus_doc_dicts


def tfidf(term, row_index, corpus_doc_dicts, total_word_freq):
    '''Formula
    TF:  word出现次数/文章所有单词数
    IDF: Inverse Document Frequency, 加权
    IDF(t) = log_e(Total number of documents / Number of documents with term t in it).

    '''
    from math import log
    # term
    term_occurence = corpus_doc_dicts[row_index][term]
    total_number_of_docs = len(corpus_doc_dicts)
    number_doc_with_term = len([ doc for doc in corpus_doc_dicts if term in doc])
    tf = term_occurence / float(total_number_of_docs)
    idf_t = log(total_number_of_docs/float(number_doc_with_term), 2)
    return tf * idf_t



corpus = ["I am well, I know",
          "I wonder!",
          "have you ever thought",
          "oh my my",
          "I'm so excited for you"]
total_word_freq, corpus_doc_dicts = create_term_dict_for_corpus(corpus)
print tfidf('wonder', 1, corpus_doc_dicts, total_word_freq)

#


# def idf(term,tot_numdocs, total_word_freq):
#   idf =  math.log(tot_numdocs/total_word_freq[term],2)
#   return idf


# def tfidf(term,row_index,corpus_doc_dicts ,total_word_freq):
#   _tf = tf(term,corpus_doc_dicts[row_index],len(corpus_doc_dicts))
#   _idf = idf(term,len(corpus_doc_dicts),total_word_freq)
#   tfidf = _tf * _idf
#   return tfidf
