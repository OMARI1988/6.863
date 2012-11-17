#!/usr/bin/env python

import nltk
from nltk.parse.chart import *
from datetime import datetime

def main():
  grammar = nltk.data.load("file:wsj.cfg")    
  sent1 = "John is happy".split()
  sent2 = "The very biggest companies are not likely to go under .".split()
  chart_parser = ChartParser(grammar,strategy=EARLEY_STRATEGY,trace=0) 
  start = datetime.now()
  trees = chart_parser.nbest_parse(sent1)
  end = datetime.now()
  elapsed = end.microsecond - start.microsecond
  print "time elapsed: %d ms" %(elapsed/1000)
  #for tree in trees:
  #  print tree    
    
if __name__ == '__main__': main()
