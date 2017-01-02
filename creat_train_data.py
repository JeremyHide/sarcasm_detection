import sys
import time
import preprocess_review
from nltk.corpus import BracketParseCorpusReader


def main():
	lines = []
	count = 0;
	key_word = 'like'
	file = open('sarcasm_lines.txt','r')
	while count <438:
		
		try:
			line = (file.readline());
			if (line is not '') and (key_word in line):
				lines.append(key_word+'\t1'+'\t'+ preprocess_review.removeID(line));
				line = '';
		except UnicodeDecodeError:
			continue;
		count += 1

	# add non-sarcasm reviews
	corpus_root ='SarcasmCorpus/22/Regular'
	corpus = BracketParseCorpusReader(corpus_root,'.*')
	for fileid in corpus.fileids()[1:]:
		
		try:
			review = corpus.raw(fileid)

			if (key_word in review):
				lines.append(key_word + '\t0' + '\t' + preprocess_review.removeHead(review))
		
		except UnicodeDecodeError:
			continue

	print(len(lines))
	file = open(key_word+'.train','w')
	file.writelines(lines)
	file.close();

main()


