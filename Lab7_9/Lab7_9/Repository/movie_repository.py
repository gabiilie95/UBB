class movie_repository():

    """Creates a repository of movies"""
    
    def __init__(self):
        self.__movies = []

    def addMovie(self, movie):

        '''Appends a movie at the end of the list.'''

        if self.findByID(movie.getID()) == False:
            self.__movies.append(movie)

        else:
            raise ValueError("A movie with the same ID already exists.")

    def deleteMovie(self, id):

        '''Deletes a movie from the list.'''
        
        if self.findByID(id):
            i = 0
            while i < len(self.__movies):
                if self.__movies[i].getID() == id:
                    self.__movies.pop(i)
                i += 1
        else:
            raise ValueError("The movie doesen't exist.")

    def getAll(self):

        '''Returns the list of movies.'''

        return self.__movies

    def findByID(self, id):

        '''Searches for a ID in the movies list, returns a bool if found or not found.'''

        movies = self.__movies
        for movie in movies:
            if movie.getID() == id:
                return True
        return False

    def getSize(self):

        '''Return the size(number of elements) of the list.'''

        return len(self.__movies)

    def modifyMovie(self, movie2):

        '''Modifies a movie with a given ID.'''

        if self.findByID(movie2.getID()) == True:
            for movie1 in self.__movies:
                if movie2.getID() == movie1.getID():
                    movie1.setTitle(movie2.getTitle())
                    movie1.setDirector(movie2.getDirector())
                    movie1.setGenre(movie2.getGenre())

        else:
            raise ValueError("The ID doesen't exist.")