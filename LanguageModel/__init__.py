import langModels
import langDriver
import dcyParam
import langCompute

if __name__=="__main__":
	driverobj = langDriver.Driver(dcyParam.TEST_SENTENCE)
	seq, text = driverobj.decipher(17)
	print 'permuted sequence: ', seq
	for row in text:
		print row
	langCompute.deleteFiles(files = dcyParam.BIGRAM_FILES)
	langCompute.deleteFiles(files = dcyParam.TRIGRAM_FILES)
    

