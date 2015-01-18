class rent_repository():
    
    def __init__(self):
        self.__rents = []

    
    def storeRent(self, rent):
        '''
        Store a rent in the rents list
        If the rent is already stored in the list and is active, raise ValueError
        '''
        if self.findByID(rent.getIDM()) == False:
            self.__rents.append(rent)
        else:
            raise ValueError("The movie is already rented")

    
    def getSize(self):
        return len(self.__rents)

    
    def getAll(self):
        return self.__rents
    
    
    def findByID(self, idm):
        '''
        Find a rent by the id of the rented movie
        idm - the movie id
        Return True if rent is found and active, otherwise return False
        '''
        for rent in self.__rents:
            if rent.getIDM() == idm and rent.getIsRented() == True:
                return True
        return False

    
    def returnMovie(self, idm):
        '''
        Return a movie
        idm - the movie id
        returns the updated list of rents
        '''
        if self.findByID(idm) == False:
            raise ValueError("Can't return the movie because it isn't rented")
        else:
            for rent in self.__rents:
                if rent.getIDM() == idm and rent.getIsRented() == True:
                    rent.setIsNotRented()
                    
        return self.__rents
    
    def returnBestClients(self):
        
        '''Returns a list with clients that rented most movies.'''
        
        rents = self.getAll()
        bestClients = []
        
        for i in range(0, self.getSize()):
            
            #tobecontinued

            PASS
    