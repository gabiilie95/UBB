from Car import car


def testCar():
    car("01CJWAT", "Dacia", "Family", 58)
    assert car.getModel_name == 'Dacia'
    assert car.getNr == '01CJWAT'
    assert car.getType == 'Family'
    assert car.getPrice_per_day == 58
    assert car.getIsRented == True
    car.setIsNotRented
    assert car.getIsRented == False