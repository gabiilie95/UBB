
from domain.film.film import Film
from domain.film.filmValidator import FilmValidator
from domain.client.client import Client

def test_film():
    film = Film(1, "avatar", "james cameron", "fantasy")
    assert film.getID() == 1
    assert film.getTitle() == "avatar"
    assert film.getDirector() == "james cameron"
    assert film.getGenre() == "fantasy"
test_film()



def test_FilmValidator():
    valid = FilmValidator()
    
    film1 = Film(1, "interstellar", "christopher nolan", "intergalactic")
    try:
        valid.validate(film1)
        assert True
    except ValueError:
        assert False
        
    film2 = Film("ads", "", "christopher nolan", "adventure")
    try:
        valid.validate(film2)
        assert False
    except ValueError:
        assert True
        
test_FilmValidator()
        
