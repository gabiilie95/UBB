
class Film():

    def __init__(self, idf, title, director, genre):
        self.__idf = idf
        self.__title = title
        self.__director = director
        self.__genre = genre


    def getID(self):
        return self.__idf


    def getTitle(self):
        return self.__title


    def getDirector(self):
        return self.__director


    def getGenre(self):
        return self.__genre
    
    
    def setID(self, idf):
        self.__idf = idf
        
    
    def setTitle(self, title):
        self.__title = title
        
    
    def setDirector(self, director):
        self.__director = director
        
    
    def setGenre(self, genre):
        self.__genre = genre

    
    def __eq__(self, film2):
        if self.getID() == film2.getID():
            return True
        return False
    