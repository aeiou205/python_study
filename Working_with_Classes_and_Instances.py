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
        self.odometer_reading = mileage



def main():

    my_new_car = Car('AUDI','a4',2019)
    print(my_new_car.get_descriptive_name())

    """Modifying an Attribute’s Value Directly"""
    my_new_car.odometer_reading = 20432103
    my_new_car.read_odometer()
    my_new_car.update_odometer(213987632198743987213)
    my_new_car.read_odometer()




if __name__ == "__main__":
    main()
