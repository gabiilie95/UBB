from Repository.client_repository import client_repository
from Domain.client_validator import client_validator
from Controller.client_controller import client_controller

def test_client_controller():
    repo = client_repository()
    valid = client_validator()
    ctrl = client_controller(repo, valid)
    
    ''' Create client tests '''
    client1 = ctrl.createClient("1", "gabi", "1111")
    assert client1.getID() == "1"
    assert client1.getName() == "Gabi"
    assert client1.getCNP() == "1111"
    allClients = ctrl.getAllClients()
    assert len(allClients) == 1
    assert allClients[0] == client1
    try:
        ctrl.createClient("1", "gabi", "2222")
        assert False
    except ValueError:
        assert True
    
    ''' Modify client test '''
    client = ctrl.modifyClient("1", "gabi2", "222222")
    assert len(ctrl.getAllClients()) == 1
    assert ctrl.getAllClients()[0] == client
    assert ctrl.getAllClients()[0].getCNP() == "222222"
    
    assert ctrl.getByID("1") == client
    try:
        ctrl.getByID("10")
        assert False
    except ValueError:
        assert True
    
    ''' Delete client test '''
    ctrl.deleteClient("1")
    assert len(ctrl.getAllClients()) == 0
        
test_client_controller()