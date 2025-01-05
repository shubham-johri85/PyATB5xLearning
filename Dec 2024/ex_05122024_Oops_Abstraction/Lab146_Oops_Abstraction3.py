from abc import ABC, abstractmethod


class GearBox(ABC):
    @abstractmethod
    def set_gear(self):
        pass


class Engine(GearBox):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Engine):
    def start(self):
        print("starting")

    def set_gear(self):
        print("Gear is set")

    def stop(self):
        print("Stop the car")

    def ride(self):
        self.start()
        self.set_gear()
        self.stop()

Alto = Car()
Alto.ride()
