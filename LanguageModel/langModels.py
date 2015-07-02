import logging
import re
import sys
import os
import subprocess
from string import ascii_lowercase
from DecipherWarmup import langParam
import langCompute
import logging
import statistics


class UnigramModel():
    def __init__(self):
        self.totalCount = {}


class BigramModel():
    def __init__(self):
        self.computeMat = {}
        self.__initMatrix()
        self.minCount = 999999
        self.totalCount = None

    def __initMatrix(self):
        self.computeMat['.'] = {}
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
        possibility = 1
        rowPoss = []
        for row in text:
            row = '.' + row
            rowPoss.append(self.__calCond(row))
        print '\n\n--------------New Record----------------'
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
                condCount = self.computeMat[prefix][current] = self.minCount
                prefixCount = self.totalCount[prefix]
                possibility = possibility*(float(condCount)/prefixCount)

        return possibility

    def getScoreMat(self):
        #1. Break sentence to words
        langCompute.sentToWords()

        #2. Break words to char
        langCompute.wordsToChar()

        #3. Shift by one character
        langCompute.shiftSequence(2, langParam.CORP_SHIFT_1)
        #4. Join character files
        langCompute.formPairs(langParam.BIGRAM_PAIR_TEMP, langParam.CORPUS_CHARS, langParam.CORP_SHIFT_1)
        #5 Clean bigram stats
        langCompute.removeLastLines(1, langParam.BIGRAM_PAIR_TEMP, langParam.BIGRAM_PAIR)
        #6. Calculating bigram count
        langCompute.calPairCount(langParam.BIGRAM_PAIR, langParam.BIGRAM_STAT)  
        
        #7. generate score matrix
        self.genScoreMatrix()

    def generate(self):
        self.getScoreMat()
        #8. generate unigram score
        langCompute.genCharCount()
        #9. 
        self.totalCount = langCompute.getCharCount()
        #10 get the score
        self.getScore()
        #langCompute.deleteFiles(files=langParam.BIGRAM_FILES)

class TrigramModel():
    def __init__(self):
        self.bigramStub = BigramModel()
        self.computeMat = {}
        self.__initMatrix()
        self.minCount = 9999999

    def __initMatrix(self):
        self.computeMat['..'] = {}
        for l in ascii_lowercase:
            for m in ascii_lowercase:
                text = l+m
                self.computeMat[text]={}
            periodText = '.'+l
            revperiodText = l+'.'
            self.computeMat[periodText] = {}
            self.computeMat[revperiodText] = {}

    def getScoreMat(self):
        self.bigramStub.generate()
        #3. Shift by one character
        langCompute.shiftSequence(3, langParam.CORP_SHIFT_2)
        #4. Join character files
        langCompute.formPairs(langParam.TRIGRAM_PAIR_TEMP, langParam.CORPUS_CHARS, langParam.CORP_SHIFT_1, langParam.CORP_SHIFT_2)
        #5 Clean bigram stats
        langCompute.removeLastLines(2, langParam.TRIGRAM_PAIR_TEMP, langParam.TRIGRAM_PAIR)

        #6. Calculating bigram count
        langCompute.calPairCount(langParam.TRIGRAM_PAIR, langParam.TRIGRAM_STAT)  

        self.genScoreMatrix()
        self.getScore()

    def genScoreMatrix(self):
        #7. Extracting count for generating scoring matrix
        try:
            fp = open(langParam.TRIGRAM_STAT, "r")
            text = fp.readline()
            while(text):
                text = fp.readline()
                text = text.lstrip()
                text = text.split()
                if text:
                    prefix = text[1] + text[2]
                    self.computeMat[prefix][text[3]] = int(text[0])
                    if int(text[0])<self.minCount:
                        self.minCount = int(text[0])
                        
        except Exception as err:
            logging.exception(err)

    def getScore(self):
        try:
            print '..........................TRIGRAM STATS.............................'
            self.__trigram(langParam.VALID_SENTENCE)
            self.__trigram(langParam.TEST_SENTENCE)
            self.__trigram(langParam.NEW_TEST)
        except Exception as e:
            logging.exception(e)

    def __trigram(self, text):
        possibility = 1
        rowPoss = []
        for row in text:
            row = '.' + row
            rowPoss.append(self.__calCond(row))

        print '\n\n--------------New Record----------------'
        print 'rowPoss',rowPoss
        print 'max', max(rowPoss)
        print 'min', min(rowPoss)
        print 'avg', statistics.mean(rowPoss)

    def __calCond(self, row):
        possibility =1
        row = list(row)
        for i in range(1, len(row)-1):
            try:
                triPrefix = row[i-1] + row[i]
                triCurrent = row[i+1]
                biPrefix = row[i-1]
                biCurrent = row[i]
                #print prefix,'-',current
                condCount = self.computeMat[triPrefix][triCurrent]
                prefixCount = self.bigramStub.computeMat[biPrefix][biCurrent]
                possibility = possibility*(float(condCount)/prefixCount)
                #print 'p(%r|%r)'%(current,prefix),'--> condCount: ',condCount, ' prefixCount: ', prefixCount, ' =', possibility 
            except KeyError:
                biPrefix = row[i-1]
                biCurrent = row[i]
                condCount = self.computeMat[triPrefix][triCurrent] = self.minCount
                prefixCount = self.bigramStub.computeMat[biPrefix][biCurrent]
                possibility = possibility*(float(condCount)/prefixCount)

        return possibility


    def generate(self):
        self.getScoreMat()
        langCompute.deleteFiles(files=langParam.TRIGRAM_FILES)
        langCompute.deleteFiles(files=langParam.BIGRAM_FILES)