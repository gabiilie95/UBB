from Domain.client import client
from Domain.movie import movie
from Domain.rent import rent
from Repository.client_repository import client_repository
from Repository.movie_repository import movie_repository
from Repository.rent_repository import rent_repository

class client_file():

    def __init__(self, filename, client_repository):
        self.__filename = filename
        self.__client_repository = client_repository
    

    def loadFromFile(self):
        
        try:
            f = open(self.__filename, "r")
        except IOError:
            print("skdjfhasdf")

        line = f.readline().strip()

        while line != "":

            atribs = line.split(";")
            client1 = client(atribs[0], atribs[1], atribs[2])
            self.__client_repository.addClient(client1)
            line = f.readline().strip()

        f.close()


    def storeToFile(self):

        try:
            f = open(self.__filename, "w")
        except IOError:
            print("File cannot be opened.")

        clients = self.__client_repository.getAll()


        for client in clients:
            
            cli = client.getID() + ";" + client.getName() + ";" + client.getCNP() + "\n"
            f.write(cli)

        f.close()


class movie_file():

    def __init__(self, filename, movie_repository):
        self.__filename = filename
        self.__movie_repository = movie_repository
    

    def loadFromFile(self):
        
        try:
            f = open(self.__filename, "r")
        except IOError:
            print("File cannot be opened.")

        line = f.readline().strip()

        while line != "":

            atribs = line.split(";")
            movie1 = movie(atribs[0], atribs[1], atribs[2], atribs[3])
            self.__movie_repository.addMovie(movie1)
            line = f.readline().strip()

        f.close()


    def storeToFile(self):

        try:
            f = open(self.__filename, "w")
        except IOError:
            print("File cannot be opened.")

        movies = self.__movie_repository.getAll()


        for movie in movies:
            
            mov = movie.getID() + ";" + movie.getTitle() + ";" + movie.getDirector() + ";" + movie.getGenre() + "\n"
            f.write(mov)

        f.close()


class rent_file():

    def __init__(self, filename, rent_repository):
        self.__filename = filename
        self.__rent_repository = rent_repository
    

    def loadFromFile(self):
        
        try:
            f = open(self.__filename, "r")
        except IOError:
            print("File cannot be opened.")

        line = f.readline().strip()

        while line != "":

            atribs = line.split(";")
            rent1 = rent(atribs[0], atribs[1])
            isRented = atribs[2]
            if isRented == 'True':
                rent1.setIsRented()
            else:
                rent1.setIsNotRented()
            self.__rent_repository.storeRent(rent1)
            line = f.readline().strip()

        f.close()


    def storeToFile(self):

        try:
            f = open(self.__filename, "w")
        except IOError:
            print("File cannot be opened.")

        rents = self.__rent_repository.getAll()


        for rent in rents:
            
            ren = rent.getIDC() + ";" + rent.getIDM() + ";" + str(rent.getIsRented()) + "\n"
            f.write(ren)

        f.close()
