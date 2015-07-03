import os
import dcyParam
import langModels

class ProbMatrix():
    gramStub = {}
    gramStub[BIGRAM_TYPE] = {}
    gramStub[TRIGRAM_TYPE] = {}
    gramStub[BIGRAM_TYPE]['obj'] = langModels.BigramModel()
    gramStub[BIGRAM_TYPE]['mat'] = gramStub[BIGRAM_TYPE]['obj'].genScoreMatrix()
    gramStub[TRIGRAM_TYPE]['obj'] = langModels.TrigramModel()
    gramStub[TRIGRAM_TYPE]['mat'] = gramStub[TRIGRAM_TYPE]['obj'].genScoreMatrix()

    @classmethod
    def getPossibility(cls, prefix, current, gramtype):
        try:
            condCount = cls.gramStub[gramtype]['mat'][prefix][current]
            if gramtype == BIGRAM_TYPE:
                prefixCount = cls.gramStub[BIGRAM_TYPE]['obj'].totalCount[prefix] 
            elif gramtype == TRIGRAM_TYPE:
                biprefix = prefix[0]
                bicurrent = prefix[1]
                prefixCount = cls.gramStub[BIGRAM_TYPE]['mat'][biprefix][bicurrent]
            possibility = possibility*(float(condCount)/prefixCount)

        except KeyError:
            condCount = cls.gramStub[gramtype]['mat'][prefix][current] = cls.gramStub[gramtype]['obj'].minCount
            if gramtype == BIGRAM_TYPE:
                prefixCount = cls.gramStub[BIGRAM_TYPE]['obj'].totalCount[prefix] 
            elif gramtype == TRIGRAM_TYPE:
                biprefix = prefix[0]
                bicurrent = prefix[1]
                prefixCount = cls.gramStub[BIGRAM_TYPE]['mat'][biprefix][bicurrent]
            possibility = possibility*(float(condCount)/prefixCount)

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

    # def getPrefix(self, nextpos, type):
    #     prefix = ""
    #     for i in range(nextpos-type, nextpos):
    #         prefix+=self.__elem[i]
    #     return prefix

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
        prefix = getPrefix(pfxIdxList)
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

