# -*- coding: utf-8 -*-
"""
@author: Chinmay
File used to train the word2vec model and save it for later use
"""
from gensim.models import word2vec
import logging
import preprocess

# Train and Save the word2vec model
def trainWord2Vec(filename):
    # Read the file data for training
    file = open(filename,'r');
    count = 0;
    lines = [];
    while count < 339:
        try:
            line = (file.readline());
            if line is not '':
                lines.append(line);
                line = '';
        except UnicodeDecodeError:
            continue;
        count += 1;
    trainData = [];
    #print(len(lines));
    #print(lines);
    file = open('text.txt','w');
    file.writelines(lines);
    file.close();
    targetWord = (lines[0].split('\t'))[0];
    # Preprocess the data for wrod2vec model    
    for line in lines:
        sent = preprocess.preprocess(line);
        if sent is not None:
            trainData.append(sent);
    # Log statement for training progress monitoring
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO);
    # Train the model
    num_features = 100;
    min_word_count = 1;
    num_workers = 4;
    context = 10;
    downsampling = 1e-3;
    model = word2vec.Word2Vec(trainData, workers=num_workers, size=num_features, min_count = min_word_count, window = context, sample = downsampling);
    model.init_sims(replace=True);
    # Save the model    
    model_name = "modelWord2Vec_"+targetWord;
    model.save(model_name);
    # Print similarity of the target word
    print('Words that are most similar to',targetWord,'in the dataset');
    print('__________________________________________________________________');
    print(model.most_similar(targetWord));
    print('__________________________________________________________________');
    
# Method used for driving the vector training
def driver(trainData):
    # Added try except and returned 0 for in case of error
    # Loads the model
    trainWord2Vec(trainData);

# Call to the driver method
driver('Mature.train');
#driver('Joy.train');