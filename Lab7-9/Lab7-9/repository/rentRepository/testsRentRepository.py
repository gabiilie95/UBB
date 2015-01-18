from domain.rent.rent import Rent
from repository.rentRepository.rentRepository import RentRepository

def tests_rentRepository():
    rentRepo = RentRepository()
    rent1 = Rent("1", "2")
    rent2 = Rent("3", "2")
    rent3 = Rent("1", "3")
    
    ''' Store tests '''
    rentRepo.storeRent(rent1)
    assert rentRepo.getSize() == 1
    assert rentRepo.getAll()[0].getIDC() == "1"
    assert rentRepo.getAll()[0].getIDF() == "2"
    try:
        rentRepo.storeRent(rent2)
        assert False
    except ValueError:
        assert True
    rentRepo.storeRent(rent3)
    assert rentRepo.getSize() == 2
    assert rentRepo.getAll()[1].getIDC() == "1"
    assert rentRepo.getAll()[1].getIDF() == "3"
    
    ''' Return tests '''
    assert rentRepo.getAll()[1].getIsRented() == True
    rentRepo.returnFilm("3")
    assert rentRepo.getSize() == 2
    assert rentRepo.getAll()[1].getIsRented() == False
    try:
        rentRepo.returnFilm("4")
        assert False
    except ValueError:
        assert True
        
    ''' Store after return '''
    rent4 = Rent("10", "3")
    rentRepo.storeRent(rent4)
    assert rentRepo.getSize() == 3
    assert rentRepo.getAll()[2].getIDC() == "10"
    assert rentRepo.getAll()[2].getIDF() == "3"
    assert rentRepo.getAll()[2].getIsRented() == True
    

tests_rentRepository()