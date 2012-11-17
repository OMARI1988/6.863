#!/usr/bin/env python
import os
import re
import sys
import cfg_parse

def num_branches(filename):
    """
    Counts the number of branches the grammar takes
    """
    fd = open(filename)
    lines = fd.readlines()
    total = 0
    for line in lines:
	line = line.strip()
	sides = line.split("->")
	lhs = sides[0].strip()
	rhs = sides[1].strip()
	choices = rhs.split("\|")
	for choice in choices:
	    choice = choice.strip()
	    parts = choice.split()
	    total += len(parts)
    fd.close()
    return total

def num_symbols(filename):
    """
    Counts the number of non-whitespace tokens in
    a file
    """
    fd = open(filename)
    lines = fd.readlines()
    total = 0
    for line in lines:
	line = line.strip()
	tokens = line.split()
	total += len(tokens)
    fd.close()
    return total

if __name__ == "__main__":
    if len(sys.argv) >= 4:
	root = sys.argv[1]
	sentence_file = sys.argv[2]
	sent_num = int(sys.argv[3])
    else:
	print "usage %s <grammar directory> <sentence file> <sentence number>" %(sys.argv[0])
	exit(1)

    dirs = os.listdir(root)
    sentences = cfg_parse.read_sentences(sentence_file)
    if sent_num < 0 or sent_num >= len(sentences):
	print "error: sentence %d not in %s" %(sent_num, sentence_file)
	exit(1)

    sys.stdout.write("filename\tgrammar_size\tnum_branches\tnum_parses\ttime_taken\n");
    dirs.sort()
    for filename in dirs:

	if re.match(".*\.cfg$", filename):
	    grammar_file = "%s/%s" %(root, filename)
	    grammar_size = num_symbols(grammar_file)
	    sent, num_parses, time_taken, trees = \
		  cfg_parse.parse(sentences[sent_num], grammar_file)
	    nbranches = num_branches(grammar_file)
	    
	    fields = [filename, str(grammar_size), str(nbranches), str(num_parses), str(time_taken)]
	    sys.stdout.write("\t".join(fields))
	    sys.stdout.write("\n")
	    sys.stdout.flush()
		 

    
