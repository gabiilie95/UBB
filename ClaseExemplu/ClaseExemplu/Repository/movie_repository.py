
class movie_repository():
    '''
    Stores all available movies
    '''
    def __init__(self):
        self.__movieList = []
 
        
    def store(self, movie):
        '''
        Adds a movie at the end of the list of movies 
        '''
        if self.findByID(movie.getID()) == False:
            self.__movieList.append(movie)
        else:
            raise ValueError("There is a movie with the same ID.")
    
    def getAll(self):
        '''
        Returns the list of movies
        '''
        return self.__movieList
    
    
    def getSize(self):
        '''
        Returns the size of the list of movies
        '''
        return len(self.__movieList)
    
    
    def findByID(self, idf):
        '''
        Search for a movie with the ID of idf
        Return True if the ID exists
        Return False if the ID doesn't exist
        '''
        movies = self.__movieList
        for movie in movies:
            if movie.getID() == idf:
                return True
        return False

    
    def modify(self, movie2):
        '''
        Search the list for the movie with the id movie2.getID() and replace it with movie2
        movie2 - movie object
        Preconditions: the id of movie must already exist
        '''
        if self.findByID(movie2.getID()) == True:
            for movie in self.__movieList:
                if movie.getID() == movie2.getID():
                    movie.setTitle(movie2.getTitle())
                    movie.setDirector(movie2.getDirector())
                    movie.setGenre(movie2.getGenre())
        else:
            raise ValueError("Can't modify the movie because the id doesn't exist")

    
    def delete(self, idf):
        '''
        Delete the movie with an ID of idf
        Preconditions: the id must exist, otherwise the list will not be modified
        '''
        if self.findByID(idf) == True:
            i = 0
            while i < len(self.__movieList):
                if self.__movieList[i].getID() == idf:
                    self.__movieList.pop(i)
                i = i + 1
        else:
            raise ValueError("Can't delete the movie because the id doesn't exist")
        
        
    def getMovieByID(self, idf):
        '''
        Return the movie with an ID of idf
        Raise ValueError if the ID does not exist
        '''
        movies = self.__movieList
        for movie in movies:
            if movie.getID() == idf:
                return movie
        raise ValueError("The movie ID does not exist")   
    
    
    def addClientTomovie(self, idf, client):
        '''
        idf - the ID of the movie
        client - the client we are renting the movie to
        '''
        movies = self.__movieList
        for movie in movies:
            if movie.getID() == idf:
                movie.setIsrented(client)
        
        
        
    
    
    
