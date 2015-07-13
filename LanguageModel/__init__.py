import math
import langModels
import langDriver
import dcyParam
import langCompute

if __name__=="__main__":
	allSeq = {}
	maxsum = -1296
	maxseq = -1
	for i in range(dcyParam.TOTAL_COLUMNS):
		print 'start index: ',i
		driverobj = langDriver.Driver(dcyParam.NEW_TEST)
		seq, text, score = driverobj.decipher(i)
		allSeq[i] = {}
		allSeq[i]['seq'] = seq
		allSeq[i]['text'] = text
		allSeq[i]['score'] = score
		seqsum = 0
		for j in range(dcyParam.TOTAL_ROWS):
			#print 'seq log',score[j]
			seqsum+=math.log(score[j])
		allSeq[i]['sum'] = seqsum
		if seqsum>maxsum:
			maxseq = i
			maxsum = seqsum

	print 'Maximum score sequence starting index', maxseq
	print 'Sequence', allSeq[maxseq]['seq']
	print 'Text', allSeq[maxseq]['text']
	print 'sum', allSeq[maxseq]['sum']
	print 'all sequence', allSeq

	langCompute.deleteFiles(files = dcyParam.BIGRAM_FILES)
	langCompute.deleteFiles(files = dcyParam.TRIGRAM_FILES)
    

