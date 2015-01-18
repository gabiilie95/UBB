
class RentValidator():

    
    def validate(self, rent):
        errors = []
        if rent.getIDC() == "": errors.append("The client ID can't be empty")
        if rent.getIDF() == "": errors.append("The film ID can't be empty")
        if len(errors) > 0:
            raise ValueError(errors)
        
    
    