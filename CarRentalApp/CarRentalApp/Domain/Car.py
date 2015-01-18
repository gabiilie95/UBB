class car():
    """Adds a car"""
    def __init__(self, nr, model_name, type, price_per_day):
        self.__nr = nr
        self.__model_name = model_name
        self.__type = type
        self.__price_per_day = price_per_day
        self.__isRented = True

    
    def getNr(self):
        '''
       
        '''
        return self.__nr

    
    def getModel_name(self):
        '''
        
        '''
        return self.__model_name

    def getType(self):
        '''
       
        '''
        return self.__type

    def getPrice_per_day(self):
        '''
       
        '''
        return self.__price_per_day
    
    
    def getIsRented(self):
        return self.__isRented

    
    def setNr(self, nr):
        '''
        '''
        self.__nr = nr

        
    def setType(self, type):
        '''
        '''
        self.__type = type

    
    def setModel_name(self, model_name):
        '''
        
        '''
        self.__model_name = model_name

    def setPrice_per_day(self, price_per_day):
        '''
        '''
        self.__price_per_day = price_per_day
    
    
    def setIsRented(self):
        self.__isRented = True
      
        
    def setIsNotRented(self):
        self.__isRented = False