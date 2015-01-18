class client_repository():

    """Creates a repository of clients"""
    
    def __init__(self):
        self.__clients = []

    def addClient(self, client):

        '''Appends a client at the end of the list.'''

        if self.findByID(client.getID()) == False:
            self.__clients.append(client)

        else:
            raise ValueError("A client with the same ID already exists.")

    def deleteClient(self, id):

        '''Deletes a client from the list.'''
        
        if self.findByID(id):
            i = 0
            while i < len(self.__clients):
                if self.__clients[i].getID() == id:
                    self.__clients.pop(i)
                i += 1
        else:
            raise ValueError("The client doesen't exist.")

    def getAll(self):

        '''Returns the list of clients.'''

        return self.__clients

    def findByID(self, id):

        '''Searches for a ID in the clients list, returns a bool if found or not found.'''

        clients = self.__clients
        for client in clients:
            if client.getID() == id:
                return True
        return False

    def getSize(self):

        '''Return the size(number of elements) of the list.'''

        return len(self.__clients)

    def modifyClient(self, client2):

        '''Modifies a client with a given ID.'''

        if self.findByID(client2.getID()) == True:
            for client1 in self.__clients:
                if client2.getID() == client1.getID():
                    client1.setName(client2.getName())
                    client1.setCNP(client2.getCNP())

        else:
            raise ValueError("The ID doesen't exist.")


    def orderByName(self):

        '''Orders the list of clients by name.'''

        n = len(self.__clients)
        for i in range(0, n-1):
            for j in range (i+1, n):
                if self.__clients[i].getName() > self.__clients[j].getName():
                    aux = self.__clients[i]
                    self.__clients[i] = self.__clients[j]
                    self.__clients[j] = aux


    def getClientByID(self, id):

        '''Returns a client by searching for an id, if the id is not found, returns 0'''

        if self.findByID(id) == True:
            clients = self.__clients
            for client in clients:
                if client.getID() == id:
                    return client
        
        return 0