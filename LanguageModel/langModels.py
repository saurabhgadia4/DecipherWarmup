import logging
import re
import sys
import os
import subprocess
from string import ascii_lowercase
import langParam
import langCompute
import logging
import statistics


class UnigramModel():
    def __init__(self):
        self.totalCount = {}


class BigramModel():
    def __init__(self):
        self.computeMat = {}
        self.computeMat['.'] = {}
        self.unigramObj = UnigramModel()
        self.initMatrix()
        self.minCount = 999999
        self.totalCount = None

    def initMatrix(self):
        for l in ascii_lowercase:
            self.computeMat[l] = {}

    def genScoreMatrix(self):
        #7. Extracting count for generating scoring matrix
        try:
            fp = open(langParam.BIGRAM_STAT, "r")
            text = fp.readline()
            while(text):
                text = fp.readline()
                text = text.lstrip()
                text = text.split()
                if text:
                    self.computeMat[text[1]][text[2]] = int(text[0])
                    if int(text[0])<self.minCount:
                        self.minCount = int(text[0])
                        
        except Exception as err:
            logging.exception(err)

    def getScore(self):
        try:
            self.__bigram(langParam.VALID_SENTENCE)
            self.__bigram(langParam.TEST_SENTENCE)
            self.__bigram(langParam.NEW_TEST)
        except Exception as e:
            logging.exception(e)

    def __bigram(self, text):
        print 'minCount: ',self.minCount
        possibility = 1
        rowPoss = []
        for row in text:
            row = '.' + row
            rowPoss.append(self.__calCond(row))

        print 'rowPoss',rowPoss
        print 'max', max(rowPoss)
        print 'min', min(rowPoss)
        print 'avg', statistics.mean(rowPoss)

    def __calCond(self, row):
        possibility =1
        row = list(row)
        for i in range(1, len(row)):
            try:
                prefix = row[i-1]
                current = row[i]
                #print prefix,'-',current
                condCount = self.computeMat[prefix][current]
                prefixCount = self.totalCount[prefix]
                possibility = possibility*(float(condCount)/prefixCount)
                #print 'p(%r|%r)'%(current,prefix),'--> condCount: ',condCount, ' prefixCount: ', prefixCount, ' =', possibility 
            except KeyError:
                self.computeMat[prefix][current] = self.minCount
                prefixCount = self.totalCount[prefix]
                possibility = possibility*(float(condCount)/prefixCount)

        return possibility

    def cleanStat(self):
        #6 removing lone '.' count
        try:
            command = "sed -i \' $ d\' " + langParam.BIGRAM_STAT 
            ret = subprocess.call(command, shell=True)
            if(ret):
                print "Error"
                sys.exit(-1)
            print 'successfully removed bigram pair'
        except Exception as e:
            logging.exception(e)


    def generate(self):
        #1. Break sentence to words
        langCompute.sentToWords()

        #2. Break words to char
        langCompute.wordsToChar()

        #3. Shift by one character
        langCompute.shiftSequence(2, langParam.CORP_SHIFT_1)
        #4. Join character files
        langCompute.formPairs(langParam.BIGRAM_PAIR, langParam.CORPUS_CHARS, langParam.CORP_SHIFT_1)
        #5. Calculating bigram count
        langCompute.calPairCount(langParam.BIGRAM_PAIR, langParam.BIGRAM_STAT)  
        #6 Clean bigram stats
        self.cleanStat()
        #7. generate score matrix
        self.genScoreMatrix()
        #8. generate unigram score
        langCompute.genCharCount()
        #9. 
        self.totalCount = langCompute.getCharCount()
        #10 get the score
        self.getScore()
        langCompute.deleteFiles(files=langParam.BIGRAM_FILES)

class TrigramModel():
    def __init__(self):
        self.bigramStub = BigramModel()
        self.computeMat = {}
        self.computeMat['.'] = {}   