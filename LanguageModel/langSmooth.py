from string import ascii_lowercase

class Handle():
    def __init__(self, trimat, bimat, unimat, total):
        self.trimat = trimat
        self.bimat = bimat
        self.unimat = unimat
        self.total = total

class Scoring():
    def __init__(self, trimat, bimat, unimat, total):
        self.smoothHndl = LinearInt(trimat, bimat, unimat, total)

    def trigramScore(self, text):
        possibility =1
        row = list(text)
        for i in range(1, len(row)-1):
            try:
                triPrefix = row[i-1] + row[i]
                triCurrent = row[i+1]
                possibility*=self.smoothHndl.triSmooth(triPrefix, triCurrent)
            except Exception as e: 
                print 'Error in trigram score calculation: ', e
        return possibility

    def bigramScore(self, text):
        possibility =1
        row = list(text)
        for i in range(1, len(row)):
            try:
                prefix = row[i-1]
                current = row[i]
                possibility*=self.smoothHndl.biSmooth(prefix, current)
            except Exception as e: 
                print 'Error in bigram score calculation: ', e
        return possibility
        

class LinearInt(Handle):
    def __init__(self, trimat, bimat, unimat, total):
        Handle.__init__(self, trimat, bimat, unimat, total)
        
    def triSmooth(self, prefix, current, l1=0.98, l2=0.0199):
        l3 = 1-l1-l2
        biPfx = prefix[1]
        unipfx = current
        possibility = 1
        try:
            cal1 = l1*(float(self.trimat[prefix][current])/float(self.bimat[prefix[0]][prefix[1]]))
        except KeyError:
            cal1 = 0

        bigram_cal = self.biSmooth(biPfx, current)
        possibility = (cal1+bigram_cal)  
        #print 'Trigram- poss after smoothing pair: ',prefix+current,' -> ', possibility
        return possibility

    def biSmooth(self, prefix, current, l1=0.9999, l2=0.0001):
        try:
            cal1 = l1*(float(self.bimat[prefix][current])/ float(self.unimat[prefix]))
        except KeyError:
            cal1 = 0

        try:
            cal2 = l2*(float(self.unimat[current])/ float(self.total))
        except KeyError:
            cal2 = 0
        #print 'Bigram - poss after smoothing pair: ',prefix+current,' -> ', (cal1+cal2)
        return (cal1+cal2)
