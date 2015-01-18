class UI():
    
    """Creates the console window."""

    def __init__(self, client_controller, movie_controller, rent_controller, clients_file, movies_file, rents_file):
        self.__client_controller = client_controller
        self.__movie_controller = movie_controller
        self.__rent_controller = rent_controller
        self.__clients_file = clients_file
        self.__movies_file = movies_file
        self.__rents_file = rents_file

    
    def print_menu(self):

        print("1. Add/Modify/Delete")
        print("2. Rent/Return")
        print("3. Print lists")
        print("4. Find")
        print("5. Filters")
        print("0. Exit")

    
    def print_submenu1(self):

        print("     1. Add Client")
        print("     2. Modify Client")
        print("     3. Delete Client")
        print("     4. Add Movie")
        print("     5. Modify Movie")
        print("     6. Delete Movie")

    
    def print_submenu2(self):

        print("     1. Rent Movie")
        print("     2. Return Movie")

    
    def print_submenu3(self):

        print("     1. All Clients")
        print("     2. All Movies")
        print("     3. Rented Films")


    def print_submenu4(self):

        print("     1. Find Client by ID")
        print("     2. Find Movie by ID")

    
    def print_submenu5(self):

        print("     1. Order by Name")

    def main(self):
        while True:
            self.print_menu()
            try:
                option = int(input("Option: "))
                if option == 1:
                    self.print_submenu1()
                    try:
                        suboption = int(input("Option: "))
                        if suboption == 1:
                            self.addClient()
                        elif suboption == 2:
                            self.modifyClient()
                        elif suboption == 3:
                            self.deleteClient()
                        elif suboption == 4:
                            self.addMovie()
                        elif suboption == 5:
                            self.modifyMovie()
                        elif suboption == 6:
                            self.deleteMovie()
                    except ValueError:
                        print("Please enter a valid option.")
                 
                elif option == 2:
                    self.print_submenu2()
                    try:
                        suboption = int(input("Option: "))
                        if suboption == 1:
                            self.rentMovie()
                        elif suboption == 2:
                            self.returnMovie()
                    except ValueError:
                        print("Please enter a valid option.")

                elif option == 3:
                    self.print_submenu3()
                    try:
                        suboption = int(input("Option: "))
                        if suboption == 1:
                            self.printClients()
                        elif suboption == 2:
                            self.printMovies()
                        elif suboption == 3:
                            self.printRented()
                    except ValueError:
                        print("Please enter a valid option.")

                elif option == 4:
                    self.print_submenu4()
                    try:
                        suboption = int(input("Option: "))
                        id = input("ID: ")
                        if suboption == 1:
                            self.getClientByID(id)
                        elif suboption == 2:
                            self.getMovieByID(id)
                    except ValueError:
                        print("Please enter a valid option.")
                    
                elif option == 5:
                    self.print_submenu5()
                    try:
                        suboption = int(input())
                        if suboption == 1:
                            self.orderClientsByName()

                    except ValueError:
                        print("Please enter a valid option.")

                elif option == 0:
                    self.__clients_file.storeToFile()
                    self.__movies_file.storeToFile()
                    self.__rents_file.storeToFile()
                    break

                else:
                    print("Please enter a valid option.")

            except ValueError:
                print("Please enter a valid option.")

    def addClient(self):
        id = input("ID: ")
        name = input("Name: ")
        cnp = input("CNP: ")
        try:
            self.__client_controller.createClient(id, name, cnp)
            print("The clent has been added.")
        except ValueError as msg:
            print(msg)

    
    def modifyClient(self):
        id = input("ID: ")
        name = input("Name: ")
        cnp = input("CNP: ")
        try:
            self.__client_controller.modifyClient(id, name, cnp)
            print ("The client has been modified")
        except ValueError as msg:
            print (msg)
            
    
    def deleteClient(self):
        id = input("ID: ")
        try:
            self.__client_controller.deleteClient(id)
            print ("The client has been deleted")
        except ValueError as msg:
            print (msg)

    
    def addMovie(self):
        id = input("ID: ")
        title = input("Title: ")
        director = input("Director: ")
        genre = input("Genre: ")
        try:
            self.__movie_controller.createMovie(id, title, director, genre)
            print ("The film has been added.")
        except ValueError as msg:
            print (msg)
    
    
    def modifyMovie(self):
        id = input("ID: ")
        title = input("Title: ")
        director = input("Director: ")
        genre = input("Genre: ")        
        try:
            self.__movie_controller.modifyMovie(id, title, director, genre)
            print ("The film has been modified")
        except ValueError as msg:
            print (msg)
            
            
    def deleteMovie(self):    
        id = input("ID: ")
        try:
            self.__movie_controller.deleteMovie(id)
            print ("The film has been deleted")
        except ValueError as msg:
            print (msg)
    

    def printClients(self):
        allClients = self.__client_controller.getAllClients()
        for client in allClients:
            print ("ID: " + client.getID() + "    Name: " + client.getName() + 
                   "    CNP: " + client.getCNP() )
    

    def printMovies(self):
        allMovies = self.__movie_controller.getAllMovies()
        for movie in allMovies:
            print("ID: " + movie.getID() + "    Title: " + movie.getTitle() + 
                  "    Director: " + movie.getDirector() + "    Genre: " + movie.getGenre())
    
    
    def rentMovie(self):
        idc = input("Client ID: ")
        idm = input("Movie ID: ")
        try:
            self.__rent_controller.createRent(idc, idm)
            print ("The film has been rented")
        except ValueError as msg:
            print (msg)
            
    
    def printRented(self):
        for rent in self.__rent_controller.getAllRents():
            print ("ID client: " + rent.getIDC() + "    ID film: " + rent.getIDM() + "    is rented: " + str(rent.getIsRented()))
            
            
    def returnMovie(self):
        idm = input("Movie ID: ")
        self.__rent_controller.returnMovie(idm)
            
    
    def orderClientsByName(self):
        self.__client_controller.orderClientByName()


    def getClientByID(self, id):
        client = self.__client_controller.getClientByID(id)
        if client == 0:
            print("The client doesen't exist.")        
        else:
            print ("ID: " + client.getID() + "    Name: " + client.getName() + 
                   "    CNP: " + client.getCNP() )
        


    def getMovieByID(self, id):
        movie = self.__movie_controller.getMovieByID(id)
        if movie == 0:
            print("The movie doesen't exist.")
        else:
            print("ID: " + movie.getID() + "    Title: " + movie.getTitle() + 
                  "    Director: " + movie.getDirector() + "    Genre: " + movie.getGenre())
        