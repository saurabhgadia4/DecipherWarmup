import os
import sets
import langInput
class Driver():
    def __init__(self, cipher):
        self.remcol = sets.Set()
        self.rowobj = []
        self.cipher = cipher
        self.rowCount = len(cipher)
        self.__sequence = []
        self.rowlen = 50

    def __initRemSet(self):
        for i in range(self.rowlen):
            self.remcol.add(i) 

    def __chooseIdx(self, matrix):
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
        maxval = 0
        idx = -1
        for idx in range(len(problist)):
            if problist[idx] > maxval:
                maxval = problist[idx]
                idx = idx
        return idx

    def genSequence(self, startIdx):
        self.getFirstIndex(startIdx)
        remlen = len(self.remcol)
        while remlen:
            idx = getNextIdx(TRIGRAM_TYPE)
            self.updateRem(idx)
            remlen = len(self.remcol)

    def getPrefixList(self, gramtype):
        pfxlist = []
        seqlen = len(self.__sequence)
        for i in range(seqlen-gramtype, seqlen):
            pfxlist.append(self.__sequence[i])
        return pfxlist

    def updateRem(self, index):
        self.__sequence.append(index)
        self.remcol.remove(idx)

    def getFirstIndex(self, index):
        self.remcol.remove(index)
        self.__sequence.append(index)
        idx = getNextIdx(BIGRAM_TYPE)
        self.updateRem(idx)

    def getNextIdx(self, gramtype):
        probmat = []
        pfxlist = getPrefixList(gramtype)
        for i in range(self.rowCount):
            probmat.append(self.rowobj[i].getRemProb(pfxlist, self.remcol, gramtype))
        idx = self.__chooseIdx(probmat)
        return idx

    def fillRowObj(self):
        for row in self.cipher:
            self.rowobj.append(langInput.RowInput(row))

    def decipher(self, startIdx):
        decipherText = []
        for rownum in self.rowCount:
            decipherText.append("")
        self.genSequence(startIdx)
        for idx in self.__sequence:
            for rownum in self.rowCount:
                seq = decipherText[rownum]
                seq+=cipher[rownum][idx]
                decipherText[rownum] = seq
