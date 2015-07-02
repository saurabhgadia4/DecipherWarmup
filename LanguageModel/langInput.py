import os
import dcyParam
import langModels

class ProbMatrix():
    bigramObject = langModels.BigramModel()
    trigramObject = langModels.TrigramModel()
    bigramMatrix = bigramObject.genScoreMatrix()
    trigramMatrix = trigramObject.genScoreMatrix()

    @classmethod
    def getPossibility(cls, prefix, current, gramtype):
        

class RowInput():
    def __init__(self, input):
        self.__elem = list(input)
        self.ctop = {}
        self.__fillctop()

    def getElement(self, position):
        return self.__elem[position]

    def __fillctop(self):
        for i in range(len(self.__elem)):
            try:
                self.ctop[self.__elem[i]].append(i)
            except KeyError:
                self.ctop[self.__elem[i]] = []
                self.ctop[self.__elem[i]].append(i)

    def getPrefix(self, nextpos, type):
        prefix = ""
        for i in range(nextpos-type, nextpos):
            prefix+=self.__elem[i]
        return prefix

    def getRemProb(self, prefix, posList, gramtype):
        probList = []
        for i in range(50):
            probList.append(0)
        if gramtype == BIGRAM_TYPE:
            gramobj = ProbMatrix.bigramObject
            grammat = ProbMatrix.bigramMatrix
        elif gramtype == TRIGRAM_TYPE:
            gramobj =  ProbMatrix.trigramObject
            grammat = ProbMatrix.trigramMatrix

        for pos in posList:
            if not probList[pos]:
                element = self.__elem[pos]


                
                condCount = grammat[prefix][element]
                prefixCount = self.totalCount[prefix]
                possibility = possibility*(float(condCount)/prefixCount)
                #print 'p(%r|%r)'%(current,prefix),'--> condCount: ',condCount, ' prefixCount: ', prefixCount, ' =', possibility 
            except KeyError:
                if gramtype == BIGRAM_TYPE:
                    pass
                elif gramtype == TRIGRAM_TYPE:
                    pass



                condCount = self.computeMat[prefix][current] = self.minCount
                prefixCount = self.totalCount[prefix]
                possibility = possibility*(float(condCount)/prefixCount)


            except KeyError:
                biPrefix = row[i-1]
                biCurrent = row[i]
                condCount = self.computeMat[triPrefix][triCurrent] = self.minCount
                prefixCount = self.bigramStub.computeMat[biPrefix][biCurrent]
                possibility = possibility*(float(condCount)/prefixCount)








