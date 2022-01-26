import pathlib
import collections


def count_unique_words(filename):
    with open(filename, 'r') as file:
        info = {}
        contents = file.read()
        lines = contents.split()
        lines = list(map(lambda s: s.strip().lower(), lines))
        lines = list(filter(lambda s: len(s) >= 1, lines))
        for word in lines:
            if word in info:
                info[word]["count"] += 1
            else:
                info[word] = {"word":word, "count": 1}
        #print(info)
        
        _list = list(info.values())
        
        #print(_list[:10])
        
        items = sorted(_list, key=lambda x: x['count'], reverse=True)
        
        #print(items)
        print(items[:10])
        
        



count_unique_words('hamlet.txt')  
    
"""
In this exercise, you'll write a function count_unique_words that prints the ten most common unique words from a text file.

def count_unique_words(filename):
    ...
Concretely, we'll be using hamlet.txt, a text file containing the full text of "The Tragedy of Hamlet, Prince of Denmark" released by Project Gutenberg under their license.

Your output might look like:

the 1109
and 763
of 735
to 673
I 514
a 499
in 455
my 443
you 423
HAMLET. 359"""