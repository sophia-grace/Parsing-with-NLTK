# Name: Sophia Trump
# File: assignment5.py
# Description: Parses sentences in the domain of animals and their properties.
# Last modified: Fri, 30 November 2018

import nltk
import urllib.request
import re

def main():
    # create the CFG
    grammar = nltk.CFG.fromstring(
   """
   S -> WH_NP VP
   S -> WH_NP AUXV NP VP
   S -> NP VP
   NP -> N | PRON | PROPN | AUXV NP | PREDET N | Det Nominal | Det Nominal PP 
   VP -> V | V ADJ | V WH_NP| V NP | V NP PP 
   PREDET -> Det | PREDET Det
   Nominal -> N | Nominal N
   PP -> P NP
   WH_NP -> WH_PRON
   WH_PRON -> "who" | "what"
   PRON -> "i"
   AUXV -> "does"
   PROPN -> "socrates" | "deepak" | "rover" | "snoopy" | "tweety" | "polly"
   ADJ -> "human" | "biped"
   V -> "saw" | "ate" | "is" | "has" | "swims" | "flies" | "fly" | "are" | "have" | "bite" | "bites" | "walk" | "walks" | "does"
   Det -> "a" | "the" | "an" | "all"
   N -> "man" | "dog" | "dogs" | "telescope" | "feathers" | "hair" | "park" | "collies" | "collie" | "beagles" | "beagle" | "parrots" | "parrot" | "canaries" | "canary" | "fish" | "animal" | "animals" | "bird" | "birds" | "gills" | "mammals" | "humans" | "canines"
   P -> "in" | "under" | "with"
   """)

    # create the parser
    RDparser = nltk.RecursiveDescentParser(grammar)
    
    # get the sentences 
    sentences = getSents()

    # tag each word in each sentence
    parsedSents = []
    for sent in sentences:
        for p in RDparser.parse_one(sent):
            print(p)
        print("\n")

# formats the sentences as acceptable to parser (i.e., as a list of tokenized sentences)
def getSents():
    sents = []
    
    page_source = urllib.request.urlopen('https://cs.brynmawr.edu/Courses/cs325/fall2018/test2.txt').read().decode('utf-8')
    lines = re.sub('\r|\?|\.|\n', '\n', page_source)
    lines = re.split('\n', lines)
    for l in lines:
        if l:
           l = l.lower()
           words = nltk.word_tokenize(l)
           sents.append(words)
    return sents





    
