"""
	annotate for a english book
"""
from nltk.corpus import wordnet as wn
import pickle
import re

known_words_file_path = 'known_words.txt'

def query_wordnet(unknown_word):
	pass

def whether_know(word):
	pass

def annotator(book_path):
	known_words_file = open(known_words_file_path, 'r')
	known_words_list = pickle.load(known_words_file)
	known_words_set = set(known_words_list)
	known_words_file.close()
	#print known_words_set
	book_in = open(book_path, 'r')
	book_out = open('annotated_'+book_path, 'w')
	unknown_word_file = open('unknown_words.txt', 'w')
	annotated_words_set = set()
	for line in book_in:
		words_list = line.split()		
		words_list_out = []
		for word in words_list:
			words_list_out.append(word)
			if word.lower() in known_words_set:
				continue
			elif word.lower() in annotated_words_set:
				continue			
			elif wn.morphy(word):					
				morphy = wn.morphy(word)
				if morphy in known_words_set:
					known_words_set.add(word)
					continue
				else:
					print >> unknown_word_file, word, morphy
					syns = wn.synsets(word)
					words_list_out.append('('+ syns[0].definition + ')')
					annotated_words_set.add(word.lower())					
		for output_word in words_list_out:
			book_out.write(output_word + ' ')
		book_out.write('\n')
		
	book_in.close()
	book_out.close()
	unknown_word_file.close()

	output_file = open(known_words_file_path, 'w')
	pickle.dump(sorted(known_words_set),output_file)
	output_file.close()
	pass

def merge_known_words_files():
	known_words_files_list = ['junior.txt','senior.txt','cet4.txt','cet6.txt']
	output_file = open(known_words_file_path, 'w')
	output_list = []
	output_set = set()
	for input_file_path in known_words_files_list:
		with open(input_file_path, 'rb') as inf:
			tmp_set = set(re.findall(re.compile('[a-zA-Z]+'), inf.read().lower()))
		output_set = output_set.union(tmp_set)
		inf.close()	
	pickle.dump(sorted(output_set),output_file)
	output_file.close()


if __name__=='__main__':
	#merge_known_words_files()
	book_path = 'war_and_peace.txt'
	annotator(book_path)
	