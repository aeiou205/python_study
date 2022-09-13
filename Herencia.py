"""You don’t always have to start from scratch when writing a class"""
#THE CAR CLASS
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

class Battery:
    def __init__(self,battery_size=75,range=0):
        self.battery_size = battery_size
        self.range=range
    def describe_battery(self):
        """print a statement describing the battery size"""
        print(f"bateria es : {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks"""
        print("This car does not need a gas tanks!")

    def get_range(self):
        """print statement about the range this battery provides"""
        if self.battery_size == 75:
            self.range = 260
        elif self.battery_size == 100:
            self.range = 315
        print(f"this range is:{self.range}.")

class ElectricCar(Car):
    """Represent aspect of a car, specif to electric vehicles"""
    def __init__(self, make,model,year): 
        """Initialize attributes of the parent class
        them initialize attributes specific to an electric car"""
        super().__init__(make, model, year) #la funcion super es una fucnion especial que le permite llamar un metodo de la clase padre
        self.battery = Battery()         #le dice a python que llame a init a esta seccion


    def describe_battery(self):
       
        """print a statement describing the battery size"""
        print(f"this car has : {self.battery_size}-kWh battery.")





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


    gas = Battery()
    gas.fill_gas_tank()

    my_tesla = ElectricCar('tesla', 'model s', 2019)
    print(my_tesla.get_descriptive_name())
    my_tesla.battery.describe_battery()

    gas.get_range()

if __name__ == "__main__":
    main()

