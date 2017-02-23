# -*- coding: utf-8 -*-

from gensim.models import word2vec
import numpy

# Method used to implement the MVME algorithm
def mvme(t1,t2):
    # Initialization - Load the word2vec vectors pre-trained
    model = word2vec.Word2Vec.load('modelWord2Vec_like');
    #if model is not None:
        #print('Model loaded .. .. ');
    #t1Tokens = preprocess.preprocess(t1);
    #t2Tokens = preprocess.preprocess(t2);
    t1Tokens = t1[0];
    t2Tokens = t2[0];
    n = len(t1Tokens);
    m = len(t2Tokens);
    #print('MVME',t1Tokens,t2Tokens);
    # Calculate the Distance matrix
    mat = [[0.0 for x in range(n)] for x in range(m)];
    for i in range(n):
        u = t1Tokens[i];
        for j in range(m):
            v = t2Tokens[j];
            try:
                mat[j][i] = model.similarity(u,v);
            except KeyError:
                mat[j][i] = 0;
            except AttributeError:
                print('Error')
                mat[j][i] = 0;
    #print('Calculating the similarity');            
    # Get the similarity value
    sim = 0.0;
    #print(mat);
    mat = numpy.asarray(mat);
    count = 0
    # Calculate the similarity between t1 and t2
    while mat.size:
        maxValue = -100.0;
        for x in range(n-count):
            for y in range(m-count):
                if mat[y][x] > maxValue:
                    row = y;
                    col = x;
                    maxValue = mat[y][x];
        sim += mat[row][col];
        mat = numpy.delete(mat, (row), axis=0);
        mat = numpy.delete(mat, (col), axis=1);
        count += 1;
         
    #print(sim);
    return sim;
    
# Checks if the similarity matrix has non zero values or not
def isMatEmpty(mat):
    print('Empty');
    for x in range(len(mat)):
        for y in range(len(mat[x])):
            if mat[x][y] == 0.0:
                continue;
            else:
                return False;
    return True;

#t1 = [(['I', 'think']),2];
#t2 = [(["can't", 'admit', 'when']),2];    
#print(mvme(t2,t2));
