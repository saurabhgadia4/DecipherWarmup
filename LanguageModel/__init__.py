import os
import subprocess
import logging
from langParam import *
import re
import sys
from string import ascii_lowercase
from compute import *
import scoring
if __name__=="__main__":

    try:
        deleteFiles(files=CORP_SUP_FILES)
        for l in ascii_lowercase:
            computeMat[l] = {}
        computeMat['.'] = {}
        # #1. splitting file by words
        command = "tr -sc \'A-Za-z\.\' \'\012\' < " + CORPUS_FILE + ">" + CORPUS_WORDS
        ret = subprocess.call(command, shell=True)
        if(ret):
            print "Error"
            sys.exit(-1)
        print 'successfully created word file'

        # # #2. splitting words by char/line
        command = "cat " + CORPUS_WORDS + "| fold -w1 > " + CORPUS_CHARS
        ret = subprocess.call(command, shell=True)
        if(ret):
            print "Error"
            sys.exit(-1)
        print 'successfully created char file'

        # # #3. Shifting chars
        command = "tail --lines +2 " + CORPUS_CHARS + " > " + CORP_SHIFT 
        ret = subprocess.call(command, shell=True)
        if(ret):
            print "Error"
            sys.exit(-1)
        print 'successfully shifted char file'
        
        # # #4. Creating bigram train data
        command = "paste " + CORPUS_CHARS + " " + CORP_SHIFT + " > " + CORP_JOIN
        ret = subprocess.call(command, shell=True)
        if(ret):
            print "Error"
            sys.exit(-1)
        print 'successfully created bigram pair'

        # # #5. Calculating bigram count
        command = "sort " + CORP_JOIN + " | uniq -ic " + " | sort -r > " + CORP_STAT
        ret = subprocess.call(command, shell=True)
        if(ret):
            print "Error"
            sys.exit(-1)
        print 'successfully counted bigram pair'

        #6 removing lone '.' count
        command = "sed -i \' $ d\' " + CORP_STAT 
        ret = subprocess.call(command, shell=True)
        if(ret):
            print "Error"
            sys.exit(-1)
        print 'successfully removed bigram pair'
 
        #7. Extracting count for generating scoring matrix
        try:
            fp = open(CORP_STAT, "r")
            text = fp.readline()
            while(text):
                text = fp.readline()
                text = text.lstrip()
                text = text.split()
                if text:
                    computeMat[text[1]][text[2]] = int(text[0])
                    if int(text[0])<scoring.minCount:
                        scoring.minCount = int(text[0])
                        
        except Exception as err:
            logging.exception(err)

        for l in ascii_lowercase:
            command = "grep "+ l +" -o " + CORPUS_FILE + " | wc -l >> " + CHAR_COUNT
            ret = subprocess.call(command, shell=True)
            if(ret):
                print "Error"
                sys.exit(-1)
        startCountCmd = "grep "+ '\'\.\'' +" -o " + CORPUS_FILE + " | wc -l >> " + CHAR_COUNT    
        ret = subprocess.call(startCountCmd, shell=True)
        print 'successfully counted characters'

        try:
            fp = open(CHAR_COUNT, "r")
            for c in ascii_lowercase:
                text = fp.readline()
                totalCount[c] = int(text)
            text = fp.readline()
            totalCount['.'] = int(text)
        
        except Exception as err:
            logging.exception(err)
        

        #calculate conditional probabilities
        scoring.bigram(VALID_SENTENCE)
        scoring.bigram(TEST_SENTENCE)
        scoring.bigram(NEW_TEST)

    except Exception as e:
        logging.exception(e)
