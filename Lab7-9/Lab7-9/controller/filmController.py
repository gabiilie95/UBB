from domain.film.film import Film

class FilmController():
    
    def __init__(self, repo, validator):
        self.__repo = repo
        self.__valid = validator
        
    def createFilm(self, idf, title, director, genre):
        '''
        Creates and stores a film
        Returns the film
        '''
        film = Film(idf, title, director, genre)
        self.__valid.validate(film)
        self.__repo.store(film)
        
        return film

    
    def getAllFilms(self):
        return self.__repo.getAll()

    
    def modifyFilm(self, idf, title, director, genre):
        '''
        Modifies the film with an id of idf
        Returns the newly modified film
        '''
        film = Film(idf, title, director, genre)
        self.__repo.modify(film)
        return film

    
    def deleteFilm(self, idf):
        '''
        Delete a film by id
        If the id does not exist, raise ValueError
        '''
        self.__repo.delete(idf)