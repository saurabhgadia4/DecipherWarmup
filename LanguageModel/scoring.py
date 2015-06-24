from langParam import *
minCount = 999999

def bigram(text):
	print 'minCount: ',minCount
	possibility = 1
	for row in text:
		row = '.' + row
		rowPoss = calCond(row)
		print 'row: ',row,'correctness: ',rowPoss
		possibility = float(possibility) * rowPoss
	#print 'Text Score: ',possibility 

def calCond(row):
	possibility =1
	row = list(row)
	for i in range(1, len(row)):
		try:
			prefix = row[i-1]
			current = row[i]
			#print prefix,'-',current
			condCount = computeMat[prefix][current]
			prefixCount = totalCount[prefix]
			possibility = possibility*(float(condCount)/prefixCount)
			#print 'p(%r|%r)'%(current,prefix),'--> condCount: ',condCount, ' prefixCount: ', prefixCount, ' =', possibility 
		except KeyError:
			computeMat[prefix][current] = minCount
			prefixCount = totalCount[prefix]
			possibility = possibility*(float(condCount)/prefixCount)

	return possibility


