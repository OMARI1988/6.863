
require 'set'
require 'pp'
require File.join(File.dirname(__FILE__), 'counter.rb')

def emission_probability(word, tag, emission_counts, ngram_counts)
  return (emission_counts[[word, tag]] || 0) / ngram_counts[0][[tag]]
end


counter = Counter.new(File.open("ner.counts"))

emission_counts = counter.emission_counts
word_counts = counter.word_counts

ngram_counts = counter.ngram_counts
entity_tags = counter.entity_tags

for word, count in word_counts do
  if count < 5
    for tag in entity_tags do
      if emission_counts.include? [word, tag] then
        emission_counts[["_RARE_", tag]] ||= 0
        emission_counts[["_RARE_", tag]] += count
      end
    end
  end
end

sentences_files = File.open("ner_dev.dat")
sentences_files.each_line do |line|
  word = line.chop
  original_word = word
  
  if word == "" then
    puts
  else
    
    if word_counts[word].nil? || word_counts[word] < 5 then
      word = "_RARE_"
    end
    
    current_probability = -1
    current_tag = nil
    
    for tag in entity_tags do
      probability = emission_probability(word, tag, emission_counts, ngram_counts)
      if probability > current_probability then
        current_probability = probability
        current_tag = tag
      end
    end
    
    
    puts original_word + " " + current_tag + " " + (Math.log(current_probability)/Math.log(2)).to_s
    
  end
  
end