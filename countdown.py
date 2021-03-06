
import itertools
import collections
import re

value = {
    'a':1,
    'b':-1,
    'c':4,
    'd':2,
    'e':1,
    'f':4,
    'g':3,
    'h':3,
    'i':-1,
    'j':10,
    'k':-1,
    'l':2,
    'm':4,
    'n':2,
    'o':1,
    'p':-1,
    'q':10,
    'r':1,
    's':1,
    't':1,
    'u':2,
    'v':5,
    'w':-1,
    'x':8,
    'y':3,
    'z':10
    }


with open('/usr/share/dict/words') as f:
    all_words = set([line.lower() for line in f.read().splitlines()])

def permutations(letters):
    valid_words = collections.OrderedDict()
    for r in xrange(len(letters)):
        all_permutations = [''.join(p) for p in itertools.permutations(letters, r)]
        for word in [p for p in all_permutations
                     if p in all_words]:
            valid_words[word] = 1
    return valid_words

def print_perms(letters, regex=""):
    pattern = re.compile(regex)
    for w in permutations(letters):
        if pattern.search(w):
            print w
        
