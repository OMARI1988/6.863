
from collections import defaultdict
from count_freqs import Hmm
from count_freqs import *
import math
import sys
import os

def emission_probability(word, tag, counts):
  return counts.emission_counts[(word, tag)] / counts.ngram_counts[0][(tag,)]

def bigram_probability(current_tag, previous_tag, counts):
  if previous_tag == "*":
    denominator = counts.ngram_counts[1][(previous_tag, previous_tag)]
  else:
    denominator = counts.ngram_counts[0][(previous_tag,)]
  
  return counts.ngram_counts[1][(previous_tag, current_tag)] / denominator

if __name__ == "__main__":
  counts_file = open(os.path.join(os.path.dirname(__file__), "ner.counts"))
  sentences_file = open(os.path.join(os.path.dirname(__file__), "ner_dev.dat"))
  
  hmm = Hmm(2)
  hmm.read_counts(counts_file)
  
  
  sentences = sentence_iterator(simple_conll_corpus_iterator(sentences_file))
  
  for sentence in sentences:
    probability_of_tag_at_word = defaultdict(float)
    most_likely_tag_given_previous_tag = defaultdict(str)
    tag_probabilities = defaultdict(str)
    
    for tag in hmm.all_states:
      probability_of_tag_at_word[(tag, 0)] = 0.0
    probability_of_tag_at_word[("*", 0)] = 1.0
    
    words = ["*"]
    
    for _, word in sentence:
      words.append(word)
      
    words.append("STOP")
    
    i = 0
    while i < len(words) - 1:
      next_word = words[i+1]
      for next_tag in hmm.all_states:
        current_max_probability = -1
        current_max_tag = None
        
        for tag in hmm.all_states:
          temp = probability_of_tag_at_word[(tag, i)] * emission_probability(next_word, next_tag, hmm) * bigram_probability(next_tag, tag, hmm)
          if temp > current_max_probability:
            current_max_probability = temp
            current_max_tag = tag
        probability_of_tag_at_word[(next_tag, i+1)] = current_max_probability
        most_likely_tag_given_previous_tag[(next_tag, i+1)] = current_max_tag
        
      i += 1
    
    print probability_of_tag_at_word
    print most_likely_tag_given_previous_tag
    
    temp_max = -1.0
    temp_tag = None
    for tag in hmm.all_states:
      value = probability_of_tag_at_word[(tag, len(words))]
      if value > temp_max:
        temp_max = value
        temp_tag = tag
    
    tag_probabilities[(len(words))] = tag
    
    i = len(words) - 1
    while i >= 0:
      tag_probabilities[(i)] = most_likely_tag_given_previous_tag[(tag_probabilities[(i+1)], i+1)]
      i -= 1
    
    print words
    print tag_probabilities
    
    sys.exit()
    
    
    
  
  
  
