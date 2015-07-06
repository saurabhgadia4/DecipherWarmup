import os
import sets
import langInput
from dcyParam import *

class Driver():
    def __init__(self, cipher):
        self.rowlen = 50
        self.cipher = cipher
        self.__sequence = []
        self.rowCount = len(cipher)
        self.remcol = sets.Set()
        self.__initRemSet()
        self.rowobj = []
        self.__fillRowObj()

    def __initRemSet(self):
        for i in range(self.rowlen):
            self.remcol.add(i) 

    def __chooseIdx(self, matrix):
        #print 'matrix', matrix
        problist = []
        for i in range(50):
            problist.append(0)
        for idx in self.remcol:
            result = 1
            for rownum in range(self.rowCount):
                result*=matrix[rownum][idx]
            problist[idx] = result
        return self.__getMaxIdx(problist)

    def __getMaxIdx(self, problist):
        #print 'problist: ', problist
        #print 'max in list: ',max(problist)
        maxval = 0
        index = -1
        for idx in range(len(problist)):
            if problist[idx] > maxval:
                maxval = problist[idx]
                index = idx
        #print 'my max: ',maxval
        return index

    def getPrefixList(self, gramtype):
        pfxlist = []
        seqlen = len(self.__sequence)
        for i in range(seqlen-gramtype, seqlen):
            pfxlist.append(self.__sequence[i])
        return pfxlist

    def updateRem(self, index):
        #print 'next selected index', index
        self.__sequence.append(index)
        self.remcol.remove(index)

    def genSequence(self, startIdx):
        self.getFirstIndex(startIdx)
        remlen = len(self.remcol)
        while remlen:
            idx = self.getNextIdx(TRIGRAM_TYPE)
            self.updateRem(idx)
            remlen = len(self.remcol)

    def getFirstIndex(self, index):
        self.updateRem(index)
        idx = self.getNextIdx(BIGRAM_TYPE)
        self.updateRem(idx)

    def getNextIdx(self, gramtype):
        probmat = []
        pfxlist = self.getPrefixList(gramtype)
        for i in range(self.rowCount):
            probmat.append(self.rowobj[i].getRemProb(pfxlist, self.remcol, gramtype))
        idx = self.__chooseIdx(probmat)
        return idx

    def __fillRowObj(self):
        for row in self.cipher:
            self.rowobj.append(langInput.RowInput(row))

    def decipher(self, startIdx):
        decipherText = []
        for rownum in range(self.rowCount):
            decipherText.append("")
        self.genSequence(startIdx)
        for idx in self.__sequence:
            for rownum in range(self.rowCount):
                seq = decipherText[rownum]
                seq+=self.cipher[rownum][idx]
                decipherText[rownum] = seq
        print 'score of decipher text: '
        langInput.ProbMatrix.gramStub[BIGRAM_TYPE]['obj'].getScore(decipherText)
        langInput.ProbMatrix.gramStub[TRIGRAM_TYPE]['obj'].getScore(decipherText)
        return self.__sequence, decipherText
