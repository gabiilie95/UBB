from Domain.client import client

class client_controller():
    
    def __init__(self, repo, validator):
        self.__repo = repo
        self.__valid = validator
        
    def createClient(self, idc, name, cnp):
        '''
        Create a client object and stores it
        Returns the client
        '''
        Client = client(idc, name, cnp)
        self.__valid.validate(Client)
        self.__repo.addClient(Client)
        return Client

    
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
        Client = client(idc, name, cnp)
        self.__repo.modify(Client)
        return Client
    
    
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
        
        
        