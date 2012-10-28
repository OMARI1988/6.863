
from collections import defaultdict
from count_freqs import *
from utils import *
import math
import sys
import os

if __name__ == "__main__":
  counts_file = open(os.path.join(os.path.dirname(__file__), "ner.counts"))
  sentences_file = open(os.path.join(os.path.dirname(__file__), "ner_dev.dat"))
  
  