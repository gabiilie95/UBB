
class Client():
    
    def __init__(self, idc, name, cnp):
        self.__idc = idc
        self.__name = name
        self.__cnp = cnp


    def getID(self):
        return self.__idc
    
    
    def getName(self):
        return self.__name
    
    
    def getCNP(self):
        return self.__cnp
    
    
    def setName(self, name):
        self.__name = name
        

    def setCNP(self, cnp):
        self.__cnp = cnp
        
    
    def __eq__(self, client):
        return self.__idc == client.getID()
    
    
