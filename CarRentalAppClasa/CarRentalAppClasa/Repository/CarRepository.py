from Domain.car import car

class CarRepository():
    """description of class"""


    def __init__(self, fisier):
        self.__fisier = fisier

    def getAll(self):
        f = open(self, __fisier, 'r')
        cars = []
        for linie in f:
            atrs = linie.split(",")
            m=car(atrs[0],atrs[1],atrs[2],atrs[3])
            cars.append(m)
        f.close()

        return cars


    def update(self, car):
        all = self.getAll()
        c = self.findById(car.getNr())
        all[all.index(c)] = car
        with open(self.__fisier, 'w') as f:
            f.write(c.getNr()+','+c.getModel()+','+c.getType()+','+c.getPricePerDay)


