
class rent_repository():
    
    def __init__(self):
        self.__rents = []

    
    def storerent(self, rent):
        '''
        Store a rent in the rents list
        If the rent is already stored in the list and is active, raise ValueError
        '''
        if self.findByID(rent.getIDF()) == False:
            self.__rents.append(rent)
        else:
            raise ValueError("The movie is already rented")

    
    def getSize(self):
        return len(self.__rents)

    
    def getAll(self):
        return self.__rents
    
    
    def findByID(self, idf):
        '''
        Find a rent by the id of the rented movie
        idf - the movie id
        Return True if rent is found and active, otherwise return False
        '''
        for rent in self.__rents:
            if rent.getIDF() == idf and rent.getIsrented() == True:
                return True
        return False

    
    def returnmovie(self, idf):
        '''
        Return a movie
        idf - the movie id
        returns the updated list of rents
        '''
        if self.findByID(idf) == False:
            raise ValueError("Can't return the movie because it isn't rented")
        else:
            for rent in self.__rents:
                if rent.getIDF() == idf and rent.getIsrented() == True:
                    rent.setIsNotrented()
                    
        return self.__rents
    
    
    