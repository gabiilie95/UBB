class client_repository():
    """Alows to create and maintain a list of clients"""
    
    def __init__(self):
        self.__clientList = []

#Adauga, sterge, modifica lista clienti

    def addClient(self, client1):
        '''
        Adds a client at the end of the list of clients 
        '''
        if self.findByID(client1.getID()) == False:
            self.__clientList.append(client1)
        else:
            raise ValueError("There is a client with the same ID.")


    def deleteClient(self):
        '''
        Deletes a client from the list, if the client does not exist, the list remains unmodified
        '''
        if self.findByID(id) == True:
            ok = 0
            for i in len(self.__clientList):
                if self.__clientList[i].getID() == idc:
                    self.__clientList.pop(i)


    def getAll(self):
        '''
        Returns the list of clients
        '''
        return self.__clientList


    def findByID(self, id):
        '''
        Search for a client with the ID of id
        Returns a bool
        '''
        clients = self.__clientList
        for client in clients:
            if client.getID() == id:
                return True
        return False


    def getSize(self):
        '''
        Returns the size of the list
        '''
        return len(self.__clientList)

    
    def modify(self, client2):
        '''
        Search the list for the client with the id client2.getID() and replace it with client2
        client2 - client object
        Pre: The ID must exist
        '''
        if self.findByID(client2.getID()) == True:
            for client in self.__clientList:
                if client.getID() == client2.getID():
                    client.setName(client2.getName())
                    client.setCNP(client2.getCNP())
        else:
            raise ValueError("Can't modify the client because the id doesn't exist")

    def delete(self, idc):
        '''
        Delete the client with an ID of idc
        Preconditions: the id must exist, otherwise the list will not be modified
        '''
        if self.findByID(idc) == True:
            i = 0
            while i < len(self.__clientList):
                if self.__clientList[i].getID() == idc:
                    self.__clientList.pop(i)
                i = i + 1
        else:
            raise ValueError("Can't delete the client because the id doesn't exist")

    def getClientByID(self, idc):
        '''
        Return the client with an ID of idc
        Raise ValueError if the ID does not exist
        '''
        clients = self.__clientList
        for client in clients:
            if client.getID() == idc:
                return client
        raise ValueError("The client ID does not exist")
        
    
    def getByID(self, idc):
        '''
        Get a client by id
        Return the client if found
        Raise ValueError if not found
        '''
        for client in self.__clientList:
            if client.getID() == idc:
                return client
        raise ValueError("Can't get client because the ID does not exist")
        

    
            