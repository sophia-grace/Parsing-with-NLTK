# Name: Sophia Trump
# File: assignment5.py
# Description: Parses sentences in the domain of animals and their properties.
#              Prints the parses and returns a list of parsed sentences.
#              Takes a list of parsed sentences (without punctuation) as input.
# First modified: Fri, 30 November 2018

import nltk
import urllib.request
import re

def main(sentences):
    
    # create the CFG
    grammar = nltk.CFG.fromstring(
   """
   S -> WH_NP VP
   S -> AuxV NP VP
   S -> AuxV NP NP
   S -> NP VP
   NP -> Nominal | PropN | PreDet NP | Det Nominal 
   VP -> V | V ADJ | V WH_NP | V NP
   Nominal -> N | Nominal N
   WH_NP -> WH_Pron
   PreDet -> "all"
   WH_Pron -> "who" | "what"
   AuxV -> "does" | "is"
   PropN -> "socrates" | "deepak" | "rover" | "snoopy" | "tweety" | "polly"
   ADJ -> "human" | "biped"
   V -> "saw" | "ate" | "is" | "has" | "swims" | "swim" | "flies" | "fly" | "are" | "have" | "bite" | "bites" | "walk" | "walks" | "does"
   Det -> "a" | "the" | "an" | "all"
   N -> "man" | "dog" | "dogs" | "telescope" | "feathers" | "hair" | "park" | "collies" | "collie" | "beagles" | "beagle" | "parrots" | "parrot" | "canaries" | "canary" | "fish" | "animal" | "animals" | "bird" | "birds" | "gills" | "mammals" | "humans" | "canines"
   """)

    # create the parser
    ECparser = nltk.parse.EarleyChartParser(grammar)

    # parse each sentence
    parsedSents = []
    for sent in sentences:
        for p in ECparser.parse(sent):
            print(p)
            parsedSents.append(p)
        print("\n")

    # return the list of parses
    return parsedSents;

# formats the sentences as acceptable to parser
def getSents():
    sents = []
    text = open('/home/strump/cs325/Assignment5/Parsing-with-NLTK/sentences.txt', 'r').readlines()

    for s in text:
        s = s.lower()
        line = re.sub('[1-5]|\.|\?|\n|(q)', '', s)
        words = nltk.word_tokenize(line)
        sents.append(words)

    return sents


# formats the extended test suite sentences as acceptable to parser (i.e., as a list of tokenized sentences)
def getExtendedSents():
    sents = []
    
    page_source = urllib.request.urlopen('https://cs.brynmawr.edu/Courses/cs325/fall2018/test2.txt').read().decode('utf-8')
    lines = re.sub('\r|\?|\.|\n|[Q]', '\n', page_source)
    lines = re.split('\n', lines)
    for l in lines:
        if l:
           l = l.lower()
           words = nltk.word_tokenize(l)
           sents.append(words)
    return sents







    
