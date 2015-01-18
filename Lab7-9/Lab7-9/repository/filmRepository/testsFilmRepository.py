from domain.film.film import Film
from repository.filmRepository.filmRepository import FilmRepository

def test_FilmRepository():
    film = Film(1, "avatar", "james cameron", "fantasy")
    film2 = Film(2, "inception", "asgasg", "adventure")
    filmRepo = FilmRepository()
    
    ''' Store tests '''
    filmRepo.store(film)
    assert filmRepo.getSize() == 1
    filmRepo.store(film2)
    assert filmRepo.getSize() == 2
    assert filmRepo.findByID(film2.getID()) == True
    assert filmRepo.findByID(3) == False
    film3 = Film(2, "goodfellas", "martin scorsese", "crime")
    try:
        filmRepo.store(film3)
        assert False
    except ValueError:
        assert True
    assert filmRepo.getSize() == 2
    
    ''' Modify tests '''
    filmRepo.modify(film3)
    assert filmRepo.getSize() == 2
    assert filmRepo.getAll()[1].getTitle() == "goodfellas"
    assert filmRepo.getAll()[1].getDirector() == "martin scorsese"
    assert filmRepo.getAll()[1].getGenre() == "crime"
    
    ''' Delete tests '''
    filmRepo.delete(1)
    assert filmRepo.getSize() == 1
    assert filmRepo.getAll()[0].getID() == 2
    
test_FilmRepository()