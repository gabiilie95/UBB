from Domain.rent import rent

class rent_controller():
    
    def __init__(self, repo, valid, movieRepo, clientRepo):
        self.__repo = repo
        self.__valid = valid
        self.__movieRepo = movieRepo
        self.__clientRepo = clientRepo

    
    def createrent(self, idc, idf):
        if self.__clientRepo.findByID(idc) == True and self.__movieRepo.findByID(idf) == True:
            rent = rent(idc, idf)
            self.__valid.validate(rent)
            self.__repo.storerent(rent)
            return rent
        else:
            raise ValueError("The id of the client or movie does not exist")

    
    def getAllrents(self):
        return self.__repo.getAll()

    
    def returnmovie(self, idf):
        try:
            self.__repo.returnmovie(idf)
        except ValueError as msg:
            print (msg)
    
    
    
    
    
    
        
    
    
        
    
    