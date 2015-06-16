import os
import logging
from dcyInput import *
import dcyParam
class Driver():
    def __init__(self, filepath=dcyParam.CIPHER_FILE_PATH):
        self.inputObjList = []
        self.filepath = filepath
        self.textDict = {}

    def getStrCorpus(self, corpDict):
        inputObj = RowInput(text)
        self.inputObjList.append(inputObj)

    def getCipherTxt(self):
        try:
            fp = open(self.filepath, "r")
            text = fp.readline()
            rowNum = 0
            while(text):
                preint text
                rowNum = rowNum + 1 
                text = fp.readline()
                self.textDict[rowNum] = list(text)
        except Exception as err:
            logging.exception(err)

    def process1(self):
        pass



if __name__=="__main__":
    '''
    1. take the text
    2. create input objects
    3. pass handle to driver.

    '''
    driverObj = Driver()
    driverObj.startProcess1()
    
    

    


