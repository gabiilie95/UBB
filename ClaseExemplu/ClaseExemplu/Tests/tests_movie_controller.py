from Repository.movie_repository import movie_repository
from Domain.movie_validator import movie_validator
from Controller.movie_controller import movie_controller

def test_movie_controller():
    movieRepo = movie_repository()
    movieVal = movie_validator()
    ctrl = movie_controller(movieRepo, movieVal)
    
    ''' Create movie tests '''
    movie1 = ctrl.createmovie("1", "avatar", "james cameron", "fantasy")
    assert movie1.getID() == "1"
    assert movie1.getTitle() == "Avatar"
    allmovies = ctrl.getAllmovies()
    assert len(allmovies) == 1
    assert allmovies[0] == movie1
    try:
        ctrl.createmovie("1", "avatar 2", "james camerooon", "fantasyyy")
        assert False
    except ValueError:
        assert True
        
    ''' Modify movie tests '''
    movie1 = ctrl.modifymovie("1", "avatar 1", "james camerooon", "fantasyyy")
    assert len(ctrl.getAllmovies()) == 1
    #assert ctrl.getAllmovies()[0] == movie
    
    #assert ctrl.getByID("1") == movie1
    try:
        ctrl.getByID("3")
        assert False
    except ValueError:
        assert True
    
    ''' Delete movie test '''
    ctrl.deletemovie("1")
    assert len(ctrl.getAllmovies()) == 0
    
    
test_movie_controller()