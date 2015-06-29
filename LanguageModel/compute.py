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
    command = "tr -sc \'A-Za-z\.\' \'\012\' < " + CORPUS_FILE + ">" + CORPUS_WORDS
    ret = subprocess.call(command, shell=True)
    if(ret):
        print "Error"
        sys.exit(-1)
    print 'successfully created word file'

def wordsToChar():
# # #2. splitting words by char/line
    command = "cat " + CORPUS_WORDS + "| fold -w1 > " + CORPUS_CHARS
    ret = subprocess.call(command, shell=True)
    if(ret):
        print "Error"
        sys.exit(-1)
    print 'successfully created char file'

def shiftSequence(nchar, filename):
# # #3. Shifting chars
    command = "tail --lines +"+ str(nchar) +" "+ CORPUS_CHARS + " > " + filename 
    ret = subprocess.call(command, shell=True)
    if(ret):
        print "Error"
        sys.exit(-1)
    print 'successfully shifted char file'

def formPairs(output, *args):
    files = " "
    for f in args:
        files = files + str(f) + " "

    command = "paste " + files + " > " + output
    ret = subprocess.call(command, shell=True)
    if(ret):
        print "Error"
        sys.exit(-1)
    print 'successfully created bigram pair'

def calcPairCount(filename, output):
# # #5. Calculating bigram count
    command = "sort " + filename + " | uniq -ic " + " | sort -r > " + output
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

