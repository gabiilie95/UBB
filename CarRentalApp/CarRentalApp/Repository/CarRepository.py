class CarRepository():
    
    def __init__(self):
        self.__carList = []
    
    def addCar(self, car):
        if car.isInList(car.getNr()) == False:
            self.__carList.append(car)
        else:
            raise ValueError("A car with the same number already exists.")
        
    def findByNr(self, nr):
        cars = self.__carList
        for car in cars:
            if car.getNr() == nr:
                return True
        return False

    def getAll(self):
        return self.__carList
        
            
