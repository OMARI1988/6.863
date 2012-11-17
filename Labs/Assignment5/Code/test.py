from nltk import *
from learn_pcfg import *
grammar = learn_trees(three_trees)
print grammar
print grammar.start()
p = prob_parse(grammar, '''Jeff pronounced that Fred snored loudly''')
print p

