class movie():
    
    """Creates a movie type object (ID, Title, Director, Genre)"""

    def __init__(self, id, title, director, genre):
        self.__id = id
        self.__title = title.title()
        self.__director = director.title()
        self.__genre = genre.title()

#Get

    def getID(self):
        return self.__id

    def getTitle(self):
        return self.__title.title()

    def getDirector(self):
        return self.__director.title()

    def getGenre(self):
        return self.__genre.title()

#Set

    def setID(self, id):
        self.__id = id
    
    def setTitle(self, title):
        self.__title = title.title()

    def setDirector(self, director):
        self.__director = director.title()

    def setGenre(self, genre):
        self.__genre = genre.title()

#Equ

    def __equ__(self, movie):
        return self.__id == movie.getID()