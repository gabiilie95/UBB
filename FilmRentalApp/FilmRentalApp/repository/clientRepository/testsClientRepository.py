from domain.client.client import Client
from repository.clientRepository.clientRepository import ClientRepository

def test_ClientRepository():
    client = Client("1", "stefan", "1234")
    client2 = Client("2", "edward", "44231")
    clientRepo = ClientRepository()
    
    ''' Store tests '''
    clientRepo.store(client)
    assert clientRepo.getSize() == 1
    clientRepo.store(client2)
    assert clientRepo.getSize() == 2
    assert clientRepo.findByID(client2.getID()) == True
    assert clientRepo.findByID(3) == False
    client3 = Client("1", "ionel", "111111")
    try:
        clientRepo.store(client3)
        assert False
    except ValueError:
        assert True
    assert clientRepo.getSize() == 2
    
    ''' Modify tests '''
    clientRepo.modify(client3)
    assert clientRepo.getSize() == 2
    assert clientRepo.getAll()[0].getName() == "ionel"
    assert clientRepo.getAll()[0].getCNP() == "111111"
    
    ''' Delete tests '''
    clientRepo.delete("1")
    assert clientRepo.getSize() == 1
    assert clientRepo.getAll()[0].getID() == "2"
    
    
test_ClientRepository()

