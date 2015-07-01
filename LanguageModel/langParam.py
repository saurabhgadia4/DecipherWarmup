CORPUS_ORIG  = "corpusOrig.en" 
CORPUS_FILE  = "corpus.en"
# CORPUS_MINUS_SPACE = "corpus_minus_space.en"
# CORPUS_TEMP_WORDS = "StempW.txt"
# CORPUS_TEMP_WORDS_1 = "StempW1.txt"
CORPUS_WORDS = "StoW.txt"
CORPUS_CHARS = "WtoC.txt"
CORP_SHIFT_1 = "CorpShift.txt"
CORP_SHIFT_2 = "CorpShift_2.txt"

UNIGRAM_STAT = "UnigramStat.txt"

BIGRAM_PAIR  = "BigramPair.txt"
BIGRAM_PAIR_TEMP = "BPairTemp.txt"
BIGRAM_STAT  = "BigramStat.txt"

TRIGRAM_PAIR = "TrigramPair.txt"
TRIGRAM_PAIR_TEMP = "TriPairTemp.txt"
TRIGRAM_STAT = "TrigramStat.txt" 


BIGRAM_FILES = [CORPUS_WORDS, CORPUS_CHARS, CORP_SHIFT_1, BIGRAM_PAIR_TEMP,BIGRAM_PAIR, BIGRAM_STAT, UNIGRAM_STAT]
TRIGRAM_FILES = [CORPUS_WORDS, CORPUS_CHARS, CORP_SHIFT_1, CORP_SHIFT_2, TRIGRAM_PAIR_TEMP, TRIGRAM_PAIR, TRIGRAM_STAT, BIGRAM_STAT]

VALID_SENTENCE =[ 
'the~panel~is~also~expected~to~recommend~that~the~whitehouse',
'the~iranian~government~has~maintained~that~it~knows~nothin',
'by~matching~the~lowest~price~and~enhancing~service~he~was~de',
'this~fall~her~neighborhood~in~the~northeastern~part~of~this',
'for~college~basketball~fans~this~is~as~good~a~week~as~your~ego',
'but~according~to~barber~shop~proprietors~the~number~of~fema',
'anintriguing~new~study~suggests~thatwhat~really~draws~peo',
'also~on~thursday~the~latest~winners~of~the~life~sciences~and',
'what~members~of~both~parties~be~moaned~more~than~anything~wa',
'one~key~hurdle~for~tesla~in~producing~the~new~smaller~car~wil']

TEST_SENTENCE = [
'heeemirhcletshlohttwhsnpuesecetottipoenadeamtoaexd',
'tnreaaahninsnootottnhiaihkvnnhimttwmtieadnrisegena',
'raomnnaytihhgchawbsindcasveedreeipeeenngcethcltswi',
'rrginhnhrllteantfttpaiashneshoeiehrbettshofodiroho',
'eaerigtolelyeaarufakoglceesoifwsolsbshsdgoosnkbata',
'nebtrdpueroribgffbhmsmcaeutaoseprrerprttoocioonbah',
'aawituendgiriygswarlaernplnotseghydtssttwathgenusu',
'eotsruilahtnridseaicennoasadnefwhteeenfltcostyslhs',
'aeoaaebhabmtrnoniwtarwetgnfamthsoryhoedemhmnebspti',
'mgreironluhrdleraowlniykwafluisreaeecdtehcenpolstn']

NEW_TEST = [
'dtjmeoftumhbhstehresweseeoatearthkteoouietohfyetri',
'ehsinaeinctnecfdbouunuetomltoimtonsrsihyeognrcfesi',
'heldoehwaenwkleomnaegnonwefrimimynhenopngotiwymltt',
'ikthgatysiowiitdeedrofeeyexonroaneitthtntsnhleofhc',
'oslmnemjrtoebeftegernesioiweayksphluethuaraeahafth',
'nfiehtuohugiandettheeoartttrbeybuiohvsatsdousnwona',
'sltaeytgnnhaatgoehtkssulttroleulenaofiolgtwanlleli',
'wmlptepmsttoehwchhieiavoehikrnwthaterecnltewacwele',
'icnoovslantrebdweoifseundstntewanhioottaeatairetds',
'cggoarrhsdewarhtipntiiretnowrddcahipwtgneoeboeldwa',]