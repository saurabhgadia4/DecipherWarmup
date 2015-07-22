import operator

class SeqGraph():
	def __init__(self, sequences):
		self.__root = {}
		self.__seq = sequences
		self.__rev_root = {}

	def createGraph(self):
		for key in self.__seq:
			sequence = self.__seq[key]['seq']
			for i in range(len(sequence)-1):
				self.fwdMapping((sequence[i], sequence[i+1]))
				self.bwdMapping((sequence[i], sequence[i+1]))
				

	def fwdMapping(self, pair):
		if not self.__root.get(pair[0], None):
			self.__root[pair[0]] = {}
		if not self.__root[pair[0]].get(pair[1], None):
			self.__root[pair[0]][pair[1]] = 1
		else:
			self.__root[pair[0]][pair[1]] += 1

	def bwdMapping(self, pair):
		if not self.__rev_root.get(pair[1], None):
			self.__rev_root[pair[1]] = {}
		if not self.__rev_root[pair[1]].get(pair[0], None):
			self.__rev_root[pair[1]][pair[0]] = 1
		else:
			self.__rev_root[pair[1]][pair[0]] += 1

	def printGraph(self):

		for key in self.__root:
			sortedDict = sorted(self.__root[key].items(), key=operator.itemgetter(1), reverse=True)
			print key,':',sortedDict

		for key in self.__rev_root:
			sortedRevDict = sorted(self.__rev_root[key].items(), key=operator.itemgetter(1), reverse=True)
			print key,':',sortedRevDict

	def generateSeq(self):
		for key in self.__root:
			sortedDict = sorted(self.__root[key].items(), key=operator.itemgetter(1), reverse=True)
			self.__root[key] = sortedDict

		for key in self.__rev_root:
			sortedRevDict = sorted(self.__rev_root[key].items(), key=operator.itemgetter(1), reverse=True)
			self.__rev_root[key] = sortedRevDict

		visited = {}
		for i in range(50):
			visited[i] = 0

		for key in visited:
			search = key                         #search=49
			if visited[key]:
				continue
			while True:
				rev_key = self.__root[search][0][0]  #rev_key=0
				match_key = self.__rev_root[rev_key][0][0] #match_key = 49
				if match_key == search and not visited[search]:
					visited[search] = 1
					print search,'->',rev_key
					search = rev_key
				else:
					break

		print 'Not visited nodes'
		not_visited = ''
		for key in visited:
			if not visited[key]:
				not_visited+='%s,'% key
		print not_visited




