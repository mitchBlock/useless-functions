import os
import random
import sys

GORGONZOLA_STR = 'gorgonzola';

def gorgonzola(rand_seed):
	print ('Using random seed: {} to find string'.format(rand_seed));
	random.seed(rand_seed);
	iter_count = 0;
	found_gorgonzola = False;
	while not found_gorgonzola:
		iter_count += 1;
		str_check = '';
		for _ in range (10):
			int_char = random.randint(97, 122);
			str_check += chr(int_char);
		found_gorgonzola = (str_check == GORGONZOLA_STR);
	return iter_count;

if __name__ == '__main__':
	rand_seed = int(sys.argv[2]) if len(sys.argv) > 1 else os.urandom(128);
	iterations = gorgonzola(rand_seed);
	print ('Using random seed: {} took {} iterations to generate the word gorgonzola'.format(rand_seed, iterations));