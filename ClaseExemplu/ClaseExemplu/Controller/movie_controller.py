from Domain.movie import movie

class movie_controller():
    
    def __init__(self, repo, validator):
        self.__repo = repo
        self.__valid = validator
        
    def createmovie(self, idf, title, director, genre):
        '''
        Creates and stores a movie type object
        Returns the movie list
        '''
        Movie = movie(idf, title, director, genre)
        self.__valid.validate(Movie)
        self.__repo.store(Movie)
        #self.__repo.storeInFile()
        
        return Movie

    
    def getAllmovies(self):
        return self.__repo.getAll()

    
    def modifymovie(self, idf, title, director, genre):
        '''
        Modifies the movie with an id of idf
        Returns the newly modified movie
        '''
        Movie = movie(idf, title, director, genre)
        self.__repo.modify(Movie)
        return Movie

    
    def deletemovie(self, idf):
        '''
        Delete a movie by id
        If the id does not exist, raise ValueError
        '''
        self.__repo.delete(idf)
        
        
    def getByID(self, idf):
        '''
        Get the movie with the ID idf
        Return the movie if found
        If not found, raise ValueError
        '''
        return self.__repo.getMovieByID(idf)
        
        
    def loadFromFile(self):
        self.__repo.loadFromFile()    
    