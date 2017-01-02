# -*- coding: utf-8 -*-
"""
@author: Sheng Liu
File used to preprocess the tweets and make them ready for classification 
using word2vec word embedding
"""
from nltk.tokenize import TweetTokenizer
import string

# Removes all the hash tags from the tweet
def removeTargetWordandHashTags(word,tweet):
    newList = [];
    for i in range(len(tweet)):
        x = tweet[i];
        if x[0] != '#':
            newList.append(x);
    return newList;

# Changes all number tokens to a standard number 2
def changeNumberToken(tweet):
    newList = [];
    for token in tweet:
        if token.isnumeric():
            newList.append('2');
        else:
            newList.append(token);
    return newList;

# Lowercases all tokens expect if the token consist of all words uppercase
def alignCase(tweet):
    newList = [];
    for token in tweet:
        if token.isupper():
            newList.append(token);
        else:
            newList.append(token.lower());
    return newList;
        
# Removes all the mentioned usernames
def removeMentions(tweet):
    for token in tweet:
        if token[0] == '@':
            tweet.remove(token);
    return tweet;
    
# Removes all the punctiations
def removePunctuations(tweet):
    newList = [];
    punctuations = string.punctuation;
    for token in tweet:
        if token[0] not in punctuations:
            newList.append(token);
    return newList;

# Preprocessing main method
def preprocess(line):
    x = line.split('\t');
    targetWord = x[0];
    tokenizer = TweetTokenizer();
    try:    
        tweet_v1 = tokenizer.tokenize(x[2]);
    except IndexError:
        return None;
    tweet_v2 = removeTargetWordandHashTags(targetWord,tweet_v1);
    tweet_v3 = changeNumberToken(tweet_v2);
    tweet_v4 = alignCase(tweet_v3);
    tweet_v5 = removeMentions(tweet_v4);
    tweet_v6 = removePunctuations(tweet_v5);
    return (tweet_v6);
    
#sent = preprocess('mature	2	I think this was a mature decision we made. #Grateful');
#print(sent);