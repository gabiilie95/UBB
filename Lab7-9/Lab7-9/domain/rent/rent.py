
class Rent():
    '''
    Store a rent
    A rent consists of a client id and a film id
    The film with the ID is rented to the client with the ID
    '''
    def __init__(self, idc, idf):
        self.__idc = idc
        self.__idf = idf
        self.__isRented = True

    
    def getIDC(self):
        '''
        Return the client ID
        '''
        return self.__idc

    
    def getIDF(self):
        '''
        Return the film ID
        '''
        return self.__idf
    
    
    def getIsRented(self):
        return self.__isRented

    
    def setIDC(self, idc):
        '''
        Set the client ID
        '''
        self.__idc = idc

    
    def setIDF(self, idf):
        '''
        Set the film ID
        '''
        self.__idf = idf
    
    
    def setIsRented(self):
        self.__isRented = True
      
        
    def setIsNotRented(self):
        self.__isRented = False
        
    
    
    
    
    
    
        
    