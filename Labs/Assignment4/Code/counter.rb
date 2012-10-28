
require 'set'

class Counter
  
  attr_accessor :word_counts
  attr_accessor :ngram_counts
  attr_accessor :emission_counts
  attr_accessor :entity_tags
  
  
  def initialize(counts_file)
    
    @emission_counts = {}
    @word_counts = {}
    @ngram_counts = []
    @entity_tags = Set.new
    
    counts_file.each_line do |line|
      parts = line.strip().split(" ")
      count = parts[0].to_f
      if parts[1] == "WORDTAG" then
        tag = parts[2]
        word = parts[3]
    
        @word_counts[word] ||= 0
        @word_counts[word] += count
    
        @emission_counts[[word, tag]] = count
        @entity_tags.add(tag)
      elsif parts[1].end_with?("GRAM")
        n = parts[1].gsub("-GRAM","").to_f
        ngram = parts
        ngram.shift
        ngram.shift
    
        @ngram_counts[n-1] ||= {}
        @ngram_counts[n-1][ngram] = count
      end
    end
  end
  
end