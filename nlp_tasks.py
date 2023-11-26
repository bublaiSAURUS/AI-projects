#!/usr/bin/env python3
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""Sample code for Comp24011 BM25 lab solution

NB: The default code in non-functional; it simply avoids type errors
"""

__author__ = "USERNAME"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# we recommend you consider these Python modules while developing your code
import math
import re
import string
import sys

from nlp_tasks_base import NLPTasksBase

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class NLPTasks(NLPTasksBase):
    def __init__(self, *params):
        """Initialise instance by passing arguments to super class"""
        super().__init__(*params)

    def preprocess(self, texts):
        """Implements text preprocessing

        :param texts: text lines
        :type texts:  list

        :return: preprocessed lines
        :rtype:  list[str]
        """
        ans = []
        for text in texts:
            ans.append(self.preprocessLine(text))
        #print(ans)
        return ans
    
    def preprocessLine(self, texts):
        line = texts
        punctuation_removed = re.findall(r'\b\w+\b', line) 
        words_to_lowerCase = [word.lower() for word in punctuation_removed]
        #stop_words = []
        with open('stopwords_en.txt', 'r') as file:
            stop_words = set(file.read().split())
        filtered_list = [word for word in words_to_lowerCase if word not in stop_words]
        if self.stemmer != None:
            filtered_list = self.stemmer.stemWords(filtered_list)
        joined = ' '.join(filtered_list)
        #print(joined)
        return joined

    def calc_IDF(self, term):
        """Calculates Inverse Document Frequency (IDF)
        of given term in preprocessed corpus

        :param term: given term
        :type term:  string

        :return: IDF
        :rtype:  float
        """
        df = 0
        #print(self.preprocessed_corpus)
        for i in self.preprocessed_corpus:
            #print(i)
            l = i.split()
            if term in l:
                df+=1
        N = len(self.preprocessed_corpus)
        IDF = math.log10((N-df+0.5)/(df+0.5))
        return IDF

    def calc_BM25_score(self, index):
        """Calculates BM25 score
        for preprocessed question in preprocessed document

        :param index: index of document in preprocessed corpus
        :type index:  int

        :return: BM25
        :rtype:  float
        """
        d = self.preprocessed_corpus[index]
        q = self.preprocessed_question
        d_length = len(d.split())
        #print(d_length)
        bm25_score = 0
        #print(q)
        #print(len(q))
        #print(d)
        sum = 0
        for w in self.preprocessed_corpus:
            #print(w)
            #print(w.split())
            #print(len(w.split()))
            sum = sum + len(w.split())
        #print(sum)
        #print(len(self.preprocessed_corpus))
        L = sum/len(self.preprocessed_corpus)
        #print(L)
        for qi in q.split():
            #print(qi)
            tf_qi = d.split().count(qi)
            #print(tf_qi)
            idf = self.get_IDF(qi)
            numerator = (tf_qi)*3
            denominator = (tf_qi)+2*(0.25+(0.75*(d_length/L)))
            bm25_score += idf*(numerator/denominator)
        return bm25_score

    def find_top_matches(self, n):
        """Finds the top scoring documents
        for preprocessed question in corpus

        :param n: number of documents to find
        :type n:  int

        :return: top scoring original documents
        :rtype:  list[str]
        """
        corpus = self.preprocessed_corpus
        question = self.preprocessed_question
        ans = []
        scores = [self.get_BM25_score(question, i) for i in range(len(corpus))]
        ranked_docs = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
        ans = []
        for item in ranked_docs:
            #ans.append(self.original_corpus(item[0]))
            ans.append(self.original_corpus[item[0]])
        return ans[:n]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == '__main__':
    import run_BM25
    run_BM25.main(sys.argv[1:])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# vim:set et sw=4 ts=4:
