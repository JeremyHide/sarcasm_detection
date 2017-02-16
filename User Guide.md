## Product Review Sarcasm Detection (LSSD problem)
- Sheng Liu shengliu [at] nyu [dot] edu
- New York University, NY, USA
## Table of Contents

### Project Abstract
In this modern age of social media, people find it convenient to voice their opinion through social media messages, blogs or post. Social media data has become an area of study in the fields of cognitive science, psychology, computational linguistics amongst various others. Sarcasm is a way of communication where the user hides the real meaning by using words in contrasting sense. Finding sarcasm in social media text can be challenging because it is natural to relate the sense of the word in its literal sense. Hence sarcasm detection can be viewed as word sense disambiguation task where the sense to be classified are sarcas- tic or literal. This is called as Literal/Sar- castic Sense Disambiguation (LSSD) prob- lem. This paper recreates the experiments performed by Ghosh and his colleagues us- ing the algorithm described by them in the same publication.


### Part 1: Dataset
Available corpus including annotations about whether a text is ironic or not has been published by Filatova (2012). Due to the limitted size of product reviews dataset, we adopted the twitter corpus that Ghosh et. al. used to perform their experiments for the ‘Sarcastic or Not: Word Embeddings to Predict the Literal or Sarcastic Meaning of Words’. I used the same target words with Ghosh et. al. The following table is the description of some target words.

| Target Word | Twitter Corpus  | Amazon Review Corpus |
|:-----------:|:---------------:|:--------------------:|
|     like    |      18734      |          426         |
|     Joy     |       1176      |          237         |



### Part 2 : Methodology

We perform the binary classification to detect the use of sarcasm by probing the target word and its usage in the tweet. The features we used are mainly two types:

1. Word2Vec
2. Sentiment Flow

#### Preprocessing
Each tweet was preprocessed to extract the fea- tures that will be used for classification later. First the raw text of the tweets is tokenized using the NLTK’s TweetTokenizer . There are lot options available in NLTK framework for tokenization, but I used this tokenizer as it is designed specifi- cally to tokenize Twitter data. Next I remove all the hash tags from the tweets. This is to normalize the sarcastic tweets as the classifier then tries to look for ‘#sarcasm’ to classify the sarcastic tweets. For a general classification implementa- tion, we would also remove the target word from the tweets, but for our experiments we keep the target word. Then we replace all numeric tokens
in the tweets with a common token- the number ‘2’. Next we align the case of all the tokens in the tweet. By aligning the case, we change the case of all the tokens to lower case except if the token consist of all the letters in uppercase. For example, ‘Never’ would be aligned to ‘never’ whereas ‘NEVER’ would be kept as it is. Now we need to remove all the usernames mentioned in the tweet. The reason behind this is to remove all the named entities that do not help us capture the relationship between the words and the target word. Next I re- moved all the punctuations from the tweets. The code even cleaned punctuation marks like the el- lipsis so as to capture word to target relation efficiently.
#### Word2Vec
Next we need to train the word vectors so as to capture the similarity between the words present in the tweets. I used the word2vec [7] model imple- mented by Gensim [8]. The list of tweets that was preprocessed is fed into the word2vec model to generate the word embedding for all the words in the bag of words. This trained model is then saved for future purpose. I am training my own vectors for these experiments, however there are pre trained vectors that are available as open source for general purpose use.
The parameters used for training the vectors are minimum word count as 1, context window size of 10 words, number of parallel threads for train- ing the model is 4 and downsampling was 0.0001. The time taken to train the vectors for the target word depend directly on the size of the training data provided.
#### Kernel Matrix -- Word2Vec
![Main_Menu](01.jpeg ?raw=true =50x20)

[Source: http://www.anthology.aclweb.org/D/D15/D15-1116.pdf]
#### Kernel Matrix -- Sentiment Flow
Assuem $s$ and $s'$ are two sentiment flows of reviews, we defined their distance as 
![02](2.jpeg ?raw=true =50x20)

[Source: An Impact Analysis of Features in a Classification Approach to
Irony Detection in Product Reviews]


