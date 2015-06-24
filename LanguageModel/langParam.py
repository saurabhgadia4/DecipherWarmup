CORPUS_FILE = "corpus.en"
CORPUS_WORDS = "corpWords.txt"
CORPUS_CHARS = "corpChar.txt"
CORP_SHIFT = "corpShift.txt"
CORP_JOIN = "corpJoin.txt"
CORP_STAT = "corpStat.txt"
CHAR_COUNT = "charCnt.txt"

CORP_SUP_FILES = [CORPUS_WORDS, CORPUS_CHARS, CORP_SHIFT, CORP_JOIN, CORP_STAT, CHAR_COUNT]
computeMat = {}
totalCount = {}

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