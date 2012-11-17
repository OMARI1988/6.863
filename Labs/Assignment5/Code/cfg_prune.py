#!/usr/bin/env python
# a program to generate the minimal grammar for a
# set of sentences.
# usage: $0 <grammar file> <sentence file> <output>
#           <max number of parses> <non-grammar>
#
# max parses - is the maximum number of parses each sentence is allowed
#    in the minimal grammar.  The generated productions can only come from
#    these parses.
# discard - is the ratio of unused productions to keep. 0.0 means discard
#           all unused productions.
#
import sys
import os
import nltk
from nltk.parse.chart import *
from datetime import datetime
import time
from nltk.parse import pchart
import random

def main(sentences, grammarfile, pcfg_grammar, algo, output, \
	 to_keeps, percent_discard, beam=0):

    grammar = nltk.data.load("file:%s" %(grammarfile))
    chart_parser = ChartParser(grammar,strategy=EARLEY_STRATEGY,trace=0)
    
    f = open(pcfg_grammar)
    pcfgrammar = f.read()
    f.close()

    if algo == "viterbi":
	pcfg_parser = nltk.ViterbiParser(nltk.parse_pcfg(pcfgrammar))
    elif algo == "inside":
	pcfg_parser = pchart.InsideChartParser(nltk.parse_pcfg(pcfgrammar),\
					       beam_size=beam)
    elif algo == "random":
	pcfg_parser = pchart.RandomChartParser(nltk.parse_pcfg(pcfgrammar),\
					       beam_size=beam)
    elif algo == "longest":
	pcfg_parser = pchart.LongestChartParser(nltk.parse_pcfg(pcfgrammar),\
						beam_size=beam)
    elif algo == "unsorted":
	pcfg_parser = pchart.UnsortedChartParser(nltk.parse_pcfg(pcfgrammar),\
						 beam_size=beam)	
    elif algo == "chart":
	pass
    else:
	print "unrecognized algorithm: %s" %(algo)
	return 1
	
    forest = []
    for sentence in sentences:
	parsed_sent = sentence.split()
	print "parsed_sent: %s" %(parsed_sent)
	start = datetime.now()

	if algo == "chart":
	    trees = chart_parser.nbest_parse(parsed_sent)
	else:
	    trees = pcfg_parser.nbest_parse(parsed_sent)
	    
	end = datetime.now()
	elapsed = end - start
	print "parsing time elapsed: %s" %(elapsed)
	print "parsing time elapsed: %d us" %(elapsed.microseconds)

	if (len(trees) == 0):
	    print "failed to parse: %s" %(sentence)
	    return 1;
	forest.append(trees)

    all_productions = grammar.productions()
    # randomly shuffle the productions
    all_productions = all_productions[0:len(all_productions)]
    random.shuffle(all_productions)
    random.shuffle(all_productions)

    status = 0
    for keep in to_keeps:
	for discard in percent_discard:
	    status += create_pruned_grammar(forest, all_productions, keep,\
					    discard, output)
    return status

def create_pruned_grammar(forest, all_productions, num_kept, discard,\
			  outputformat):
    used_set = set()
    for trees in forest:
	print "number of parses: %d" %(len(trees))
	if len(trees) > num_kept:
	    copytrees = trees[0:num_kept]
	else:
	    copytrees = trees[0:len(trees)]

	print "number kept: %d" %(len(copytrees))
	for tree in copytrees:
	    for production in tree.productions():
		used_set.add(production)

    can_discard = []
    keep_productions = []
    for production in all_productions:
	if production not in used_set:
	    can_discard.append(production)
	else:
	    keep_productions.append(production)

    print "initial can-discard: %d" %(len(can_discard))
    target = int( len(can_discard) * (discard/100.0) )
    print "target: %d" %(target)

    can_discard = can_discard[0:target]
    print "after pruned can-discard: %d" %(len(can_discard))

    outputfile = outputformat %(num_kept, discard)
    fd = open(outputfile, 'w')
    lines = 0
    for production in keep_productions:
	fd.write("%s\n" %(production))
	lines += 1
    for production in can_discard:
	fd.write("%s\n" %(production))
	lines += 1
    fd.close()
    print "grammar lines: %d" %(lines)
    
    os.system("cat minimal.cfg %s | sort | uniq > g%d_%d_raw.cfg"\
	      %(outputfile, num_kept, discard))
    os.system("python merge_grammar.py g%d_%d_raw.cfg g%d_%03d.cfg"\
	      %(num_kept, discard, num_kept, discard))
    os.system("rm g%d_%d_raw.cfg %s" %(num_kept, discard, outputfile))
    return 0

if __name__ == '__main__':
    if len(sys.argv) < 7:
	print "usage: %s <cfg> <p-cfg> <sentences> <keeps> <discards> algo [<min> <max>]" \
	      %(sys.argv[0])
	exit(1)

    grammarfile = sys.argv[1]
    pcfgrammarfile = sys.argv[2]
    sentencefile = sys.argv[3]
    keeps = sys.argv[4].split(",")
    int_keeps = [int(keep) for keep in keeps]

    discards = sys.argv[5].split(",")
    f_discards = [float(d) for d in discards]
    algo = sys.argv[6]

    if len(sys.argv) > 7:
	min_beam = int(sys.argv[7])
    else:
	min_beam = 100
	
    if len(sys.argv) > 8:
	max_beam = int(sys.argv[8])
    else:
	max_beam = 1000

    print "keeps: %s" %(int_keeps)
    step = 100
    fd = open(sentencefile)
    sentences = fd.readlines()
    fd.close()
    
    if algo != "chart":
	for beam in xrange(min_beam, max_beam, step):
	    output = "%s_b%d_%s_%s" %(algo, beam, sentencefile, grammarfile)
	    output = 'f%d_' + output
	    output = 'k%d_' + output
	    print "output: %s" %(output)
	    status = main(sentences, grammarfile,\
			  pcfgrammarfile, algo, output,\
			  int_keeps, f_discards,\
			  beam)
	    if status == 0:
		break
    else:
	output = "%s_%s_%s" %(algo, sentencefile, grammarfile)
	output = 'f%d_' + output
	output = 'k%d_' + output
	print "output: %s" %(output)
	status = main(sentences, grammarfile,\
		      pcfgrammarfile, algo, output,\
		      int_keeps, f_discards)
	
    
