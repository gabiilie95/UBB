
class Ui():
    
    def __init__(self, filmController, clientController, rentController):
        self.__filmController = filmController
        self.__clientController = clientController
        self.__rentController = rentController
        
        
    def addFilm(self):
        idf = input("ID: ")
        title = input("Title: ")
        director = input("Director: ")
        genre = input("Genre: ")
        try:
            self.__filmController.createFilm(idf, title, director, genre)
            print ("The film has been added.")
        except ValueError as msg:
            print (msg)
                
                
    def printAllFilms(self):
        allFilms = self.__filmController.getAllFilms()
        for film in allFilms:
            print("ID: " + film.getID() + "    Title: " + film.getTitle() + 
                  "    Director: " + film.getDirector() + "    Genre: " + film.getGenre())
            
    
    
    def modifyFilm(self):
        idf = input("ID: ")
        title = input("Title: ")
        director = input("Director: ")
        genre = input("Genre: ")        
        try:
            self.__filmController.modifyFilm(idf, title, director, genre)
            print ("The film has been modified")
        except ValueError as msg:
            print (msg)
            
            
    def deleteFilm(self):    
        idf = input("ID: ")
        try:
            self.__filmController.deleteFilm(idf)
            print ("The film has been deleted")
        except ValueError as msg:
            print (msg)
            
            
    def addClient(self):
        idc = input("ID: ")
        name = input("Name: ")
        cnp = input("CNP: ")
        try:
            self.__clientController.createClient(idc, name, cnp)
            print ("The client has been added")
        except ValueError as msg:
            print (msg)
            
            
    def printAllClients(self):
        allClients = self.__clientController.getAllClients()
        for client in allClients:
            print ("ID: " + client.getID() + "    Name: " + client.getName() + 
                   "    CNP: " + client.getCNP() )
            
            
    def modifyClient(self):
        idc = input("ID: ")
        name = input("Name: ")
        cnp = input("CNP: ")
        try:
            self.__clientController.modifyClient(idc, name, cnp)
            print ("The client has been modified")
        except ValueError as msg:
            print (msg)
            
    
    def deleteClient(self):
        idc = input("ID: ")
        try:
            self.__clientController.deleteClient(idc)
            print ("The client has been deleted")
        except ValueError as msg:
            print (msg)
            
            
    def rentFilm(self):
        idc = input("Client ID: ")
        idf = input("Film ID: ")
        try:
            self.__rentController.createRent(idc, idf)
            print ("The film has been rented")
        except ValueError as msg:
            print (msg)
            
    
    def showRents(self):
        for rent in self.__rentController.getAllRents():
            print ("ID client: " + rent.getIDC() + "    ID film: " + rent.getIDF() + "    is rented: " + rent.getIsRented())
            
            
    def returnFilm(self):
        idf = input("Film ID: ")
        self.__rentController.returnFilm(idf)
            
    
    def orderClientsByName(self):
        try:
            clients = self.__rentController.orderClientsByName()
        except ValueError as msg:
            print (msg)
    
            
    def printMenu(self):
        print ("1. Add film")
        print ("2. Modify film")
        print ("3. Delete film")
        print ("4. Print all films")
        print ("5. Add client")
        print ("6. Modify client")
        print ("7. Delete client")
        print ("8. Print all clients")
        print ("9. Rent film to client")
        print ("10. Return a film")
        print ("11. Print all rented films")
        print ("12. Order clients with rented films by name")
        print ("0. Exit")
                
    def main(self):
        while True:
            self.printMenu()
            try:
                option = int (input("Option: "))
                if option == 0:
                    return False
                elif option == 1:
                    self.addFilm()
                elif option == 2:
                    self.modifyFilm()
                elif option == 3:
                    self.deleteFilm()
                elif option == 4:
                    self.printAllFilms()
                elif option == 5:
                    self.addClient()
                elif option == 6:
                    self.modifyClient()
                elif option == 7:
                    self.deleteClient()
                elif option == 8:
                    self.printAllClients()
                elif option == 9:
                    self.rentFilm()
                elif option == 10:
                    self.returnFilm()
                elif option == 12:
                    self.orderClientsByName()
                elif option == 11:
                    self.showRents()
                elif option == 1:
                    self.orderClientsByName()
                else:
                    print ("Please enter a valid option")
            except ValueError:
                print ("Please enter a valid option")
                
    
            
            
            
            
            
            