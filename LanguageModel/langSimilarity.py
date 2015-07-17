
import dcyParam

def getSubstrMatrix(seq1, seq2):
    len1 = len(seq1)
    len2 = len(seq2)
    simDict = {}
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

    for row in submat:
        print row
    travSubstr(simDict, submat, 2, 2, len1+1)
    return simDict

def travSubstr(simDict, submat, row, col, rowlen, prefix=''):
    if not row>rowlen:
        if submat[row][col]!=0:
            print submat[row-1][0]
            prefix+='%r-' % (submat[row-1][0])
            travSubstr(simDict, submat, row+1, col+1, rowlen, prefix)
        else:
            try:
                simDict[prefix]+=1
            except KeyError:
                simDict[prefix] = 1
            new_col = submat[row].index(1)
            print 'break'
            travSubstr(simDict, submat, row, new_col, rowlen)


if __name__=="__main__":
    seq1 =[ 31, 32, 24, 34, 25, 47, 43, 23, 28, 15, 33, 40, 48, 16, 18, 2, 37, 45, 5, 8, 27, 42, 6, 10, 35, 
     22, 26, 49, 0, 41, 11, 46, 19, 36, 3, 13, 21, 9, 38, 44, 4, 17, 20, 29, 14, 12, 39, 1, 7, 30]

    seq2 = [1, 12, 39, 37, 33, 40, 48, 34, 25, 47, 43, 23, 28, 15, 21, 9, 49, 0, 35, 22, 26, 38, 13, 41, 11, 
    45, 5, 8, 27, 42, 6, 10, 4, 17, 24, 20, 29, 31, 32, 18, 2, 46, 19, 36, 3, 44, 7, 16, 14, 30]
    simDict = getSubstrMatrix(seq1, seq2)
    print simDict
