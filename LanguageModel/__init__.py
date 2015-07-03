import langModels
import langDriver
import dcyParam

if __name__=="__main__":
	driverobj = langDriver.Driver(dcyParam.TEST_SENTENCE)
	seq, text = driverobj.decipher(0)
	print 'permuted sequence: ', seq
	print 'decipher text: ', text
    

