
import re

def arg_max(iterator, callback):
  max_value = -1
  max_index = None
  for i in iterator:
    value = callback(i)
    if value > max_value:
      max_value = value
      max_index = i
  return (max_index, max_value)

def emission_probability(word, tag, counts):
  if tag == "*":
    denominator = counts.ngram_counts[1][(tag, tag)]
  else:
    denominator = counts.ngram_counts[0][(tag,)]
  
  return counts.emission_counts[(word, tag)] / denominator

def bigram_probability(tag1, tag2, counts):
  if tag1 == "*":
    denominator = counts.ngram_counts[1][(tag1, tag1)]
  else:
    denominator = counts.ngram_counts[0][(tag1,)]
  
  return counts.ngram_counts[1][(tag1, tag2)] / denominator

def trigram_probability(tag1, tag2, tag3, counts, vocab_size):
  numerator = counts.ngram_counts[2][(tag1, tag2, tag3)]
  denominator = counts.ngram_counts[1][(tag1, tag2)]
  return  (numerator + 1) / (denominator + vocab_size)
  
def classify_word(word):
  classes = [
    (re.compile("^[A-Z\.]+$"), "_ABREVIATION_"),
    #(re.compile("(^[A-Z\.]+)|(^[A-Z]{3})$"), "_ABREVIATION_"),
    #(re.compile("^[A-Z]\.$"), "_ABREVIATION_"),
    (re.compile("^[\.\-\,\d]+$"), "_NUMBER_"),
    (re.compile("^[A-Z][a-z]+$"), "_CAPITALIZED_"),
    (re.compile("^[A-Z]+$"), "_UPPERCASE_"),
    (re.compile("^[a-z]+$"), "_LOWERCASE_")
    #(re.compile("-"), "_HYPHEN_"),    
  ]
  for pattern, name in classes:
    if pattern.search(word) != None:
      return name
  return "_RARE_"
  

  