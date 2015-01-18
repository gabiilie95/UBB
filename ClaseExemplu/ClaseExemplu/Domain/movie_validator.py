
class movie_validator():
    
    def validate(self, Movie):
        errors = []
        
        if Movie.getID() == "": errors.append("ID can't be empty")
        if Movie.getTitle() == "": errors.append("Title can't be empty")
        if Movie.getDirector() == "": errors.append("The movie must have a director")
        if Movie.getGenre() == "": errors.append("The movie must have a genre")
        
        if len(errors) > 0:
            raise ValueError(errors)