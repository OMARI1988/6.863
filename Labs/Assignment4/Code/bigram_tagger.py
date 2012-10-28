
from collections import defaultdict
from count_freqs import Hmm
from count_freqs import *
import math
import sys
import os

def emission_probability(word, tag, counts):
  return counts.emission_counts[(word, tag)] / counts.ngram_counts[0][(tag,)]

def bigram_probability(previous_tag, current_tag, counts):
  if previous_tag == "*":
    denominator = counts.ngram_counts[1][(previous_tag, previous_tag)]
  else:
    denominator = counts.ngram_counts[0][(previous_tag,)]
  
  return counts.ngram_counts[1][(previous_tag, current_tag)] / denominator

if __name__ == "__main__":
  counts_file = open(os.path.join(os.path.dirname(__file__), "ner.counts"))
  sentences_file = open(os.path.join(os.path.dirname(__file__), "ner_dev.dat"))
  
  hmm = Hmm()
  hmm.read_counts(counts_file)
  
  word_counts = defaultdict(int)
  
  for word, tag in hmm.emission_counts:
    word_counts[word] += hmm.emission_counts[(word, tag)]
  
  for word in word_counts:
    count = word_counts[word]
    if count < 5:
      for tag in hmm.all_states:
        if (word, tag) in hmm.emission_counts:
          hmm.emission_counts[("_RARE_", tag)] += count
  
  initial_probability = defaultdict(float)
  initial_tag = None
  
  current_max = -1
  for tag in hmm.all_states:
    value = bigram_probability("*", tag, hmm)
    if value > current_max:
      current_max = value
      initial_tag = tag
    initial_probability[tag] = value
  
  
  sentences = sentence_iterator(simple_conll_corpus_iterator(sentences_file))
  foo_bar_count = 0
  
  for sentence in sentences:
    original_words = []
    words = []
    for _, word in sentence:
      if not(word in word_counts) or (word_counts[word] < 5):
        words.append("_RARE_")
      else:
        words.append(word)
      original_words.append(word)
    
    t1 = defaultdict(float)
    t2 = defaultdict(str)
    
    x_probs = defaultdict(float)
    x = defaultdict(str)
    
    for tag in hmm.all_states:
      t1[(tag, 0)] = initial_probability[tag] * emission_probability(words[0], tag, hmm)
      t2[(tag, 0)] = initial_tag
    
    for i in range(1, len(words)):
      for j in hmm.all_states:
        current_max = -1
        current_tag = None
        
        for k in hmm.all_states:
          value = t1[(k, i - 1)] * bigram_probability(k , j, hmm) * emission_probability(words[i], j, hmm)
          if value > current_max:
            current_max = value
            current_tag = k
        
        t1[(j, i)] = current_max
        t2[(j, i)] = current_tag
    
    
    current_max = -1.0
    current_tag = None
    for k in hmm.all_states:
      value = t1[(k, len(words) - 1)]
      if value > current_max:
        current_max = value
        current_tag = k
    
    
    x[len(words) - 1] = current_tag
    x_probs[len(words) - 1] = current_max
    
    for i in reversed(range(1, len(words))):
      current_max = -1
      current_tag = None
      for k in hmm.all_states:
        value = t1[(k, i - 1)]
        if value > current_max:
          current_max = value
          current_tag = k
      x[i - 1] = current_tag
      x_probs[i - 1] = current_max
    
    for i in range(0, len(words)):
      print original_words[i] + " " + x[i] + " " + str(math.log(x_probs[i])/math.log(2))
    print ""
    
    foo_bar_count += 1
    if foo_bar_count == 3:
      pass
      #sys.exit()

    
    
    
  
  
  
