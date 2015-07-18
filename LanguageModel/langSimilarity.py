
import dcyParam

def getSubstrMatrix(seq1, seq2, simDict = {}):
    len1 = len(seq1)
    len2 = len(seq2)
    submat = [[0 for i in range(len1+2)] for j in range(len2+2)]
    submat[0][0] = '*'
    for i in range(1,len2+1):
        submat[0][i] = seq2[i-1]
    for j in range(1, len1+1):
        submat[j][0] = seq1[j-1]
    for i in range(1,len1+1):
        for j in range(1,len2+1):
            if(seq1[i-1]==seq2[j-1]):
                submat[i+1][j+1] = submat[i][j]+1

    # for row in submat:
    #     print row
    travSubstr(simDict, submat, 2, 1, len1+1)
    return simDict

def travSubstr(simDict, submat, row, col, rowlen, prefix='', add=1):
    if not row>rowlen:
        if col<= rowlen:
            if submat[row][col]!=0:
                #print submat[row-1][0]
                prefix+='%r-' % (submat[row-1][0])
                travSubstr(simDict, submat, row+1, col+1, rowlen, prefix, 0)
            else:
                try:
                    simDict[prefix]+=1
                except KeyError:
                    simDict[prefix] = 1
                #print 'row',row
                #print 'submat',submat[row][0]
                new_col = submat[row].index(1)
                if new_col==0:
                    new_col = submat[row].index(1, 1)
                travSubstr(simDict, submat, row, new_col, rowlen)
        else:
            try:
                simDict[prefix]+=1
            except KeyError:
                simDict[prefix] = 1
            #print 'hit'
            if add==0:
                travSubstr(simDict, submat, row, 1, rowlen)
            else:
                travSubstr(simDict, submat, row+1, 1, rowlen)



if __name__=="__main__":
    
    seq1 = [0, 41, 25, 47, 43, 23, 28, 15, 33, 40, 48, 34, 5, 8, 27, 42, 6, 37, 44, 9, 49, 13, 21, 31, 32, 24, 35, 22, 26, 38, 18, 2, 10, 4, 17, 19, 16, 29, 45, 39, 20, 36, 3, 11, 46, 12, 1, 7, 30, 14]
    seq2 = [26, 49, 0, 35, 22, 23, 41, 25, 47, 43, 13, 37, 33, 40, 48, 34, 5, 8, 27, 42, 6, 10, 4, 17, 24, 15, 44, 9, 28, 20, 39, 31, 32, 18, 38, 16, 19, 36, 3, 11, 45, 21, 29, 14, 12, 46, 1, 7, 30, 2]

    simDict = getSubstrMatrix(seq1, seq2)
    print simDict
