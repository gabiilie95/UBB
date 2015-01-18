
class Ui():
    
    def __init__(self, movie_controller, client_controller, rent_controller):
        self.__movie_controller = movie_controller
        self.__client_controller = client_controller
        self.__rent_controller = rent_controller
        
        
    def addMovie(self):
        idf = input("ID: ")
        title = input("Title: ")
        director = input("Director: ")
        genre = input("Genre: ")
        try:
            self.__movie_controller.createmovie(idf, title, director, genre)
            print ("The movie has been added.")
        except ValueError as msg:
            print (msg)
                
                
    def printAllMovies(self):
        allmovies = self.__movie_controller.getAllmovies()
        for movie in allmovies:
            print("ID: " + movie.getID() + "    Title: " + movie.getTitle() + 
                  "    Director: " + movie.getDirector() + "    Genre: " + movie.getGenre())
            
    
    
    def modifyMovie(self):
        idf = input("ID: ")
        title = input("Title: ")
        director = input("Director: ")
        genre = input("Genre: ")        
        try:
            self.__movie_controller.modifyMovie(idf, title, director, genre)
            print ("The movie has been modified")
        except ValueError as msg:
            print (msg)
            
            
    def deleteMovie(self):    
        idf = input("ID: ")
        try:
            self.__movie_controller.deletemovie(idf)
            print ("The movie has been deleted")
        except ValueError as msg:
            print (msg)
            
            
    def addClient(self):
        idc = input("ID: ")
        name = input("Name: ")
        cnp = input("CNP: ")
        try:
            self.__client_controller.createClient(idc, name, cnp)
            print ("The client has been added")
        except ValueError as msg:
            print (msg)
            
            
    def printAllClients(self):
        allClients = self.__client_controller.getAllClients()
        for client in allClients:
            print ("ID: " + client.getID() + "    Name: " + client.getName() + 
                   "    CNP: " + client.getCNP() )
            
            
    def modifyClient(self):
        idc = input("ID: ")
        name = input("Name: ")
        cnp = input("CNP: ")
        try:
            self.__client_controller.modifyClient(idc, name, cnp)
            print ("The client has been modified")
        except ValueError as msg:
            print (msg)
            
    
    def deleteClient(self):
        idc = input("ID: ")
        try:
            self.__client_controller.deleteClient(idc)
            print ("The client has been deleted")
        except ValueError as msg:
            print (msg)
            
            
    def rentMovie(self):
        idc = input("Client ID: ")
        idf = input("movie ID: ")
        try:
            self.__rent_controller.createrent(idc, idf)
            print ("The movie has been rented")
        except ValueError as msg:
            print (msg)
            
    
    def showrents(self):
        for rent in self.__rent_controller.getAllrents():
            print ("ID client: " + rent.getIDC() + "    ID movie: " + rent.getIDF() + "    is rented: " + rent.getIsrented())
            
            
    def returnMovie(self):
        idf = input("movie ID: ")
        self.__rent_controller.returnmovie(idf)
            
    
    def orderClientsByName(self):
        try:
            clients = self.__rent_controller.orderClientsByName()
        except ValueError as msg:
            print (msg)
    
            
    def printMenu(self):
        print ("1. Add movie")
        print ("2. Modify movie")
        print ("3. Delete movie")
        print ("4. Print all movies")
        print ("5. Add client")
        print ("6. Modify client")
        print ("7. Delete client")
        print ("8. Print all clients")
        print ("9. rent movie to client")
        print ("10. Return a movie")
        print ("11. Print all rented movies")
        print ("12. Order clients with rented movies by name")
        print ("0. Exit")
                
    def main(self):
        while True:
            self.printMenu()
            try:
                option = int (input("Option: "))
                if option == 0:
                    return False
                elif option == 1:
                    self.addMovie()
                elif option == 2:
                    self.modifyMovie()
                elif option == 3:
                    self.deletemovie()
                elif option == 4:
                    self.printAllmovies()
                elif option == 5:
                    self.addClient()
                elif option == 6:
                    self.modifyClient()
                elif option == 7:
                    self.deleteClient()
                elif option == 8:
                    self.printAllClients()
                elif option == 9:
                    self.rentMovie()
                elif option == 10:
                    self.returnMovie()
                elif option == 12:
                    self.orderClientsByName()
                elif option == 11:
                    self.showrents()
                elif option == 1:
                    self.orderClientsByName()
                else:
                    print ("Please enter a valid option")
            except ValueError:
                print ("Please enter a valid option")
                
    
            
            
            
            
            
            