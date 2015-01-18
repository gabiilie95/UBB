from Domain.client import client
from Repository.client_repository import client_repository



def test_ClientRepository():
    client1 = client(1, "Gabi", "1234567890")
    client2 = client(2, "Pop", "4567891023")
    clientRepo = client_repository()
    
    ''' Add clients '''

    clientRepo.addClient(client1)
    assert clientRepo.getSize() == 1
    clientRepo.addClient(client2)
    assert clientRepo.getSize() == 2
    assert clientRepo.findByID(client2.getID()) == True
    assert clientRepo.findByID(3) == False
    client3 = client(1, "Stefan", "1111111111")
    try:
        clientRepo.addClient(client3)
        assert False
    except ValueError:
        assert True
    assert clientRepo.getSize() == 2


test_ClientRepository()