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
from nltk.stem import PorterStemmer

def get_words_in_tweets(tweets):
   	all_words = []
   	for (words, sentiment) in tweets:
   		all_words.extend(words)
   	return all_words



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
    
    #Tokenizing
    tok_postweets=[]
    tok_postest=[]
    tok_negtweets=[]
    tok_negtest=[]
    for (words) in pos_tweets:
    	words_filtered = [e.lower() for e in words.split()]
    	tok_postweets.append((words_filtered))
    for (words) in neg_tweets:
    	words_filtered = [e.lower() for e in words.split()]
    	tok_negtweets.append((words_filtered))
    for (words) in pos_test:
    	words_filtered = [e.lower() for e in words.split()]
    	tok_postest.append((words_filtered))
    for (words) in neg_test:
    	words_filtered = [e.lower() for e in words.split()]
    	tok_negtest.append((words_filtered)) 
    #print(tok_postweets[:1])
    #print(tok_negtweets[:1])
    
        #Stopwords Removal
    

    filter_tweetspos=[]
    filter_tweetsneg=[]
    filter_testpos=[]
    filter_testneg=[]
    stopWords=defaultdict(int)
    stopword=[]
    f=open("stopWords.txt", "r")
    for line in f:
        if line:
            line=line.strip(specialChar).lower()
            stopword.append(line)
    f.close()
    #print(stopword)
    for sent in tok_postweets:
        filtered_sentence=[]
        for w in sent:
            #print(w)
            if w not in stopword:
                #print(w)
                if "http" not in w:
                    filtered_sentence.append(w)
        filter_tweetspos.append(filtered_sentence)
    for sent in tok_negtweets:
        filtered_sentence=[]
        for w in sent:
            #print(w)
            if w not in stopword:
                #print(w)
                if "http" not in w:
                    filtered_sentence.append(w)
        filter_tweetsneg.append(filtered_sentence)
    for sent in tok_postest:
        filtered_sentence=[]
        for w in sent:
            #print(w)
            if w not in stopword:
                if "http" not in w:
                #print(w)
                    filtered_sentence.append(w)
        filter_testpos.append(filtered_sentence)
    for sent in tok_negtest:
        filtered_sentence=[]
        for w in sent:
            #print(w)
            if w not in stopword:
                if "http" not in w:
                #print(w)
                    filtered_sentence.append(w)
        filter_testneg.append(filtered_sentence) 
    #print(filter_tweetspos[:1])

     #Stemming
    pos_tweets=[]
    neg_tweets=[]
    pos_test=[]
    neg_test=[]
    for sent in filter_tweetspos:
        filtered_sentence=[]
        for w in sent:
            filtered_sentence.append(ps.stem(w))
        pos_tweets.append(filtered_sentence)
    for sent in filter_tweetsneg:
        filtered_sentence=[]
        for w in sent:
            filtered_sentence.append(ps.stem(w))
        neg_tweets.append(filtered_sentence)
    for sent in filter_testpos:
        filtered_sentence=[]
        for w in sent:
            filtered_sentence.append(ps.stem(w))
        pos_test.append(filtered_sentence)
    for sent in filter_testneg:
        filtered_sentence=[]
        for w in sent:
            filtered_sentence.append(ps.stem(w))
        neg_test.append(filtered_sentence) 
    #print(pos_tweets)

    for (words) in pos_tweets:
        #print(words)
        words= [e.lower() for e in words]
        tweets.append((words,'positive'))
    for (words) in neg_tweets:
        words= [e.lower() for e in words]
        tweets.append((words,'negative'))
    for (words) in pos_test:
        words= [e.lower() for e in words]
        test.append((words,'positive'))
    for (words) in neg_test:
        words= [e.lower() for e in words]
        test.append((words,'negative'))
    #print(tweets)

    word_features = get_word_features(get_words_in_tweets(tweets))
    
if __name__ == "__main__":                                                                              
    main()