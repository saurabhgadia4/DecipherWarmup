import os
import subprocess
import logging
from langParam import *
import re
import sys
from string import ascii_lowercase
if __name__=="__main__":

    try:
        computeMat = {}
        for l in ascii_lowercase:
            computeMat[l] = {}
        computeMat['.'] = {}
        # #1. splitting file by words
        # command = "tr -sc \'A-Za-z\.\' \'\012\' < " + CORPUS_FILE + ">" + CORPUS_WORDS
        # ret = subprocess.call(command, shell=True)
        # if(ret):
        #     print "Error"
        #     sys.exit(-1)
        # print 'successfully created word file'

        # #2. splitting words by char/line
        # command = "cat " + CORPUS_WORDS + "| fold -w1 > " + CORPUS_CHARS
        # ret = subprocess.call(command, shell=True)
        # if(ret):
        #     print "Error"
        #     sys.exit(-1)
        # print 'successfully created char file'

        # #3. Shifting chars
        # command = "tail --lines +2 " + CORPUS_CHARS + " > " + CORP_SHIFT 
        # ret = subprocess.call(command, shell=True)
        # if(ret):
        #     print "Error"
        #     sys.exit(-1)
        # print 'successfully shifted char file'
        
        # #4. Creating bigram train data
        # command = "paste " + CORPUS_CHARS + " " + CORP_SHIFT + " > " + CORP_JOIN
        # ret = subprocess.call(command, shell=True)
        # if(ret):
        #     print "Error"
        #     sys.exit(-1)
        # print 'successfully created bigram pair'

        # #5. Calculating bigram count
        # command = "sort " + CORP_JOIN + " | uniq -ic " + " | sort -r > " + CORP_STAT
        # ret = subprocess.call(command, shell=True)
        # if(ret):
        #     print "Error"
        #     sys.exit(-1)
        # print 'successfully counted bigram pair'

        #6. Extracting count for generating scoring matrix
        
        try:
            fp = open(CORP_STAT, "r")
            text = fp.readline()
            while(text):
                text = fp.readline()
                text = text.lstrip()
                text = text.split()
                computeMat[text[1]] =
        except Exception as err:
            logging.exception(err)

    except Exception as e:
        logging.exception(e)
