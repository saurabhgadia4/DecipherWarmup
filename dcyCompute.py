import os
import nltk
import re
from string import ascii_lowercase
from dcyParam import *

def pairCount():
    wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()] 
        startDict = {}
        adjDict = {}
        print 'Total Word Count:', len(wordlist)
        count = 0
        #fp = open("condProb.txt","a")
        for l in ascii_lowercase:
            startDict[l] = {}
            adjDict[l] = {}

        for w in wordlist:
            count+=1
            #print 'Word:',w, ' Count:',count
            for i in ascii_lowercase:
                isStart = False
                doesContain = False
                for j in ascii_lowercase:
                    prefix = i+j;
                    isStart = w.startswith(prefix)
                    doesContain = w.__contains__(prefix)
                    if isStart:
                        if startDict[i].get(j,None):
                            startDict[i][j] += 1
                        else:
                            startDict[i][j] = 1

                    if doesContain:
                        if adjDict[i].get(j, None):
                            adjDict[i][j] += 1
                        else:
                            adjDict[i][j] = 1

                    isStart = False
                    doesContain = False
        print startDict
        print adjDict