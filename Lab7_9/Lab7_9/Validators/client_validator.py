class client_validator():

    def validate(self, client):
        
        errors = []

        if client.getID()  == '':
            errors.append("The ID of the client can't be empty. ")
        if client.getName() == '':
            errors.append("The name of the client can't be empty. ")
        if client.getCNP() == '':
            errors.append("The CNP of the client can't be empty. ")

        if len(errors) > 0:
            raise ValueError(errors)