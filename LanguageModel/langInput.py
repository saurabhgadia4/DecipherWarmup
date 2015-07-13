import os
import dcyParam
import langModels
import langSmooth
from dcyParam import *

class ProbMatrix():
    gramStub = {}
    gramStub[BIGRAM_TYPE] = {}
    gramStub[TRIGRAM_TYPE] = {}
    gramStub[BIGRAM_TYPE]['obj'] = langModels.BigramModel()
    gramStub[BIGRAM_TYPE]['mat'] = gramStub[BIGRAM_TYPE]['obj'].getScoreMat()
    gramStub[TRIGRAM_TYPE]['obj'] = langModels.TrigramModel()
    gramStub[TRIGRAM_TYPE]['mat'] = gramStub[TRIGRAM_TYPE]['obj'].getScoreMat()
    smoothHndl = langSmooth.LinearInt(gramStub[TRIGRAM_TYPE]['mat'], gramStub[BIGRAM_TYPE]['mat'], gramStub[BIGRAM_TYPE]['obj'].totalCount, gramStub[BIGRAM_TYPE]['obj'].total)

    @classmethod
    def getPossibility(cls, prefix, current, gramtype):
        possibility = 1
        try:
            if gramtype == BIGRAM_TYPE:
                possibility = cls.smoothHndl.biSmooth(prefix, current)
            elif gramtype == TRIGRAM_TYPE:
                possibility = cls.smoothHndl.triSmooth(prefix, current)
        except Exception as e:
            print 'Exception in calculating possiblility: ', e
        return possibility

class RowInput():
    def __init__(self, input):
        self.__elem = list(input)
        self.__ctop = {}
        self.__fill__ctop()

    def getElement(self, position):
        return self.__elem[position]

    def __fill__ctop(self):
        for i in range(len(self.__elem)):
            try:
                self.__ctop[self.__elem[i]].append(i)
            except KeyError:
                self.__ctop[self.__elem[i]] = []
                self.__ctop[self.__elem[i]].append(i)

    def __rm_ctop(self, position):
        element = self.__elem[position]
        self.__ctop[element].remove(position)

    def getPrefix(self, pfxlist):
        prefix = ""
        for idx in pfxlist:
            prefix+=self.__elem[idx]
        return prefix

    def __floodProbList(self, element, prob, probList):
        if self.__ctop.get(element, None):
            for pos in self.__ctop[element]:
                probList[pos] = prob

    def getRemProb(self, pfxIdxList, posList, gramtype):
        probList = []
        prefix = self.getPrefix(pfxIdxList)
        for i in range(50):
            probList.append(0)
        
        for pos in posList:
            if not probList[pos]:
                element = self.__elem[pos]
                prob = ProbMatrix.getPossibility(prefix, element, gramtype)
                self.__floodProbList(element, prob, probList)
        return probList

    def removeCol(self, columnIdx):
        self.__rm_ctop(columnIdx)

