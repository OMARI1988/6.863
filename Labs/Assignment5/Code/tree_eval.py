#!/usr/bin/env python2.5
#
# A utility class to compute the span (constituent)
# intersection between two parse trees.
# Example:
#
#  intersection_spans = spans_intersection_from_sexp(reference, parsed)
#
# where reference and parsed are s-expressions like (S (NP ...)).
# The returned intersection_spans is a list strings of the form:
#      <non-terminal>:[leaf words]
#
# - yks 2/19/2009
#
import nltk
import sys

def tree_from_sexp(sexp):
    """
    parses an s-expression into a tree
    """
    return nltk.bracket_parse(sexp)

def spans_from_sexp(sexp):
    """
    computes the set of spans given the s-expression
    """
    tree = nltk.bracket_parse(sexp)
    return spans_from_tree(tree)
    
def spans_from_tree(tree):
    """
    computes the set of spans
    <production> <tokens> given a treee.
    A span would be something like:
    NP\t[John loves Mary]

    """
    s = []
    if tree is not None:
	forest = tree.subtrees()
	for tree in forest:
	    s.append("%s\t%s" %(tree.productions()[0].lhs(), tree.leaves()))
    return s

def spans_intersection_from_sexp(sexp1, sexp2):
    """
    computes the span difference between two s-expressions
    """
    tree1 = nltk.bracket_parse(sexp1)
    tree2 = nltk.bracket_parse(sexp2)
    return spans_intersection(tree1, tree2)
    
def spans_intersection(tree1, tree2):
    """
    compute the span intersection between two trees
    """
    span1 = spans_from_tree(tree1)
    span2 = spans_from_tree(tree2)

    intersection = []
    for item1 in span1:
	if item1 in span2:
	    intersection.append(item1)
	    span2.remove(item1)
    return intersection

def test(reference, parsed):
    reference_spans = spans_from_sexp(reference)
    parsed_spans = spans_from_sexp(parsed)
    
    print "reference: %d constituents" %(len(reference_spans))
    print "parsed: %d constituents" %(len(parsed_spans))
    #print "reference spans: %s" %(reference_spans)
    #print "parsed spans: %s" %(parsed_spans)
    intersection_spans = spans_intersection_from_sexp(reference, parsed)
    print "common(reference, parsed): %d constituents"%(len(intersection_spans))
    print "common constituents"
    for const in intersection_spans:
	print "%s" %(const)

    intersect = len(intersection_spans) + 0.0
    print "precision: %f" %(intersect / len(parsed_spans))
    print "recall: %f" %(intersect / len(reference_spans))
    
if __name__ == "__main__":

    if len(sys.argv) > 2:
	reference_file = open(sys.argv[1])
	parsed_file = open(sys.argv[2])
	reference = reference_file.read()
	parsed = parsed_file.read()
    else:
	reference = """
(S (NP-SBJ (DT the) (NN luxury) (NN auto) (NN maker))
(NP-TMP (JJ last) (NN year))
(VP (VBD sold) (NP (CD 1,000) (NNS cars))
(PP-LOC (IN in)
(NP (DT the) (NNP U.S.) ))))
"""
	
	parsed = """
(S (NP-SBJ
(NP (DT the) (NN luxury) (NN auto))
    (NN maker)
    (JJ last)
    (NN year))
    (VP
    (VBN sold)
    (NP (CD 1,000) (NNS cars))
    (PP (IN in) (NP (DT the) (NNP U.S.)))))
"""
	
    test(reference, parsed)
    
