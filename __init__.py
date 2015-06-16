import os
import nltk
import re
from string import ascii_lowercase
from dcyParam import *
if __name__=='__main__':
    print 'starting pairs',STARTING_PAIR
    print 'adjacent pairs',ADJACENT_PAIR











    '''
    #for finding adjacent possible pairs
    pair = {}
    fp = open("adj.txt","a")
    wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()] 
    for i in ascii_lowercase:
        pair[i] = []
        for j in ascii_lowercase:
            prefix = i+j
            try:
                for w in wordlist:
                    if w.__contains__(prefix) and not w.startswith(prefix):
                        pair[i].append(j)
                        break

            except Exception as e:
                print prefix
    print pair
    for key in pair:
        fp.write(str(key))
        fp.write('=')
        fp.write(str(pair[key]))
        fp.write('\n')
    
    fp.close()
'''

