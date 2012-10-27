
require 'set'
require 'pp'

def emission_probability(word, tag, emission_counts, ngram_counts)
  return (emission_counts[[word, tag]] || 0) / ngram_counts[0][[tag]]
end


counts_file = File.open("ner.counts")

emission_counts = {}
word_counts = {}

ngram_counts = []
entity_tags = Set.new

counts_file.each_line do |line|
  parts = line.strip().split(" ")
  count = parts[0].to_f
  if parts[1] == "WORDTAG" then
    tag = parts[2]
    word = parts[3]
    
    word_counts[word] ||= 0
    word_counts[word] += count
    
    emission_counts[[word, tag]] = count
    entity_tags.add(tag)
  elsif parts[1].end_with?("GRAM")
    n = parts[1].gsub("-GRAM","").to_f
    ngram = parts
    ngram.shift
    ngram.shift
    
    ngram_counts[n-1] ||= {}
    ngram_counts[n-1][ngram] = count
  end
end

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
    
    
    puts original_word + " " + current_tag + " " + (Math.log2(current_probability)).to_s
    
  end
  
end