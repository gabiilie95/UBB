from domain.client.client import Client

class ClientController():
    
    def __init__(self, repo, validator):
        self.__repo = repo
        self.__valid = validator
        
    def createClient(self, idc, name, cnp):
        '''
        Create a client object and stores it
        Returns the client
        '''
        client = Client(idc, name, cnp)
        self.__valid.validate(client)
        self.__repo.store(client)
        return client

    
    def getAllClients(self):
        '''
        Returns the list of clients
        '''
        return self.__repo.getAll()

    
    def modifyClient(self, idc, name, cnp):
        '''
        Modified the client with an id of idc
        Returns the newly modified client
        '''
        client = Client(idc, name, cnp)
        self.__repo.modify(client)
        return client
    
    
    def deleteClient(self, idc):
        '''
        Delete a client by id
        If the id does not exist, raise ValueError
        '''
        self.__repo.delete(idc)
        
        
    def getByID(self, idc):
        '''
        Get a client by id
        Return the client if found
        Raise ValueError if not found
        '''
        return self.__repo.getByID(idc)
        
        
        