
from domain.client.client import Client
from domain.client.clientValidator import ClientValidator
from domain.film.film import Film

def test_client():
    client = Client(1, "stefan fai", "1112123123123")
    client2 = Client(2, "stefan fai", "1112123123123")
    assert client.getID() == 1
    assert client.getName() == "stefan fai"
    assert client.getCNP() == "1112123123123"
    assert client != client2
    
test_client()



def test_ClientValidator():
    valid = ClientValidator()
    
    client1 = Client(1, "stefan fai", 1112123123123)
    try:
        valid.validate(client1)
        assert True
    except ValueError:
        assert False
        
    client2 = Client("", "", 1112123123123)
    try:
        valid.validate(client2)
        assert False
    except ValueError:
        assert True
        
test_ClientValidator()
        