from Controllers.controllers import CarController


def test_filtrare():
    rep=CarRepository('cars.txt')
    l=filtrare_tip("Family")