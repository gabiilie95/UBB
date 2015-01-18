from Domain.car import car


def test_car():
    car1=car("01CJWAS", "Dacia", "Family", 51)
    assert car1.getNr() == "01CJWAS"
    assert car1.getModel() == "Dacia"
    assert car1.getType() == "Family"
    assert car1.getPricePerDay() == 51