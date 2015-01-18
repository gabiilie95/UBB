
class ClientRepository():
    '''
    Stores all clients
    '''
    def __init__(self):
        self.__clientList = []
 
        
    def store(self, client):
        '''
        Adds a client at the end of the list of clients 
        '''
        if self.findByID(client.getID()) == False:
            self.__clientList.append(client)
        else:
            raise ValueError("There is a client with the same ID.")
    
    def getAll(self):
        '''
        Returns the list of clients
        '''
        return self.__clientList
    
    
    def getSize(self):
        '''
        Returns the size of the list of clients
        '''
        return len(self.__clientList)
    
    
    def findByID(self, idc):
        '''
        Search for a client with the ID of idc
        Return True if the ID exists
        Return False if the ID doesn't exist
        '''
        clients = self.__clientList
        for client in clients:
            if client.getID() == idc:
                return True
        return False

    def returnByID(self, id):
        '''Search for a id, returns a client object, if id doesen't exist doesen't return anything'''
        if findByID(id) == True:
            clients = self.__clientList
            for client in clients:
                if client.getID == id:
                    return client


    def modify(self, client2):
        '''
        Search the list for the client with the id client2.getID() and replace it with client2
        client2 - client object
        Preconditions: the id of client must already exist
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
    
    
    def rentFilmToClient(self, idc, film):
        '''
        idc - The ID of the client
        film - the film we must rent
        '''
        clients = self.__clientList
        for client in clients:
            if client.getID() == idc:
                client.rentFilm(film)
        
    
    def orderByName(self):
        '''
        Order clients which rented films alphabetically
        return a list containing the clients with rented films alphabetically
        '''
        clients =[]
        for client in self.__clientList:
            if len(client.getAllFilms()) > 0:
                clients.append(client.getName())
        for i in range(0, len(clients) - 1):
            for j in range(i+1, len(clients)):
                if clients[i] > clients[j]:
                    aux = clients[i]
                    clients[i] = clients[j]
                    clients[j] = aux
        return clients
        
        
        
        
        
        
                
                
                
