from repository.filmRepository.filmRepository import FilmRepository
from domain.film.filmValidator import FilmValidator
from filmController import FilmController

def test_filmController():
    filmRepo = FilmRepository()
    filmVal = FilmValidator()
    ctrl = FilmController(filmRepo, filmVal)
    
    ''' Create film tests '''
    film1 = ctrl.createFilm("1", "avatar", "james cameron", "fantasy")
    assert film1.getID() == "1"
    assert film1.getTitle() == "avatar"
    allFilms = ctrl.getAllFilms()
    assert len(allFilms) == 1
    assert allFilms[0] == film1
    try:
        ctrl.createFilm("1", "avatar 2", "james camerooon", "fantasyyy")
        assert False
    except ValueError:
        assert True
        
    ''' Modify film tests '''
    film = ctrl.modifyFilm("1", "avatar 1", "james camerooon", "fantasyyy")
    assert len(ctrl.getAllFilms()) == 1
    assert ctrl.getAllFilms()[0] == film
    
    ''' Delete film test '''
    ctrl.deleteFilm("1")
    assert len(ctrl.getAllFilms()) == 0
    
test_filmController()