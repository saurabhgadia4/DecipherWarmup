import os
import logging
import subprocess
import sys
import shutil
from dcyParam import * 
from string import ascii_lowercase

def deleteFiles(path=None, files=[]):
    try:
        if not files:
            if path:
                files = os.listdir(path)
        for file in files:
            if os.path.exists(file):
                os.remove(file)
        logging.info("successfully deleted files")
    except Exception as e:
        logging.exception(e)

def truncExpr(expr, inputfile, outputfile):
    try:
        command = "tr -s \'" + expr + " \' < " + inputfile + " > " + outputfile
        ret = subprocess.call(command, shell=True)
        if(ret):
            print "Error"
            sys.exit(-1)
        logging.info('successfully removed extra space chatacters')
    except Exception as e:
        logging.exception(e)

def sentToWords():
# #1. splitting file by words
    try:
        truncExpr('\. ', CORPUS_FILE, CORPUS_CLEAN)
        command = "tr -sc \'A-Za-z\.\' \'\012\' < " + CORPUS_CLEAN + ">" + CORPUS_WORDS
        ret = subprocess.call(command, shell=True)
        if(ret):
            print "Error"
            sys.exit(-1)
        logging.info('successfully created word file')
    
    except Exception as e:
        logging.exception(e)

def wordsToChar():
# # #2. splitting words by char/line
    try:
        command = "cat " + CORPUS_WORDS + "| fold -w1 > " + CORPUS_CHARS
        ret = subprocess.call(command, shell=True)
        if(ret):
            print "Error"
            sys.exit(-1)
        logging.info('successfully created char file')
    except Exception as e:
        logging.exception(e)

def shiftSequence(nchar, filename):
# # #3. Shifting chars
    try:
        
        command = "tail --lines +"+ str(nchar) +" "+ CORPUS_CHARS + " > " + filename 
        ret = subprocess.call(command, shell=True)
        if(ret):
            print "Error"
            sys.exit(-1)
        logging.info('Successfully shifted char file')
    
    except Exception as e:
        logging.exception(e)

def formPairs(output, *args):
    try:
        files = " "
        for f in args:
            files = files + str(f) + " "

        command = "paste " + files + " > " + output
        ret = subprocess.call(command, shell=True)
        if(ret):
            print "Error"
            sys.exit(-1)
        logging.info('successfully created bigram pair')
    except Exception as e:
        logging.exception(e)

def calPairCount(inputfile, outputfile):
# # #5. Calculating bigram count
    command = "sort " + inputfile + " | uniq -ic " + " | sort -r > " + outputfile
    ret = subprocess.call(command, shell=True)
    if(ret):
        print "Error"
        sys.exit(-1)
    print 'successfully counted bigram pair'

def cleanStats():
#6 removing lone '.' count
    command = "sed -i \' $ d\' " + CORP_STAT 
    ret = subprocess.call(command, shell=True)
    if(ret):
        print "Error"
        sys.exit(-1)
    print 'successfully removed bigram pair'

def genCharCount():
    for l in ascii_lowercase:
        command = "grep "+ l +" -o " + CORPUS_FILE + " | wc -l >> " + UNIGRAM_STAT
        ret = subprocess.call(command, shell=True)
        if(ret):
            print "Error"
            sys.exit(-1)
    startCountCmd = "grep "+ '\'\.\'' +" -o " + CORPUS_FILE + " | wc -l >> " + UNIGRAM_STAT    
    ret = subprocess.call(startCountCmd, shell=True)
    print 'successfully counted characters'

def getCharCount():
        totalCount = {}
        total = 0
        try:
            fp = open(UNIGRAM_STAT, "r")
            for c in ascii_lowercase:
                text = fp.readline()
                totalCount[c] = int(text)
                total+=totalCount[c]
            text = fp.readline()
            totalCount['.'] = int(text)
        except Exception as err:
            logging.exception(err)
        return totalCount, total

def removeLastLines(nlines, inputfile, outputfile):
        #6 removing lone '.' count
        try:
            command = "head -n -" + str(nlines) +" "+inputfile + " > " + outputfile
            ret = subprocess.call(command, shell=True)
            if(ret):
                print "Error"
                sys.exit(-1)
            print 'successfully removed ',nlines, 'from ',inputfile
        except Exception as e:
            logging.exception(e)
