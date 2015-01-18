import Car
from Car import car

from CarRepository import CarRepository


nr=input()
model_name=input()
type=input()
ppd=input()

CarRepository.addCar(car(nr, model_name, type, ppd))
print(CarRepository.getAll)

file = open('car.txt', 'r')
file.close()
