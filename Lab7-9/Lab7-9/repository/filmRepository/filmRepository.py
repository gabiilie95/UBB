
class FilmRepository():
    '''
    Stores all available films
    '''
    def __init__(self):
        self.__filmList = []
 
        
    def store(self, film):
        '''
        Adds a film at the end of the list of films 
        '''
        if self.findByID(film.getID()) == False:
            self.__filmList.append(film)
        else:
            raise ValueError("There is a film with the same ID.")
    
    def getAll(self):
        '''
        Returns the list of films
        '''
        return self.__filmList
    
    
    def getSize(self):
        '''
        Returns the size of the list of films
        '''
        return len(self.__filmList)
    
    
    def findByID(self, idf):
        '''
        Search for a film with the ID of idf
        Return True if the ID exists
        Return False if the ID doesn't exist
        '''
        films = self.__filmList
        for film in films:
            if film.getID() == idf:
                return True
        return False

    
    def modify(self, film2):
        '''
        Search the list for the film with the id film2.getID() and replace it with film2
        film2 - film object
        Preconditions: the id of film must already exist
        '''
        if self.findByID(film2.getID()) == True:
            for film in self.__filmList:
                if film.getID() == film2.getID():
                    film.setTitle(film2.getTitle())
                    film.setDirector(film2.getDirector())
                    film.setGenre(film2.getGenre())
        else:
            raise ValueError("Can't modify the film because the id doesn't exist")

    
    def delete(self, idf):
        '''
        Delete the film with an ID of idf
        Preconditions: the id must exist, otherwise the list will not be modified
        '''
        if self.findByID(idf) == True:
            i = 0
            while i < len(self.__filmList):
                if self.__filmList[i].getID() == idf:
                    self.__filmList.pop(i)
                i = i + 1
        else:
            raise ValueError("Can't delete the film because the id doesn't exist")
        
        
    def getFilmByID(self, idf):
        '''
        Return the film with an ID of idf
        Raise ValueError if the ID does not exist
        '''
        films = self.__filmList
        for film in films:
            if film.getID() == idf:
                return film
        raise ValueError("The film ID does not exist")   
    
    
    def addClientToFilm(self, idf, client):
        '''
        idf - the ID of the film
        client - the client we are renting the film to
        '''
        films = self.__filmList
        for film in films:
            if film.getID() == idf:
                film.setIsRented(client)
        
        
        
    
    
    
