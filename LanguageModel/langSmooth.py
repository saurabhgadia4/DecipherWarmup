from string import ascii_lowercase

class LinearInt():
    def __init__(self, trimat, bimat, unimat, total):
        self.trimat = trimat
        self.bimat = bimat
        self.unimat = unimat
        self.total = total

    def triSmooth(self, prefix, current, l1=0.8, l2=0.197):
        l3 = 1-l1-l2
        biPfx = prefix[1]
        unipfx = current
        possibility = 1
        try:
            cal1 = l1*(float(self.trimat[prefix][current])/float(self.bimat[prefix[0]][prefix[1]]))
        except KeyError:
            cal1 = 0

        bigram_cal = self.biSmooth(biPfx, current, l1=0.197, l2=l3)

        # try:
        #     cal2 = l2*(((float)self.bimat[biPfx][current])/(float)self.unimat[biPfx])
        # except KeyError:
        #     cal2 = 0

        # try:
        #     cal3 = l3*((float)self.unimat[current]/(float)self.total)
        # except KeyError:
        #     cal3 = 0
        possibility = (cal1+bigram_cal)  
        print 'poss after smooth', possibility
        return possibility

    def biSmooth(self, prefix, current, l1=0.997, l2=0.003):
        try:
            cal1 = l1*(float(self.bimat[prefix][current])/ float(self.unimat[prefix]))
        except KeyError:
            cal1 = 0

        try:
            cal2 = l2*(float(self.unimat[current])/ float(self.total))
        except KeyError:
            cal2 = 0

        return (cal1+cal2)
