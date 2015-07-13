import logging
import re
import sys
import os
import subprocess
from string import ascii_lowercase
import dcyParam
import langCompute
import logging
import langSmooth
import statistics


class UnigramModel():
    def __init__(self):
        self.totalCount = {}
        self.total = 0

    def genUniStat(self):
        self.totalCount, self.total = langCompute.getCharCount()

class BigramModel(UnigramModel):
    def __init__(self):
        UnigramModel.__init__(self)
        self.computeMat = {}
        self.__initMatrix()
        self.minCount = 999999

    def __initMatrix(self):
        self.computeMat['.'] = {}
        for l in ascii_lowercase:
            self.computeMat[l] = {}

    def genScoreMatrix(self):
        #7. Extracting count for generating scoring matrix
        try:
            fp = open(dcyParam.BIGRAM_STAT, "r")
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
        return self.computeMat

    def getScore(self, text):
        try:
            # self.__bigram(dcyParam.VALID_SENTENCE)
            # self.__bigram(dcyParam.TEST_SENTENCE)
            # self.__bigram(dcyParam.NEW_TEST)
            rowPoss = self.__bigram(text)
        except Exception as e:
            logging.exception(e)
        return rowPoss

    def __bigram(self, text):
        possibility = 1
        rowPoss = []
        self.scoring =  langSmooth.Scoring(None, self.computeMat, self.totalCount, self.total)
        for row in text:
            row = '.' + row
            rowPoss.append(self.scoring.bigramScore(row))
        return rowPoss

    def getScoreMat(self):
        #1. Break sentence to words
        langCompute.sentToWords()

        #2. Break words to char
        langCompute.wordsToChar()

        #3. Shift by one character
        langCompute.shiftSequence(2, dcyParam.CORP_SHIFT_1)
        #4. Join character files
        langCompute.formPairs(dcyParam.BIGRAM_PAIR_TEMP, dcyParam.CORPUS_CHARS, dcyParam.CORP_SHIFT_1)
        #5 Clean bigram stats
        langCompute.removeLastLines(1, dcyParam.BIGRAM_PAIR_TEMP, dcyParam.BIGRAM_PAIR)
        #6. Calculating bigram count
        langCompute.calPairCount(dcyParam.BIGRAM_PAIR, dcyParam.BIGRAM_STAT) 
        #7 Generate unigram stat
        langCompute.genCharCount() 
        
        #generating total count
        self.genUniStat()
        #7. generate score matrix

        return self.genScoreMatrix()

    def generate(self):
        self.getScoreMat()
        #8. generate unigram score
#        langCompute.genCharCount()
        #9. 
        
        #10 get the score
        #self.getScore()
        #langCompute.deleteFiles(files=dcyParam.BIGRAM_FILES)

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
        langCompute.shiftSequence(3, dcyParam.CORP_SHIFT_2)
        #4. Join character files
        langCompute.formPairs(dcyParam.TRIGRAM_PAIR_TEMP, dcyParam.CORPUS_CHARS, dcyParam.CORP_SHIFT_1, dcyParam.CORP_SHIFT_2)
        #5 Clean bigram stats
        langCompute.removeLastLines(2, dcyParam.TRIGRAM_PAIR_TEMP, dcyParam.TRIGRAM_PAIR)

        #6. Calculating bigram count
        langCompute.calPairCount(dcyParam.TRIGRAM_PAIR, dcyParam.TRIGRAM_STAT)  

        return self.genScoreMatrix()
        #self.getScore()

    def genScoreMatrix(self):
        #7. Extracting count for generating scoring matrix
        try:
            fp = open(dcyParam.TRIGRAM_STAT, "r")
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
        return self.computeMat

    def getScore(self, text):
        try:
            rowPoss = self.__trigram(text)
        except Exception as e:
            logging.exception(e)
        return rowPoss

    def __trigram(self, text):
        possibility = 1
        rowPoss = []
        self.scoring = langSmooth.Scoring(self.computeMat, self.bigramStub.computeMat, self.bigramStub.totalCount, self.bigramStub.total)
        for row in text:
            row = '.' + row
            rowPoss.append(self.scoring.trigramScore(row))
        return rowPoss

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
        langCompute.deleteFiles(files=dcyParam.TRIGRAM_FILES)
        langCompute.deleteFiles(files=dcyParam.BIGRAM_FILES)