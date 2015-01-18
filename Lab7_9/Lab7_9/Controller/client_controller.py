from Domain.client import client

class client_controller():

    def __init__(self, repository, validator):
        self.__repo = repository
        self.__valid = validator
        
    def createClient(self, id, name, cnp):
        
        '''Validates and creates a client type object, and returns it'''
        
        client1 = client(id, name, cnp)
        self.__valid.validate(client1)
        self.__repo.addClient(client1)
        return client1

    
    def getAllClients(self):
        
        '''Returns the list of clients'''

        return self.__repo.getAll()

    
    def modifyClient(self, id, name, cnp):
        
        '''Modifies a client object, and returns it'''

        client1 = client(id, name, cnp)
        self.__repo.modifyClient(client1)
        return client1
    
    
    def deleteClient(self, id):
        
        '''Deletes a client, if the client doesen't exist Raises ValueError'''

        self.__repo.deleteClient(id)


    def orderClientByName(self):
        
        '''Orders the list of clients by name'''

        self.__repo.orderByName()


    def getClientByID(self, id):

        '''Returns a client type object based on the id of that client.'''

        self.__repo.getClientByID(id)


    
