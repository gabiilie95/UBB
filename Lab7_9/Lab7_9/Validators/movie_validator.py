class movie_validator():

    def validate(self, movie):
        
        errors = []

        if movie.getID()  == '':
            errors.append("The ID of the movie can't be empty. ")
        if movie.getTitle() == '':
            errors.append("The name of the movie can't be empty. ")
        if movie.getDirector() == '':
            errors.append("The director of the movie can't be empty. ")
        if movie.getGenre() == '':
            errors.append("The genre of the movie can't be empty.")

        if len(errors) > 0:
            raise ValueError(errors)