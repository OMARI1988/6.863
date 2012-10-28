
require 'pp'
require File.join(File.dirname(__FILE__), 'counter.rb')

def bigram_probability(current_tag, previous_tag, ngram_counts)
  return ngram_counts[1][[previous_tag, current_tag]] / ngram_counts[0][[previous_tag]]
end

counter = Counter.new(File.open("ner.counts"))

emission_counts = counter.emission_counts
word_counts = counter.word_counts

ngram_counts = counter.ngram_counts
entity_tags = counter.entity_tags

pp ngram_counts