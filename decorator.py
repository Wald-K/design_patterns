import abc


class Car(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def assemble(self):
        pass


class CarDecorator(Car):
    def __init__(self, car):
        self.__car = car

    def assemble(self):
        self.__car.assemble()


class BasicCar(Car):
    def assemble(self):
        print("Basic Car.")


class SportsCar(CarDecorator):
    def __init__(self, car):
        super(SportsCar, self).__init__(car)

    def assemble(self):
        super(SportsCar, self).assemble()
        print("Adding features of Sports Car.")


class LuxuryCar(CarDecorator):
    def __init__(self, car):
        super(LuxuryCar, self).__init__(car)

    def assemble(self):
        super(LuxuryCar, self).assemble()
        print("Adding features of Luxury Car.")


if __name__ == '__main__':
    sports_car = SportsCar(BasicCar())
    sports_car.assemble()
    print("-----")

    sports_luxury_car = SportsCar(LuxuryCar(BasicCar()))
    sports_luxury_car.assemble()
    print("-----")