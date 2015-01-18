from Repository.client_repository import client_repository
from Repository.movie_repository import movie_repository
from Repository.rent_repository import rent_repository
from Validators.client_validator import client_validator
from Validators.movie_validator import movie_validator
from Validators.rent_validator import rent_validator
from Controller.client_controller import client_controller
from Controller.movie_controller import movie_controller
from Controller.rent_controller import rent_controller

def test_client_controller():
    repo = client_repository()
    valid = client_validator()
    ctrl = client_controller(repo, valid)
    
    ''' Create client tests '''
    client1 = ctrl.createClient("1", "stefan", "1111")
    assert client1.getID() == "1"
    assert client1.getName() == "Stefan"
    assert client1.getCNP() == "1111"
    allClients = ctrl.getAllClients()
    assert len(allClients) == 1
    assert allClients[0] == client1
    try:
        ctrl.createClient("1", "stefan2", "2222")
        assert False
    except ValueError:
        assert True
    
    ''' Modify client test '''
    client2 = ctrl.modifyClient("1", "stefan2", "222222")
    assert len(ctrl.getAllClients()) == 1
    #assert ctrl.getAllClients()[0] == client2
    assert ctrl.getAllClients()[0].getCNP() == "222222"
    
    ''' Delete client test '''
    ctrl.deleteClient("1")
    assert len(ctrl.getAllClients()) == 0



def test_movie_controller():
    movieRepo = movie_repository()
    movieVal = movie_validator()
    ctrl = movie_controller(movieRepo, movieVal)
    
    ''' Create movie tests '''
    movie1 = ctrl.createMovie("1", "avatar", "james cameron", "fantasy")
    assert movie1.getID() == "1"
    assert movie1.getTitle() == "Avatar"
    allMovies = ctrl.getAllMovies()
    assert len(allMovies) == 1
    assert allMovies[0] == movie1
    try:
        ctrl.createMovie("1", "avatar 2", "james camerooon", "fantasyyy")
        assert False
    except ValueError:
        assert True
        
    ''' Modify movie tests '''
    movie = ctrl.modifyMovie("1", "avatar 1", "james camerooon", "fantasyyy")
    assert len(ctrl.getAllMovies()) == 1
    #assert ctrl.getAllMovies()[0] == movie
    
    ''' Delete movie test '''
    ctrl.deleteMovie("1")
    assert len(ctrl.getAllMovies()) == 0

def test_rent_controller():

    movieRepo = movie_repository()
    movieValid = movie_validator()
    movieController = movie_controller(movieRepo, movieValid)
    
    clientRepo = client_repository()
    clientValid = client_validator()
    clientController = client_controller(clientRepo, clientValid)
    
    movieController.createMovie("1", "blabla", "blaaa", "fantasy")
    movieController.createMovie("2", "blabla2", "blaaa2", "fantasy")
    movieController.createMovie("3", "blabla3", "blaaa3", "adventure")
    
    clientController.createClient("1", "stefan", "1234")
    clientController.createClient("2", "stefan2", "12345")
    clientController.createClient("3", "stefan3", "123456")
    
    
    
    
    repo = rent_repository()
    valid = rent_validator()
    ctrl = rent_controller(repo, valid, movieRepo, clientRepo)
    
    rent1 = ctrl.createRent("1", "2")
    assert len(ctrl.getAllRents()) == 1
    assert rent1.getIDC() == "1"
    assert rent1.getIDM() == "2"
    
    try:
        ctrl.createRent("3", "2")
        assert False
    except ValueError:
        assert True
        
    ctrl.returnMovie("2")
    assert ctrl.getAllRents()[0].getIsRented() == False
    
    try:
        ctrl.createRent("3", "2")
        assert True
    except ValueError:
        assert False
        
    
