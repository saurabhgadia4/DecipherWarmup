CORPUS_FILE  = "corpus.en"
CORPUS_CLEAN = "corpus_clean.en"
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

BIGRAM_TYPE = 1
TRIGRAM_TYPE = 2
TOTAL_COLUMNS = 50
TOTAL_ROWS = 10

BIGRAM_FILES = [CORPUS_CLEAN, CORPUS_WORDS, CORPUS_CHARS, CORP_SHIFT_1, BIGRAM_PAIR_TEMP, BIGRAM_PAIR, BIGRAM_STAT, UNIGRAM_STAT]
TRIGRAM_FILES = [CORPUS_WORDS, CORPUS_CHARS, CORP_SHIFT_1, CORP_SHIFT_2, TRIGRAM_PAIR_TEMP, TRIGRAM_PAIR, TRIGRAM_STAT, BIGRAM_STAT]

VALID_SENTENCE =[ 
'thepanelisalsoexpectedtorecommendthatthewhitehouse',
'theiraniangovernmenthasmaintainedthatitknowsnothin',
'bymatchingthelowestpriceandenhancingservicehewasde',
'thisfallherneighborhoodinthenortheasternpartofthis',
'forcollegebasketballfansthisisasgoodaweekasyourego',
'butaccordingtobarbershopproprietorsthenumberoffema',
'anintriguingnewstudysuggeststhatwhatreallydrawspeo',
'alsoonthursdaythelatestwinnersofthelifesciencesand',
'whatmembersofbothpartiesbemoanedmorethananythingwa',
'onekeyhurdleforteslainproducingthenewsmallercarwil']


VALID_SENTENCE_P_1 = [
'tommendthatthedtorecepanelisalsoexpectisehouthehwe', 
'ttainedthatithasmaineiraniangovernmenswinoththnonk', 
'penhancingserriceandmatchingthelowesthedewasbyeciv', 
'henortheasteroodinthisfallherneighbortriofththsapn', 
'lsisasgoodawefansthircollegebasketbalysgourefooake', 
'rprietorsthenshopprotaccordingtobarberemoffebuabmu', 
'ysthatwhatreasuggestintriguingnewstudrdeawspanoyll', 
'tersofthelifeestwinnsoonthursdaythelanencesaaldics', 
'roanedmorethatiesbematmembersofbothpatywhingwhanan', 
'acingthenewsminproduekeyhurdleforteslreicarwonllla'
]

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