"""You don’t always have to start from scratch when writing a class"""
#THE CAR CLASS
from cgi import MiniFieldStorage

class Car:

    #INIT METOD
    def __init__(self, make,model,year):
        """inicializa los atributos"""
        self.make =  make
        self.model = model
        self.year = year
        """Setting a Default Value for an Attribute"""
        self.odometer_reading = 0

    #Descriptive car a car
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.model} {self.model}"
        return long_name.title()

    #Read odometer of each car
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
       
    
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
       
        if mileage>=self.odometer_reading:
            self.odometer_reading = mileage      
        else:
            print("You can't roll back an odomoter")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles

class Bat


class ElectricCar(Car):
    """Represent aspect of a car, specif to electric vehicles"""
    def __init__(self, make,model,year): 
        """Initialize attributes of the parent class
        them initialize attributes specific to an electric car"""

        super().__init__(make, model, year) #la funcion super es una fucnion especial que le permite llamar un metodo de la clase padre
        self.battery_size = 75              #le dice a python que llame a init a esta seccion



def main():

    my_new_car = Car('AUDI','a4',2019)
    print(my_new_car.get_descriptive_name())

    """Modifying an Attribute’s Value Directly"""
    my_new_car.odometer_reading = 23
    my_new_car.read_odometer()
    my_new_car.update_odometer(50)
    my_new_car.read_odometer()
    my_new_car.update_odometer(70)
    my_new_car.read_odometer()
    my_new_car.increment_odometer(20)
    my_new_car.read_odometer()

    my_tesla = ElectricCar('tesla', 'model s', 2019)
    print(my_tesla.get_descriptive_name())
    my_tesla.describe_battery()

if __name__ == "__main__":
    main()


class ElectriCar(Car):

    def fill_gas_tank(self):
        """Electric cars don't have gas thanks"""
        print("This car doesn't need a gas tanki")

    class Battery:
        """A simple attemp to model a battery for an electric car"""

        def __init__(self, battery_size = 75):
            """initialize the battery's attributes"""
            self.battery_size = battery_size

        def describe_battery(self):
            """print description of batery"""
            print(f"this bateria of car is: {self.battery_size}")

