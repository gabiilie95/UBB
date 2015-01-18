from Controllers.controllers import CarController

class console():
    """description of class"""
    def __init__(self, ctr):
        self.__ctr = ctr


    def runUI():
        while True:
            cmd = input("1. Filtrare \nX. Iesire")
            if cmd == '1':
                print("1")
            if cmd == 'x':
                break