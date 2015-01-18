from repository.clientRepository.clientRepository import ClientRepository
from domain.client.clientValidator import ClientValidator
from clientController import ClientController

def test_ClientController():
    repo = ClientRepository()
    valid = ClientValidator()
    ctrl = ClientController(repo, valid)
    
    ''' Create client tests '''
    client1 = ctrl.createClient("1", "stefan", "1111")
    assert client1.getID() == "1"
    assert client1.getName() == "stefan"
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
    client = ctrl.modifyClient("1", "stefan2", "222222")
    assert len(ctrl.getAllClients()) == 1
    assert ctrl.getAllClients()[0] == client
    assert ctrl.getAllClients()[0].getCNP() == "222222"
    
    ''' Delete client test '''
    ctrl.deleteClient("1")
    assert len(ctrl.getAllClients()) == 0
        
test_ClientController()