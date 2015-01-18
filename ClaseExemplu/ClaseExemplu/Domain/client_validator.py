
class client_validator():
    
    def validate(self, client):
        errors = []
        
        if client.getID() =="": errors.append("ID can't be empty")
        if client.getName() =="": errors.append("Name can't be empty")
        if client.getCNP() =="": errors.append("ID can't be empty")
        
        if len(errors) > 0:
            raise ValueError(errors)