#!/usr/bin/env ruby

#
# 6.863 Assignment 2
#
# Author: Salman Ahmad (saahmad@mit.edu)
#

require "pp"

class Helper
  
  def self.random_number(first, last)
     first + rand(last - first)
  end
  
  def self.random_index(probabilities = [])
    if probabilities.size == 0 then
      raise "To pick a random index you must have a non-empty array"
    end
    
    cumulative_probabilities = []
    
    sum = 0
    for probability in probabilities do
      sum += probability.to_f
      cumulative_probabilities << sum
    end
    
    cumulative_probabilities.each_index do |index|
      cumulative_probabilities[index] = cumulative_probabilities[index] / sum
    end
    
    pick = rand()
    selected_index = 0
    
    cumulative_probabilities.each_index do |index|
      size = cumulative_probabilities.size
      look_up = size - 1 - index
      
      prob = cumulative_probabilities[look_up]
      if pick <= prob then
        selected_index = look_up
      end
    end
    
    return selected_index
  end
  
end

class Rule
  
  attr_accessor :probability
  attr_accessor :lhs
  attr_accessor :rhs
  
  def initialize(probability, lhs, rhs)
    unless rhs.class == Array then
      raise "The RHS must be an array (even if it is a single symbol)"
    end
    
    self.probability = probability
    self.lhs = lhs
    self.rhs = rhs
  end
end

class Grammar
  
  attr_accessor :table
  
  def initialize
    self.table = {}
  end
  
  def self.parse(contents)
    grammar = self.new
    
    lines = contents.split("\n")
    processed_lines = []
    
    for line in lines do
      line.gsub!(/#.*$/, "")
      next if line.match(/^\s*$/)
      processed_lines << line.strip
    end
    
    for line in processed_lines do
      tokens = line.split
      
      probability = tokens[0]
      tokens = tokens[1, tokens.size - 1]
      
      lhs = tokens[0]
      rhs = tokens[1, tokens.size - 1]
      
      grammar.add_rule(Rule.new(probability, lhs, rhs))
    end
    
    
    return grammar
  end
  
  def self.parse_file(file)
    contents = file.read
    self.parse(contents)
  end
  
  def self.parse_file_named(filename)
    self.parse_file(File.open(filename))
  end
  
  def add_rule(rule)
    unless rule.class == Rule then
      raise "You must add only a Rule to the grammar"
    end
    
    table[rule.lhs] ||= []
    table[rule.lhs] << rule
  end
  
  def random_sentence
    random_phrase
  end
  
  def random_phrase(start_symbol = "START")
    phrase = []
    choices = @table[start_symbol]
    
    if choices.nil? || choices.size == 0 then
      phrase << start_symbol
    else
      probabilities = []
      for rule in choices do
        probabilities << rule.probability
      end
      
      index = Helper.random_index(probabilities)
      choice = choices[index]
      
      for symbol in choice.rhs do
        phrase << random_phrase(symbol)
      end
    end
    
    return phrase.join(" ")
  end
  
end


grammar_file_name = ARGV[0] || "grammar"

count = ARGV[1] || 1
count = count.to_i

grammar = Grammar.parse_file_named(grammar_file_name)

count.times do
  puts grammar.random_sentence
end

