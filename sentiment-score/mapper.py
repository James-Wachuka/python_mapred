# -*- coding: utf-8 -*-
""" This program is used for scoring  sentiments from different reviews and it 
can be implemented on hadoop mapreduce framework using the hadoop-streaming.jar"""

# This is the mapper code for our mapreduce job
import sys
import hashlib
positive_words = open('opt/positivewords/positive-words.txt').read().split('\n')
negative_words = open('opt/negativewords/negative-words.txt').read().split('\n')
def sentiment_score(text, pos_list, neg_list):
    positive_score = 0
    negative_score = 0
    for w in text.split('\t'):
        if w in pos_list:
            positive_score+=1
        if w in neg_list: 
            negative_score+=1
    return positive_score - negative_score
for l in sys.stdin:
    
    # Trailing and Leading white space is removed
    l = l.strip()
    #Convert to lower case
    l = l.lower()
 #Getting the sentiment score
    score = sentiment_score(l, positive_words, negative_words)
 #Hashing the review to use it as a string
    hash_object = hashlib.md5("l".encode('utf-8'))
 # Key Value pair is outputted
    print ('%s\t%s' % (hash_object.hexdigest(), score))