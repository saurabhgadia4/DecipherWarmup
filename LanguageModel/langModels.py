import logging
import langParam
from strings import ascii_lowercase
import langCompute
import langParam

class UnigramModel():
    def __init__(self):
        pass

class BigramModel():
    def __init__(self):
        self.computeMat = {}
        self.computeMat['.'] = {}

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
                    computeBiMat[text[1]][text[2]] = int(text[0])
                    if int(text[0])<scoring.minCount:
                        scoring.minCount = int(text[0])
                        
        except Exception as err:
            logging.exception(err)

    def getBigramScore():
    try:
        scoring.bigram(VALID_SENTENCE)
        scoring.bigram(TEST_SENTENCE)
        scoring.bigram(NEW_TEST)
    except Exception as e:
        logging.exception(e)

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
        langCompute.shiftSequence(1, langParam.CORP_SHIFT_1)
        #4. Join character files
        langCompute.formPairs(langParam.BIGRAM_PAIR, langParam.CORPUS_CHARS, langParam.CORP_SHIFT_1)
        #5. Calculating bigram count
        langCOmpute.calPairCount(langParam.BIGRAM_PAIR, langParam.BIGRAM_STAT)  
        #6 Clean bigram stats
        self.cleanStat()
        #7. generate score matrix
        self.genScoreMatrix()



class TrigramModel():
    def __init__(self):
        self.bigramStub = BigramModel()
        self.computeMat = {}
        self.computeMat['.'] = {}   