
class rent_validator():

    
    def validate(self, rent):
        errors = []
        if rent.getIDC() == "": errors.append("The client ID can't be empty")
        if rent.getIDM() == "": errors.append("The film ID can't be empty")
        if len(errors) > 0:
            raise ValueError(errors)
        
    
    