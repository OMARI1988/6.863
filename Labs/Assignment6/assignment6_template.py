#!/usr/bin/env python
# Assignment 6 answer template.
# Updated Fri Nov 16, 2012 at 23:28
# http://web.mit.edu/6.863/fall2012/writeups/assignment6/assignment6_template.py
#
# Fill in your answers here, in the variables that end with _ANSWER.
# The format of the desired answers are described in the variables that end with _FORMAT. Don't deviate from this format.
#
# Before submitting, verify that you have filled out the questions and
# your submission follows the desired format by running this file:
# python assignment6_template.py

# what is your name?
what_is_my_name_ANSWER = 'Salman Ahmad'
what_is_my_name_FORMAT = 'freeform text' # can be an arbitrary string, no format restrictions

# what are the names of your collaborators, if any?
who_are_my_collaborators_ANSWER = []
who_are_my_collaborators_FORMAT = 'list of strings' # ie, ['John Doe', 'Jane Doe']

# === question 1: using modern probabilistic parsers ===

# What information was present in the NLTK parser's part-of-speech assignments that is not conveyed between the maximum entropy tagger and the Bikel parser?
info_lost_when_using_maxent_tagger_ANSWER = 'The Bikel parser only sees the part of speech tag and does not get to see the actual word itself. So the parser is "at the mercy" of the tagger to do its job correctly.'
info_lost_when_using_maxent_tagger_FORMAT = 'freeform text'

# what is the first sentence in the training set where the (Bikel) parser makes an error with Precision < 100% ? Report the sentence number and the actual sentence
sentence_number_of_first_error_ANSWER = 9
sentence_number_of_first_error_FORMAT = 'integer' # 0, 1, etc

sentence_with_first_error_ANSWER = 'Bell , based in Los Angeles , makes and distributes electronic , computer and building products .'
sentence_with_first_error_FORMAT = 'freeform text'

# how would you describe the kind of error that the parser makes on this sentence? Does this error have any effect on the meaning? Explain briefly.
error_type_made_by_parser_ANSWER = 'The parser messes up with "electronic, computer and building". Instead of treating each of the words as describing "products" the parser groups "electronic, computer" together and only uses "building" to describe "products". This does change the meaning. Bell does not distribute "electronic" - that does not even make grammatical sense - it distributes "electronic products".'
error_type_made_by_parser_FORMAT = 'freeform text'

# === question 2: current issues for statistical parsers ===

# What is the relationship between sentence length and sentence likelihood, all other things being equal?
sentence_length_and_likelihood_relationship_ANSWER = 'The longer the sentences seem to be less likely - their log scores are more negative.'
sentence_length_and_likelihood_relationship_FORMAT = 'freeform text'

# Is there any difference between the scores when you substitute 'broker' for 'witch'?
is_there_a_difference_in_score_ANSWER = False
is_there_a_difference_in_score_FORMAT = 'boolean' # True or False

# Why or why not?
why_or_why_not_is_score_different_ANSWER = 'Granted, while the scores are not "identical" they are not as different as the change you see between longer and shorter sentences. The reason for this is that the Bikel parser only takes into account the part of speech, not the actual word itself. Thus, the Bikel parser (which does take into account context) is unable to see that "wicked witch" may be more likely than "wicked broker" because all it sees is "JJ NN". The reason the scores are not "identical" is because the actual part of speech tagger itself may have associated different likelihoods to each word which get propogated up to the parser. In fact, this is probably why the parser thinks that "wicked broker" is actually more likely than "wicked witch" because the "broker" may be more common than "witch" when you remove the surrounding context.'
why_or_why_not_is_score_different_FORMAT = 'freeform text'

# List the log probability of the parses of each of these sentences (using the Bikel parser)

# John slept .
sentence1_logprob_ANSWER = -20.47
sentence1_logprob_FORMAT = 'float' # floating-point number, ie -32.6

