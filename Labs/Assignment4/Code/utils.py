
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
  return counts.emission_counts[(word, tag)] / counts.ngram_counts[0][(tag,)]

def bigram_probability(previous_tag, current_tag, counts):
  if previous_tag == "*":
    denominator = counts.ngram_counts[1][(previous_tag, previous_tag)]
  else:
    denominator = counts.ngram_counts[0][(previous_tag,)]
  
  return counts.ngram_counts[1][(previous_tag, current_tag)] / denominator
