from domain.client.client import Client

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
        
        
        
class ClientFileRepository(ClientRepository):
    '''
    Store/retrieve clients from file
    '''
    def __init__(self, fileN):
        ClientRepository.__init__(self)
        self.__fileN = fileN
        self.loadFromFile()
    
    def loadFromFile(self):
        try:
            f = open(self.__fileN, "r")
        except IOError:
            return
        line = f.readline().strip()
        while line != "":
            attrs = line.split(";")
            client = Client(attrs[0], attrs[1], attrs[2])
            ClientRepository.store(self, client)
            line = f.readline().strip()
        f.close()
        
    
    def storeInFile(self):
        try:
            f = open(self.__fileN, "w")
        except IOError:
            return
        allClients = ClientRepository.getAll(self)
        for client in allClients:
            f.write(client.getID() + ";" + client.getName() + ";" + client.getCNP() + "\n")
        f.close()
        
        
        
        
        
        
                
                
                
