#!/usr/bin/env ruby

require "pp"

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
  
  
  
end


Grammar.parse_file_named("grammar")