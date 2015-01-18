class client():
    
    """Creates a client type object (ID, Name, CNP)"""

    def __init__(self, id, name, cnp):
        self.__id = id
        self.__name = name.title()
        self.__cnp = cnp

#Get

    def getID(self):
        return self.__id

    def getName(self):
        return self.__name.title()

    def getCNP(self):
        return self.__cnp

#Set

    def setID(self, id):
        self.__id = id

    def setName(self, name):
        self.__name = name

    def setCNP(self, cnp):
        self.__cnp = cnp

#Equ

    def __equ__(self, client):
        return self.__id == client.getID()