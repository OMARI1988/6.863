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
      tokens = tokens[1, tokens.size - 1]
      
      lhs = tokens[0]
      rhs = tokens[1, tokens.size - 1]
      
      grammar.add_rule(lhs, rhs)
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
  
  def add_rule(lhs, rhs)
    unless rhs.class == Array then
      raise "The RHS must be an array (even if it is a single symbol)"
    end
    
    table[lhs] ||= []
    table[lhs] << rhs
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
      index = Helper.random_number(0, choices.size)
      choice = choices[index]
      
      
      for symbol in choice do
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

