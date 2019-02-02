from strategy import LoudQuackStrategy
from strategy import GentleQuackStrategy
from strategy import OnForTenSecondsStrategy


# strategy objects
loud_quack = LoudQuackStrategy()
gentle_quack = GentleQuackStrategy()
ten_seconds = OnForTenSecondsStrategy()


class Duck(object):

    def __init__(self, quack_strategy, light_strategy):
        self._quack_strategy = quack_strategy
        self._light_strategy = light_strategy

    def quack(self):
        self._quack_strategy.quack()

    def lights_on(self):
        self._light_strategy.lights_on()


# Types of Ducks
class VillageDuck(Duck):

    def __init__(self):
        super(VillageDuck, self).__init__(loud_quack, None)

    @staticmethod
    def go_home():
        print("Go to the river")


class ToyDuck(Duck):

    def __init__(self):
        super(ToyDuck, self).__init__(gentle_quack, ten_seconds)


class CityDuck(Duck):

    def __init__(self):
        super(CityDuck, self).__init__(gentle_quack, None)


class RobotDuck(Duck):
    
    def __init__(self):
        super(RobotDuck, self).__init__(loud_quack, ten_seconds)


print("-------------------------")
print("RoboDuck")
robo = RobotDuck()
robo.quack()
robo.lights_on()
print("-------------------------")

print("CityDuck")
city = CityDuck()
city.quack()
print("-------------------------")

print("ToyDuck")
toy = ToyDuck()
toy.quack()
toy.lights_on()
print("-------------------------")

print("VillageDuck")
village = VillageDuck()
village.quack()


