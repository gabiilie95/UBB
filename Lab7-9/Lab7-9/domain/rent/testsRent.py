from domain.rent.rent import Rent
from domain.rent.rentValidator import RentValidator


def test_rent():
    rent = Rent("1", "2")
    assert rent.getIDC() == "1"
    assert rent.getIDF() == "2"
    assert rent.getIsRented() == True
    rent.setIsNotRented()
    rent.setIDC("2")
    rent.setIDF("1")
    assert rent.getIDC() == "2"
    assert rent.getIDF() == "1"
    assert rent.getIsRented() == False
    
test_rent()
    

def test_validator():
    rent = Rent("1", "")
    valid = RentValidator()
    try:
        valid.validate(rent)
        assert False
    except ValueError:
        assert True
        
    rent = Rent("1", "1")
    try:
        valid.validate(rent)
        assert True
    except ValueError:
        assert False
        
test_validator()