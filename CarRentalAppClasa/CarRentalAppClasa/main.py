from Domain.carTests import test_car
from Controllers.controllers import CarController
from Repository.CarRepository import CarRepository
from UI.console import console



test_car()

rep = CarRepository("cars.txt")
ctr = CarController(rep)
ui=Console(ctr)

console.runUI()