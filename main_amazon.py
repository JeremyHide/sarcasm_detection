# -*- coding: utf-8 -*-
"""
@author: Sheng Liu
File used to run the classification model
"""
from nltk.classify import SklearnClassifier
from sklearn.svm import SVC
from sklearn import cross_validation
import project
import preprocess
import numpy
import nltk
import random

def writeFile(matrix):
    file = open('matrix.csv','w');
    line = '';
    for x in matrix:
        line += str(x) + ",";
    file.write(line);
    file.close();

def classifyFeatures(feature):
    # Define folds for cross validation
    kf = cross_validation.KFold(len(feature), n_folds=5, shuffle=False);
    featuresetsUpdatedArray = numpy.array(feature);
    max2 = 0;
    SVMmodel = SklearnClassifier(SVC());
    for x,y in kf:
        train_set_fold = featuresetsUpdatedArray[x];
        test_set_fold = featuresetsUpdatedArray[y];
        train_set = list(train_set_fold);
        test_set = list(test_set_fold);
        # SV Classifier
        classifier2 = SklearnClassifier(SVC()).train(train_set);
        accuracy2 = nltk.classify.accuracy(classifier2,test_set)*100;
        # Use the best model       
        if accuracy2 > max2:
            SVMmodel = classifier2;
    return SVMmodel;

# Main method
def main():
    # Read the traininf file
    file = open('like.train','r');
    count = 0;
    lines = [];
    while count < 476:
        try:
            line = (file.readline());
            if line is not '':
                lines.append(line);
                line = '';
        except UnicodeDecodeError:
            continue;
        count += 1;
    trainData = [];
    targetWord = (lines[0].split('\t'))[0];
    print('\nTarget Word is ',targetWord);
    # Preprocess the data    
    for line in lines:
        x = line.split("\t");
        try:
            trainData.append((preprocess.preprocess(line),x[1]));
        except IndexError:
            print();
    m = int(len(trainData)*0.8);
    random.seed(2);
    random.shuffle(trainData);
    testData = trainData[m:];
    data = trainData[:m];
    trainData = data;
    print('\nPreprocessing Complete.. ..');
    print('\nLoading vectors pre-trained on Training data');
    n = len(trainData);
    print(n);
    print('\nComputing Kernel Matirx');
    featureList = [];
    kMatrix = [[0 for x in range(n)] for x in range(n)];
    for i in range(n):
        print(i);
        iDictionary = {};
        for j in range(n):
            kMatrix[i][j] = project.mvme(trainData[i],trainData[j]);
            iDictionary[j] = kMatrix[i][j];
        featureList.append([iDictionary,(trainData[i])[1]]);
    # Write the kernel matrix to CSV file
    writeFile(kMatrix);
    print('\nKernal Matrix computed and saved in csv file');
    # Train the classification model
    print('\nTraining the SVM model using the kernel matrix');
    classifier = classifyFeatures(featureList);
    print('\n\n');
    n  = len(testData);
    featureList = [];
    kMatrix = [[0 for x in range(n)] for x in range(n)];
    for i in range(n):
        print(i);
        iDictionary = {};
        for j in range(n):
            kMatrix[i][j] = project.mvme(testData[i],testData[j]);
            iDictionary[j] = kMatrix[i][j];
        featureList.append([iDictionary,(testData[i])[1]]);
    # Test the classification model
    print('Classification Accuracy is ',end='');
    print(nltk.classify.accuracy(classifier,featureList)*100);
        
main()