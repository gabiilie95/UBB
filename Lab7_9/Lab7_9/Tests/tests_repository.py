from Repository.client_repository import client_repository
from Repository.movie_repository import movie_repository
from Repository.rent_repository import rent_repository
from Domain.client import client
from Domain.movie import movie
from Domain.rent import rent

def test_client_repository():

    repo = client_repository()

    client1 = client('1', 'Gabi Ilie', '1234567890')
    client2 = client('2', 'Dan Ioan', '0987654321')

    '''Add tests'''

    repo.addClient(client1)
    assert repo.getSize() == 1
    repo.addClient(client2)
    assert repo.getSize() == 2

    assert repo.findByID(client2.getID()) == True
    assert repo.findByID('3') == False

    client3 = client('3', 'razvan pop', '1234509876')

    repo.addClient(client3)
    assert repo.getSize() == 3

    try:
        repo.addClient(client3)
        assert False
    except ValueError:
        assert True

    '''Modify tests'''
    
    clientModif = client('2', 'Ionut morar', '0987612345')
    repo.modifyClient(clientModif)
    assert repo.getAll()[1].getName() == 'Ionut Morar'
    assert repo.getAll()[1].getCNP() == '0987612345'

    assert repo.findByID(client3.getID()) == True
    repo.deleteClient('3')
    assert repo.getSize() == 2

def test_movie_repository():

    movieRepo = movie_repository()

    movie1 = movie('1', 'avatar', 'James cameron', 'sci-fi')
    movie2 = movie('2', 'goodfellas', 'martin Scorsese', 'Drama')

    '''Add tests'''

    movieRepo.addMovie(movie1)
    assert movieRepo.getSize() == 1
    movieRepo.addMovie(movie2)
    assert movieRepo.getSize() == 2

    assert movieRepo.findByID(movie2.getID()) == True
    assert movieRepo.findByID(3) == False

    movie3 = movie('3', 'casino', 'Martin Scorsese', 'drama')

    movieRepo.addMovie(movie3)
    assert movieRepo.getSize() == 3

    try:
        movieRepo.addMovie(movie3)
        assert False
    except ValueError:
        assert True

    '''Modify tests'''
    
    movieModif = movie('2', 'the departed', 'martin scorsese', 'crime')
    movieRepo.modifyMovie(movieModif)
    assert movieRepo.getAll()[1].getTitle() == 'The Departed'
    assert movieRepo.getAll()[1].getDirector() == 'Martin Scorsese'

    assert movieRepo.findByID(movie3.getID()) == True
    movieRepo.deleteMovie('3')
    assert movieRepo.getSize() == 2


def test_rent_repository():
    rentRepo = rent_repository()
    rent1 = rent("1", "2")
    rent2 = rent("3", "2")
    rent3 = rent("1", "3")
    
    ''' Store tests '''
    rentRepo.storeRent(rent1)
    assert rentRepo.getSize() == 1
    assert rentRepo.getAll()[0].getIDC() == "1"
    assert rentRepo.getAll()[0].getIDM() == "2"
    try:
        rentRepo.storeRent(rent2)
        assert False
    except ValueError:
        assert True
    rentRepo.storeRent(rent3)
    assert rentRepo.getSize() == 2
    assert rentRepo.getAll()[1].getIDC() == "1"
    assert rentRepo.getAll()[1].getIDM() == "3"
    
    ''' Return tests '''
    assert rentRepo.getAll()[1].getIsRented() == True
    rentRepo.returnMovie("3")
    assert rentRepo.getSize() == 2
    assert rentRepo.getAll()[1].getIsRented() == False
    try:
        rentRepo.returnMovie("4")
        assert False
    except ValueError:
        assert True
        
    ''' Store after return '''
    rent4 = rent("10", "3")
    rentRepo.storeRent(rent4)
    assert rentRepo.getSize() == 3
    assert rentRepo.getAll()[2].getIDC() == "10"
    assert rentRepo.getAll()[2].getIDM() == "3"
    assert rentRepo.getAll()[2].getIsRented() == True
    