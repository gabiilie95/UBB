class rent():

    """Creates a rent type object (Client's ID, Movie's ID), automatially sets the object as rented"""

    def __init__(self, idc, idm):
        self.__idc = idc
        self.__idm = idm
        self.__isRented = True

#Get

    def getIDC(self):
        return self.__idc

    def getIDM(self):
        return self.__idm
    
    def getIsRented(self):
        return self.__isRented

#set

    def setIDC(self, idc):
        self.__idc = idc
    
    def setIDM(self, idm):
        self.__idm = idm
    
    def setIsRented(self):
        self.__isRented = True

    def setIsNotRented(self):
        self.__isRented = False