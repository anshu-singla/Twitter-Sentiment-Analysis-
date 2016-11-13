import sys
import nltk
import csv
import re
import nltk.metrics
import itertools
import collections
import nltk.classify.util
from prepare import *
from collections import defaultdict


def main():
	pos_tweets=[]
    neg_tweets=[]
    pos_test=[]
    neg_test=[]
	acronymDict,stopWords,emoticonsDict = loadDictionary()
    #print(acronymDict)
    #print(stopWords)
    #print(emoticonsDict)
    with open('newsent.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            if line['sentiment']=="Positive":
                words=re.sub('[^A-Za-z0-9]+', ' ', line['text'])
                pos_tweets.append(words)
            if line['sentiment']=="Negative":
                words=re.sub('[^A-Za-z0-9]+', ' ', line['text'])
                neg_tweets.append(words)
    #f=open(sys.argv[1],'r')
    #f.close()
    with open('newtest.csv') as tcsvfile:
        reader = csv.DictReader(tcsvfile)
        for line in reader:
            if line['sentiment']=="Positive":
                words=re.sub('[^A-Za-z0-9]+', ' ', line['text'])
                pos_test.append(words)
            if line['sentiment']=="Negative":
                words=re.sub('[^A-Za-z0-9]+', ' ', line['text'])
                neg_test.append(words)
    #print(pos_tweets[:6])
    
if __name__ == "__main__":                                                                              
    main()