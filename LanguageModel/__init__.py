import os
import subprocess
import logging
from langParam import *
import re
import sys
from string import ascii_lowercase
from compute import *
import scoring

def calculateBigram():
    try:
        deleteFiles(files=CORP_SUP_FILES)
        #calculate conditional probabilities
        scoring.bigram(VALID_SENTENCE)
        scoring.bigram(TEST_SENTENCE)
        scoring.bigram(NEW_TEST)

    except Exception as e:
        logging.exception(e)


if __name__=="__main__":
    calculateBigram()

