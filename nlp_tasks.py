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
        return []

    def calc_IDF(self, term):
        """Calculates Inverse Document Frequency (IDF)
        of given term in preprocessed corpus

        :param term: given term
        :type term:  string

        :return: IDF
        :rtype:  float
        """
        return 0.0

    def calc_BM25_score(self, index):
        """Calculates BM25 score
        for preprocessed question in preprocessed document

        :param index: index of document in preprocessed corpus
        :type index:  int

        :return: BM25
        :rtype:  float
        """
        return 0.0

    def find_top_matches(self, n):
        """Finds the top scoring documents
        for preprocessed question in corpus

        :param n: number of documents to find
        :type n:  int

        :return: top scoring original documents
        :rtype:  list[str]
        """
        return []

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == '__main__':
    import run_BM25
    run_BM25.main(sys.argv[1:])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# vim:set et sw=4 ts=4:
