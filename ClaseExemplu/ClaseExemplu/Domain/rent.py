
class rent():
    '''
    Store a rent
    A rent consists of a client id and a movie id
    The movie with the ID is rented to the client with the ID
    '''
    def __init__(self, idc, idf):
        self.__idc = idc
        self.__idf = idf
        self.__isrented = True

    
    def getIDC(self):
        '''
        Return the client ID
        '''
        return self.__idc

    
    def getIDF(self):
        '''
        Return the movie ID
        '''
        return self.__idf
    
    
    def getIsrented(self):
        return self.__isrented

    
    def setIDC(self, idc):
        '''
        Set the client ID
        '''
        self.__idc = idc

    
    def setIDF(self, idf):
        '''
        Set the movie ID
        '''
        self.__idf = idf
    
    
    def setIsrented(self):
        self.__isrented = True
      
        
    def setIsNotrented(self):
        self.__isrented = False
        
    
    
    
    
    
    
        
    