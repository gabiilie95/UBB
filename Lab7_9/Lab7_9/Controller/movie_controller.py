from Domain.movie import movie

class movie_controller():
    
    def __init__(self, repo, validator):
        self.__repo = repo
        self.__valid = validator
        
    def createMovie(self, id, title, director, genre):
       
        '''Validates and creates a movie object, returns it'''

        movie1 = movie(id, title, director, genre)
        self.__valid.validate(movie1)
        self.__repo.addMovie(movie1)
        
        return movie1

    
    def getAllMovies(self):
        
        '''Returns all movies'''

        return self.__repo.getAll()

    
    def modifyMovie(self, id, title, director, genre):
       
        '''Modifies a movie'''

        movie1 = movie(id, title, director, genre)
        self.__repo.modifyMovie(movie1)

        return movie1

    
    def deleteMovie(self, id):
        
        '''Deletes a movie, if the movie doesen't exist raise ValueError'''

        self.__repo.deleteMovie(id)


