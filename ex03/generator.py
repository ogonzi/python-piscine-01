import string
import random

def is_printable_string(text):
	if isinstance(text, str) == False:
		return False
	for c in text:
		if c not in string.printable:
			return False
	return True

def shuffle_array(arr):
	'''Takes an array as input and returns the shuffled array.
	It works by iterating over the array in reverse order, and 
	for each element 'i', it randomly selects another index 'j'
	between 0 and 'i', and swaps the elements at those two indices.
	The process is repeated until all elements have been shuffled.'''
	for i in range(len(arr) - 1, 0, -1):
		j = random.randint(0, i)
		arr[i], arr[j] = arr[j], arr[i]
	return arr

def generator(text, sep=" ", option=None):
	'''Divides the text with accordance to the value of sep and produces
	the sub-strings. options specifies if an action if realized to the sub-strings before being produced'''
	valid_options = ['shuffle', 'ordered', 'unique']
	if is_printable_string(text) == False:
		print("ERROR")
	elif option != None and option not in valid_options:
		print("ERROR")
	else:
		split_text = text.split(" ")
		if option == "shuffle":
			split_text = shuffle_array(split_text)
		elif option == "ordered":
			split_text = sorted(split_text)
		elif option == "unique":
			split_text = set(split_text)
		for word in split_text:
			yield word