
class FilmValidator():
    
    def validate(self, film):
        errors = []
        
        if film.getID() == "": errors.append("ID can't be empty")
        if film.getTitle() == "": errors.append("Title can't be empty")
        if film.getDirector() == "": errors.append("The film must have a director")
        if film.getGenre() == "": errors.append("The film must have a genre")
        
        if len(errors) > 0:
            raise ValueError(errors)