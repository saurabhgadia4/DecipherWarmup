import math
import itertools
import langModels
import langDriver
import dcyParam
import langCompute
import langSimilarity
import operator

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
# 	new_seq = [33, 40, 48, 5, 8, 27, 42, 6, 10, 35, 22, 26, 49, 46, 19, 36, 21, 9, 38, 25, 47, 43, 18, 2, 44, 4, 17, 1, 7, 30,
# 34, 37, 0, 14, 12, 39, 31, 32, 29, 45, 3,  24, 13, 41, 11, 16,  28, 20, 15, 23]
# 	new_text = langCompute.formText(CIPHER_TEXT, new_seq)
# 	print 'new_seq', new_seq
# 	print 'new_text', new_text
# 	new_biscore, new_triscore = driverobj.calScore(new_text)
# 	origsum = 0
# 	for j in range(dcyParam.TOTAL_ROWS):
# 			#print 'seq log',score[j]
# 			origsum+=math.log(new_triscore[j])
# 	print 'new_sum', origsum
	return allSeq, maxseq

def deriveSimilarity(allSeq):
	iterRange = []
	simDict = {}
	revDict = {}
	for i in range(50):
		iterRange.append(i)
	itr = itertools.combinations(iterRange, 2)
	print 'allSeq',allSeq
	try:
		i = 1
		while True:
			pair = itr.next()
			id1 = pair[0]
			id2 = pair[1]
			langSimilarity.getSubstrMatrix(allSeq[id1]['seq'], allSeq[id2]['seq'], simDict)
			i+=1
	except StopIteration:
		pass

	print 'simDict',simDict
	sortedRevDict = sorted(simDict.items(), key=operator.itemgetter(1), reverse=True)
	print 'sortedRevDict',sortedRevDict
	# for k in simDict:
	# 	try:
	# 		if not revDict.get(simDict[k], None):
	# 			revDict[simDict[k]] = []
	# 		revDict[simDict[k]].append(k)
	# 	except KeyError:
	# 		revDict[simDict[k]] = []
	# 		revDict[simDict[k]].append(k)
	# print 'revDict = ',revDict


if __name__=="__main__":
	global CIPHER_TEXT
	CIPHER_TEXT = dcyParam.NEW_TEST
	langCompute.deleteFiles(files = dcyParam.BIGRAM_FILES)
	langCompute.deleteFiles(files = dcyParam.TRIGRAM_FILES)
	allSeq, maxseq = generateResult(CIPHER_TEXT)
	printStat(allSeq, maxseq)
	deriveSimilarity(allSeq)