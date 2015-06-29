import logging
import langParam
from strings import ascii_lowercase

class Unigram():
    def __init__(self):
        pass

class Bigram():
    def __init__(self):
        self.computeMat = {}
        self.computeMat['.'] = {}

    def initMatrix(self):
        for l in ascii_lowercase:
            self.computeMat[l] = {}

    def genScoreMatrix(self):
        #7. Extracting count for generating scoring matrix
        try:
            fp = open(CORP_STAT, "r")
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

    def calculateBigram():
    try:
        scoring.bigram(VALID_SENTENCE)
        scoring.bigram(TEST_SENTENCE)
        scoring.bigram(NEW_TEST)
    except Exception as e:
        logging.exception(e)

class Trigram():
    def __init__(self):
        pass