
class car():
    """description of class"""
    def __init__(self, nr, model, tip, price_per_day):
        self.__nr=nr
        self.__model=model
        self.__tip=tip
        self.__price_per_day=price_per_day


    def getNr(self):
        return self.__nr


    def getModel(self):
        return self.__model

    
    def getType(self):
        return self.__tip


    def getPricePerDay(self):
        return self.__price_per_day


    def __eq__(self, ot):
        if ot == None:
            return False
        return self.getNr() == ot.getNr()