# John slept Bill .
sentence2_logprob_ANSWER = -33.65
sentence2_logprob_FORMAT = 'float'

# Bill was arrested .
sentence3_logprob_ANSWER = -28.22
sentence3_logprob_FORMAT = 'float'

# It was arrested Bill .
sentence4_logprob_ANSWER = -33.09
sentence4_logprob_FORMAT = 'float'

# I tried to leave .
sentence5_logprob_ANSWER = -24.49
sentence5_logprob_FORMAT = 'float'

# I tried John to leave .
sentence6_logprob_ANSWER = -39.06
sentence6_logprob_FORMAT = 'float'

# I promised John to leave .
sentence7_logprob_ANSWER = -40.74
sentence7_logprob_FORMAT = 'float'

# Based on this, do you think the alignment between grammaticality and likelihood is accurate?
alignment_between_grammaticality_and_likelihood_ANSWER = 'No. The best example is to look at sentences 6 and 7. Both of these sentences are the most simliar allowing us the test the "all other things considered equal" theory. They are the same lenngth (in words), produce the exact same parts of speech tags and exact same parse tree structure. However, (6) is ungramatical while (7) is. Interestingly enough, 6 is MORE likely than 7 despite it being ungrammatical. Thus, there does not seem to be a good alignment between gramticality and likelihood.'
alignment_between_grammaticality_and_likelihood_FORMAT = 'freeform text'

# Fill out the rest of the table, with either the entries 'high' or 'low', first recording the results from your parse of mixed the milk with the water, and then the rest of the table entries, which are blank.

# Verb: mixed; Noun: water; Noun with milk
table1_ANSWER = 'HIGH'
table1_FORMAT = 'HIGH or LOW' # 'HIGH' or 'LOW'

# Verb: mixed; Noun: water; milk with Noun
table2_ANSWER = 'LOW'
table2_FORMAT = 'HIGH or LOW'

# Verb: mixed; Noun: stock; Noun with milk
table3_ANSWER = 'LOW'
table3_FORMAT = 'HIGH or LOW'

# Verb: mixed; Noun: stock; milk with Noun
table4_ANSWER = 'LOW'
table4_FORMAT = 'HIGH or LOW'

# Verb: sold; Noun: water; Noun with milk
table5_ANSWER = 'HIGH'
table5_FORMAT = 'HIGH or LOW'

# Verb: sold; Noun: water; milk with Noun
table6_ANSWER = 'LOW'
table6_FORMAT = 'HIGH or LOW'

# Verb: sold; Noun: stock; Noun with milk
table7_ANSWER = 'HIGH'
table7_FORMAT = 'HIGH or LOW'

# Verb: sold; Noun: stock; milk with Noun
table8_ANSWER = 'LOW'
table8_FORMAT = 'HIGH or LOW'

# What explains the pattern of HIGH and LOW attachments that you got in the previous problem?
high_low_attachment_pattern_ANSWER = 'Sold almost always appears with VP -> VBN NP PP (a high assignment). '
high_low_attachment_pattern_FORMAT = 'freeform text'

# === END OF YOUR SUBMISSION, DON'T MODIFY THIS LINE OR ANYTHING BELOW IT ===

# The following code does the verification that your submission is correctly formatted and that you have filled out all the questions.

