import os
import logging

def deleteFiles(path=None, files=[]):
    try:
        if not files:
            if path:
                files = os.listdir(path)
        for file in files:
            if os.path.exists(file):
                os.remove(file)
    except Exception as e:
        logging.exception(e)

def sentToWords():
# #1. splitting file by words
    try:
        if os.path.exists(CORPUS_FILE):
            if not os.path.exists(CORPUS_WORDS):
                command = "tr -sc \'A-Za-z\.\' \'\012\' < " + CORPUS_FILE + ">" + CORPUS_WORDS
                ret = subprocess.call(command, shell=True)
                if(ret):
                    print "Error"
                    sys.exit(-1)
                logging.info('successfully created word file')
            else:
                logging.info('Corpus word file already present')

        else:
            logging.info("Corpus File is missing")
    except Exception as e:
        logging.exception(e)

def wordsToChar():
# # #2. splitting words by char/line
    try:
        if not os.path.exists(CORPUS_CHARS):
            command = "cat " + CORPUS_WORDS + "| fold -w1 > " + CORPUS_CHARS
            ret = subprocess.call(command, shell=True)
            if(ret):
                print "Error"
                sys.exit(-1)
            logging.info('successfully created char file')
        else:
            logging.info("Character file already present")
    except Exception as e:
        logging.exception(e)

def shiftSequence(nchar, filename):
# # #3. Shifting chars
    try:
        if not os.path.exists(filename):
            command = "tail --lines +"+ str(nchar) +" "+ CORPUS_CHARS + " > " + filename 
            ret = subprocess.call(command, shell=True)
            if(ret):
                print "Error"
                sys.exit(-1)
            logging.info('Successfully shifted char file')
        else:
            logging.info("Required sequence file already present")
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
        command = "grep "+ l +" -o " + CORPUS_FILE + " | wc -l >> " + CHAR_COUNT
        ret = subprocess.call(command, shell=True)
        if(ret):
            print "Error"
            sys.exit(-1)
    startCountCmd = "grep "+ '\'\.\'' +" -o " + CORPUS_FILE + " | wc -l >> " + CHAR_COUNT    
    ret = subprocess.call(startCountCmd, shell=True)
    print 'successfully counted characters'

def storeCharCount():
    try:
        fp = open(CHAR_COUNT, "r")
        for c in ascii_lowercase:
            text = fp.readline()
            totalBiCount[c] = int(text)
        text = fp.readline()
        totalBiCount['.'] = int(text)
    
    except Exception as err:
        logging.exception(err)

