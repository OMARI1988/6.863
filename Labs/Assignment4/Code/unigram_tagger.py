
from collections import defaultdict
from count_freqs import Hmm
import math
import sys

def emission_probability(word, tag, emission_counts, ngram_counts):
  return emission_counts[(word, tag)] / ngram_counts[0][(tag,)]

if __name__ == "__main__":
  counts_file = open(sys.argv[1])
  sentences_file = open(sys.argv[2])
  
  hmm = Hmm()
  hmm.read_counts(counts_file)
  
  emission_counts = hmm.emission_counts
  ngram_counts = hmm.ngram_counts
  
  print ngram_counts
  sys.exit()
  
  entity_tags = ["I-PER", "I-ORG", "I-LOC", "I-MISC", "O"]
  entity_tags = hmm.all_states
  trained_words = defaultdict(int)
  infrequent_words = defaultdict(int)
  
  for word, tag in emission_counts:
    trained_words[word] += hmm.emission_counts[(word, tag)]
  
  for word in trained_words:
    if trained_words[word] < 5:
      infrequent_words[word] = 1
  
  for word in infrequent_words:
    for tag in entity_tags:
      if (word, tag) in emission_counts:
        emission_counts[("_RARE_", tag)] += 1
        del emission_counts[(word, tag)]
  
  line = sentences_file.readline()
  while line:
      word = line.strip()
      original_word = word
      if word and not(word == ""):
        if (word in infrequent_words) or not(word in trained_words):
          word = "_RARE_"
        
        current_probability = -1
        current_tag = None
        
        for tag in entity_tags:
          probability = emission_probability(word, tag, emission_counts, ngram_counts)
          if probability > current_probability:
            current_probability = probability
            current_tag = tag
            
        print original_word + " " + current_tag + " " + str(math.log(current_probability))
      else:
        print ""
      line = sentences_file.readline()
      
  