
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
  