def have_format_error(answer, fmt):
  if fmt == 'integer':
    if type(answer) != type(0):
      return 'Must be an integer, ex: 1'
    return None
  elif fmt == 'boolean':
    if answer not in [True, False]:
      return 'Must be a boolean, ex: True'
    return None
  elif fmt == 'float':
    if type(answer) != type(0.0):
      return 'Must be a float, ex: 0.0'
    return None
  elif fmt == 'probability':
    if type(answer) != type(0.0):
      return 'Must be a float, ex: 0.0'
    if not (0.0 <= answer <= 1.0):
      return 'Probability must be between 0.0 and 1.0, ex: 0.5'
    return None
  elif fmt == 'list of strings':
    if type(answer) != type([]):
      return "Must be a list, ex: ['John Doe']"
    if len([x for x in answer if type(x) != type('')]) > 0:
      return "Elements in the list must be strings, ex: ['John Doe']"
    return None
  elif fmt == 'dictionary of rule probabilities':
    if type(answer) != type({}):
      return "Must be a dictionary, ex: {'V PP': 0.1, 'V': 0.9}"
    if len([x for x in answer.keys() if type(x) != type('')]) > 0:
      return "Keys in the dictionary must be strings, ex: {'V PP': 0.1, 'V': 0.9}"
    if len([x for x in answer.values() if type(x) != type(0.0)]) > 0:
      return "Values in the dictionary must be floating point numbers, ex: {'V PP': 0.1, 'V': 0.9}"
    if False in [0.0 <= x <= 1.0 for x in answer.values()]:
      return "Values in the dictionary must each be between 0.0 and 1.0, ex: {'V PP': 0.1, 'V': 0.9}"
    if not (0.99 <= sum(answer.values()) <= 1.01):
      return "Values in the dictionary must sum to 1.0, ex: {'V PP': 0.1, 'V': 0.9}"
    return None
  elif fmt in ['freeform text', 'tree', 'parse strategy', 'HIGH or LOW']: # strings
    if type(answer) != type(''):
      return "Must be a string"
    answer = answer.strip()
    if fmt == 'tree':
      if '(' not in answer:
        return "Parse tree needs to have at least 1 '('"
      if ')' not in answer:
        return "Parse tree needs to have at least 1 ')'"
      if answer[0] != '(':
        return "Parse tree needs to start with '('"
      if answer[-1] != ')':
        return "Parse tree needs to end with ')'"
      if answer.count('(') != answer.count(')'):
        return "Parse tree need to have an equal number of '(' and ')'"
      if index_where_parse_tree_is_closed(answer) != len(answer) - 1:
        return 'Answer should be a single complete parse tree; you either have multiple trees, or your tree was prematurely closed'
      return None
    if fmt == 'parse strategy':
      if answer not in ['shift > reduce', 'reduce > shift']:
        return "Parse strategy must be either 'shift > reduce' or 'reduce > shift'"
      return None
    if fmt == 'HIGH or LOW':
      if answer.lower() not in ['high', 'low']:
        return "Must be either 'HIGH' or 'LOW'"
      return None
    if fmt == 'freeform text':
      if len(answer) < 1:
        return 'You need to write something'
      return None
  return "The declared answer format '" + fmt + "' is not recognized; you changed _FORMAT for this question"

def index_where_parse_tree_is_closed(parse_tree):
  if len(parse_tree) == 0 or parse_tree[0] != '(':
    return -1
  parens_to_close = 1
  for idx in range(1, len(parse_tree)):
    c = parse_tree[idx]
    if c == '(':
      parens_to_close += 1
    elif c == ')':
      parens_to_close -= 1
      if parens_to_close <= 0:
        return idx
  return -1

if __name__ == '__main__':
  question_names = locals().keys()
  question_names = [x for x in question_names if '__' not in x]
  question_names = [x for x in question_names if '_ANSWER' in x]
  question_names = [x.replace('_ANSWER', '') for x in question_names]
  question_formats = {}
  for x in question_names:
    question_formats[x] = locals()[x + '_FORMAT']
  question_answers = {}
  for x in question_names:
    question_answers[x] = locals()[x + '_ANSWER']
  unanswered_questions = set()
  for question,answer in question_answers.items():
    if answer == 'FILLIN':
      print 'Need to answer question: ' + question
      unanswered_questions.add(question)
  for question,fmt in question_formats.items():
    if question in unanswered_questions:
      continue
    format_error = have_format_error(question_answers[question], fmt)
    if format_error:
      print 'Not in correct format: ' + question + ': ' + format_error

