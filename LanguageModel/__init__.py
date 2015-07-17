import math
import itertools
import langModels
import langDriver
import dcyParam
import langCompute

'''
def getScore(text):
	print '----------------------------Original sequence-----------------------------'
	origbiscore, origtriscore = driverobj.calScore(text)
	print 'biscore', origbiscore
	print 'triscore', origtriscore
	origsum = 0
	for j in range(dcyParam.TOTAL_ROWS):
			#print 'seq log',score[j]
			origsum+=math.log(origtriscore[j])
	print 'sum', origsum
'''

def printStat(allSeq, maxseq):
	print 'Maximum score sequence starting index', maxseq
	print 'Sequence', allSeq[maxseq]['seq']
	print 'sum', allSeq[maxseq]['sum']
	print langCompute.formText(CIPHER_TEXT, allSeq[maxseq]['seq'])
	#print 'all sequence', allSeq

def generateResult(cipher):
	allSeq = {}
	maxsum = -1296
	maxseq = -1
	for i in range(dcyParam.TOTAL_COLUMNS):
		print 'start index: ',i
		driverobj = langDriver.Driver(CIPHER_TEXT)
		seq, score = driverobj.decipher(i)
		allSeq[i] = {}
		allSeq[i]['seq'] = seq
		allSeq[i]['score'] = score
		seqsum = 0
		for j in range(dcyParam.TOTAL_ROWS):
			#print 'seq log',score[j]
			seqsum+=math.log(score[j])
		allSeq[i]['sum'] = seqsum
		if seqsum>maxsum:
			maxseq = i
			maxsum = seqsum
	return allSeq, maxseq

def deriveSimilarity(allSeq):
	iterRange = []
	simDict = {}
	for i in range(50):
		iterRange.append(i)
	itr = itertools.combinations(iterRange, 2)
	try:
		while True:
			pair = itr.next()
			id1 = pair[0]
			id2 = pair[1]
			
	except StopIteration:
		pass


if __name__=="__main__":
	global CIPHER_TEXT
	CIPHER_TEXT = dcyParam.TEST_SENTENCE
	langCompute.deleteFiles(files = dcyParam.BIGRAM_FILES)
	langCompute.deleteFiles(files = dcyParam.TRIGRAM_FILES)
	allSeq, maxseq = generateResult(CIPHER_TEXT)
	printStat(allSeq, maxseq)
	deriveSimilarity(allSeq)