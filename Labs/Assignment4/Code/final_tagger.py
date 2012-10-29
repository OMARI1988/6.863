
from copy import copy
from collections import defaultdict
from count_freqs import *
from utils import *
import math
import sys
import os


if __name__ == "__main__":
  counts_file = open(os.path.join(os.path.dirname(__file__), "ner.counts"))
  sentences_file = open(os.path.join(os.path.dirname(__file__), "ner_dev.dat"))
  
  counts_file = open(sys.argv[1])
  sentences_file = open(sys.argv[2])
  
  
  infrequent_count = 5
  
  hmm = Hmm()
  hmm.read_counts(counts_file)
  
  word_counts = defaultdict(int)
  
  for word, tag in hmm.emission_counts:
    word_counts[word] += hmm.emission_counts[(word, tag)]
  
  vocab_size = len(word_counts)
  
  for word in word_counts:
    count = word_counts[word]
    if count < infrequent_count:
      for tag in hmm.all_states:
        if (word, tag) in hmm.emission_counts:
          #hmm.emission_counts[("_RARE_", tag)] += count
          hmm.emission_counts[("_RARE_", tag)] += hmm.emission_counts[(word, tag)]
  
  
  
  states = hmm.all_states.copy()
  #states.add("*")
  
  
  sentences = sentence_iterator(simple_conll_corpus_iterator(sentences_file))
  
  
  
  counters = 0
  
  for sentence in sentences:
    original_words = []
    words = defaultdict(str)
    n = len(sentence)
    
    words[-1] = "*"
    words[0] = "*"
    
    for i in range(0, n):
      word = sentence[i][1]
      original_words.append(word)
      if not(word in word_counts) or (word_counts[word] < infrequent_count):
        word = "_RARE_"
      words[i + 1] = word
    
    words[i + 2] = "STOP"
    
    
    bp = defaultdict(str)
    pi = defaultdict(float)
    y = defaultdict(str)
    y_probs = defaultdict(float)
    
    for u in states:
      for v in states:
        pi[(0, u, v)] = trigram_probability("*", u, v, hmm, vocab_size)
    
    
    for k in range(1, n + 1):
      word = words[k]
      for u in states:
        for v in states:
          max_prob = -1
          max_tag = None
          for w in states:
            prob = pi[(k - 1, w, u)] * trigram_probability(w, u, v, hmm, vocab_size) * emission_probability(word, v, hmm)
            if prob > max_prob:
              max_prob = prob
              max_tag = w
          pi[(k, u, v)] = max_prob
          bp[(k, u, v)] = max_tag
    
    
    max_prob = -1
    max_tag = (None, None)
    for u in hmm.all_states:
      for v in hmm.all_states:
        prob = pi[(n, u, v)] * trigram_probability(u, v, "STOP", hmm, vocab_size)
        if prob > max_prob:
          max_prob = prob
          max_tag = (u, v)
    
    y[n - 1] = max_tag[0]
    y[n] = max_tag[1]
    
    y_probs[n - 1] = max_prob
    y_probs[n] = max_prob
    
    for k in reversed(range(1, n - 1)):
      y[k] = bp[(k + 2, y[k + 1], y[k + 2])]
      y_probs[k] = pi[(k + 2, y[k + 1], y[k + 2])]
    
    
    for i in range(0, len(original_words)):
      print original_words[i] + " " + y[i + 1] + " " + str(math.log(y_probs[i + 1])/math.log(2))
    print ""
    
    counters += 1
    if counters == 1:
      #sys.exit()
      pass
    
  
  
