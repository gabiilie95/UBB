class movie():
    """Creates a movie, (ID, Title, Genre, Director)"""
    
    def __init__(self, id, title, genre, director):
        self.__id= id
        self.__title = title.title()
        self.__genre = genre.title()
        self.__director = director.title()

#Functiile GET

    def getID(self):
        '''
        Returns a movie's ID
        '''
        return self.__id 


    def getTitle(self):
        '''
        Returns a movie's Title
        '''
        return self.__title


    def getGenre(self):
        '''
        Returns a movie's Genre
        '''
        return self.__genre


    def getDirector(self):
        '''
        Returns a movie's Director
        '''
        return self.__director

#Functiile SET

    def setID(self, id):
        '''
        Sets a movie's ID
        '''
        self.__id = id


    def setTitle(self, title):
        '''
        Sets a movie's Title
        '''
        self.__title = title


    def setGenre(self, genre):
        '''
        Sets a movie's Genre
        '''
        self.__genre = genre


    def setDirector(self, director):
        '''
        Sets a movie's Director
        '''
        self.__director = director



    def __equ__(self, movie):
        '''
        Verifica daca id-ul unui movie exista deja
        '''
        if __self.getID() == movie.getID():
            return True
        return False
