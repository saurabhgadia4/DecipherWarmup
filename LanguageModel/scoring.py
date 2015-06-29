from langParam import *
import statistics
minCount = 999999

def bigram(text):
	print 'minCount: ',minCount
	possibility = 1
	rowPoss = []
	for row in text:
		row = '.' + row
		rowPoss.append(calCond(row))
		# print 'row: ',row,'correctness: ',rowPoss
		# possibility = float(possibility) * rowPoss
		# print 'Text Score: ',possibility
	print 'rowPoss',rowPoss
	print 'max', max(rowPoss)
	print 'min', min(rowPoss)
	print 'avg', statistics.mean(rowPoss)

def calCond(row):
	possibility =1
	row = list(row)
	for i in range(1, len(row)):
		try:
			prefix = row[i-1]
			current = row[i]
			#print prefix,'-',current
			condCount = computeBiMat[prefix][current]
			prefixCount = totalBiCount[prefix]
			possibility = possibility*(float(condCount)/prefixCount)
			#print 'p(%r|%r)'%(current,prefix),'--> condCount: ',condCount, ' prefixCount: ', prefixCount, ' =', possibility 
		except KeyError:
			computeBiMat[prefix][current] = minCount
			prefixCount = totalBiCount[prefix]
			possibility = possibility*(float(condCount)/prefixCount)

	return possibility


