#!/usr/bin/env python

import nltk
from nltk.parse import pchart
from datetime import datetime
import cfg_parse

def pcfg_chartparser(grammarfile):
 f = open(grammarfile)
 grammar = f.read()
 f.close()
 return nltk.ViterbiParser(nltk.parse_pcfg(grammar))


def main():
  grammarp = pcfg_chartparser("wsjp.cfg")
  sents = cfg_parse.read_sentences("sentences.txt")
  print "sentence\ttime elapsed (us)"
  for sent in sents:
    start = datetime.now()
    tree = grammarp.parse(sent) 
    end = datetime.now()
    elapsed = end - start
    microseconds = elapsed.microseconds + 1000000*elapsed.seconds
    print "%s\t%d" %(sent, microseconds)
    print tree 
if __name__ == '__main__': main()
