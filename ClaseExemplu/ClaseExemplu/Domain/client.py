class client():
    """Creates a client, (ID, Name, CNP)"""

    def __init__(self, id, name, cnp):
        self.__id = id
        self.__name = name.title()
        self.__cnp = cnp

#Functiile GET

    def getID(self):
        '''
        Returns a client's ID
        '''
        return self.__id


    def getName(self):
        '''
        Returns a client's Name
        '''
        return self.__name 


    def getCNP(self):
        '''
        Returns a client's CNP
        '''
        return self.__cnp

#Functiile SET

    def setID(self, id):
        '''
        Sets a client's ID
        '''
        self.__id = id


    def setName(self, name):
        '''
        Sets a client's Name
        '''
        self.__name = name


    def setCNP(self, cnp):
        '''
        Sets a client's CNP
        '''
        self.__cnp = cnp



    def __eq__(self, client):
        return self.__id == client.getID()


