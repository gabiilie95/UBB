from domain.rent.rent import Rent

class RentController():
    
    def __init__(self, repo, valid, filmRepo, clientRepo):
        self.__repo = repo
        self.__valid = valid
        self.__filmRepo = filmRepo
        self.__clientRepo = clientRepo

    
    def createRent(self, idc, idf):
        if self.__clientRepo.findByID(idc) == True and self.__filmRepo.findByID(idf) == True:
            rent = Rent(idc, idf)
            self.__valid.validate(rent)
            self.__repo.storeRent(rent)
            return rent
        else:
            raise ValueError("The id of the client or film does not exist")

    
    def getAllRents(self):
        return self.__repo.getAll()

    
    def returnFilm(self, idf):
        try:
            self.__repo.returnFilm(idf)
        except ValueError as msg:
            print (msg)
    
    
    
    
    
    
        
    
    
        
    
    