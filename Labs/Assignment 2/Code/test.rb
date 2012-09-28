#!/usr/bin/env ruby

grammar3 = [
  "Sally ate a sandwich .",
  "Sally and the president wanted and ate a sandwich .",
  "the president sighed .",
  "the president thought that a sandwich sighed .",
  "that a sandwich ate Sally perplexed the president .",
  "the very very very perplexed president ate a sandwich .",
  "the president worked on every proposal on the desk ."
]

grammar4 = grammar3.clone.concat [
  "did Sally eat a sandwich ?",
  "will Sally eat a sandwich ?",
  "did the president think ?",
  "did the president think that Sally ate ?",
  
  "what did the president think ?",
  "what did the president think that Sally ate ?",
  "what did Sally eat the sandwich with ?",
  "who ate the sandwich ?",
  "where did Sally eat the sandwich ?"
]

puts "# Grammar 3"
for sentence in grammar3 do
  puts `echo "#{sentence}" | ~/6863-assignment2/parse -g ./grammar3`
end

puts
puts
puts "# Grammar 4"

for sentence in grammar4 do
  puts `echo "#{sentence}" | ~/6863-assignment2/parse -g ./grammar4`
end

